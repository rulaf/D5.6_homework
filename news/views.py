from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
# выводить список объектов из БД
from .models import *
from .filters import PostFilter
from .forms import PostForm  # импортируем нашу форму
from datetime import datetime

from django.views import View  # импортируем простую вьюшку

# =============== D5 Авторизация ==============================
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# ==============================================================


# Create your views here.
class NewsList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']
    paginate_by = 10
    form_class = PostForm

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
            'form': self.form_class,
            'all_post': Post.objects.all(),
            'time_now': datetime.utcnow(),
            'is_not_authors': not self.request.user.groups.filter(name='authors').exists(),
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


# дженерик для получения деталей новости
class NewsDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'news_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'new'
    permission_required = 'news.add_post'


# дженерик для создания объекта.
class NewsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'news_create.html'
    form_class = PostForm
    context_object_name = 'new'
    permission_required = 'news.add_post'


# для поиска публикаций
class NewsSearchView(LoginRequiredMixin, PermissionRequiredMixin, NewsList):
    template_name = 'search.html'
    permission_required = 'news.add_post'


# дженерик для редактирования объекта
class NewsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'news_update.html'
    form_class = PostForm
    permission_required = 'news.add_post'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления
class NewsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    context_object_name = 'new'
    success_url = '/news/'
    permission_required = 'news.add_post'

