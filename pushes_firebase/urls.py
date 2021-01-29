from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from notification import views

urlpatterns = [
    path('admin/', admin.site.urls, name='login'),
    path('', views.get_home_page, name='home_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Сервис пуш-рассылок"
admin.site.site_title = "Администрирование"
admin.site.index_title = "Привет! Здесь ты можешь управлять пуш-уведомлениями"