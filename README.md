Учебный проект NewsPaper по модулю D5.6 -"Авторизация и регистрация"

Добавлены функции авторизации/регистрации в ранее созданый учебный проект NewsPaper.

(для работы проекта требуется установка дополнительного модуля django-filter и
django-allauth)

1. В классе-представлении редактирования профиля UserUpdateView была добавлена добавить 
проверка аутентификации при помощи LoginRequiredMixin.
2. Установлен и настроен пакет allauth.Были выполнены необходимые настройки пакета allauth в файле конфигурации.
3. В файле конфигурации определён адрес для перенаправления на страницу входа в 
систему: http://127.0.0.1:8000/accounts/login/ и адрес перенаправления после успешного входа
на страничку авторизованного пользователя
4. Реализован шаблон с формой входа в систему и выполнена настройка конфигурации URL.
5. Реализован шаблон страницы регистрации пользователей:
6. Реализована возможность регистрации через Google-аккаунт.
7. Созданы группы common и authors.
8. Реализовано автоматическое добавление новых пользователей в группу common.
9. Создана возможность стать автором (быть добавленным в группу authors). Добавлена ссылка на главной странице проекта -/news/
10. Для группы authors в админ панели были предоставлены права создания и редактирования объектов модели 
Post (новостей и статей).
11. В классах-представлениях добавления и редактирования новостей и статей была доблена 
проверку прав доступа.
