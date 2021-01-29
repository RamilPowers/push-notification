from django.contrib import admin
from .models import Notification
import requests
import datetime
from django.forms import TextInput, Textarea
from django.db import models
from pushes_firebase.settings import environment_variables


class NotificationAdmin(admin.ModelAdmin):

    """Управление рассылкой пуш-уведомлений через админку"""

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '95'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 95})},
    }
    list_display = [
        '__str__',
        'title',
        'created',
        'sending_status',
        'sent',
        'action',
    ]
    list_editable = [
        'action',
    ]
    readonly_fields = [
        'created',
        'sending_status',
        'sent',
    ]
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        """
        Переопределение метода Save админки

        При нажатии на кнопку сохранить отправялется POST-запрос
        к Firebase с параметрами, меняется статус отправки сообщения и
        сохраняется дата отправки уведомления, если пришел ответ 200.

        """
        url = "https://fcm.googleapis.com/fcm/send"
        key = environment_variables.FIREBASE_KEY
        headers = {
            'Content-type': 'application/json',
            'Authorization': f'key={key}',
        }
        data = {
            'to': obj.to,
            'priority': 'high',
            'content_available': True,
            'data': {
                'title': obj.title,
                'body': obj.description,
                'payload_title': obj.payload_title,
                'payload_body': obj.payload_body,
            },
        }

        if obj.sending_status != 'POSTED' and obj.action is True or obj.reaction is True:
            answer = requests.post(url, json=data, headers=headers)
            obj.sending_status = 'POSTED' if answer.status_code == 200 else 'ERROR'
            obj.sent = datetime.datetime.now() if obj.sending_status == 'POSTED' or obj.reaction is True else None
            obj.reaction = False
        obj.save()


admin.site.register(Notification, NotificationAdmin)
