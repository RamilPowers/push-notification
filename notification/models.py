from django.db import models


class Notification(models.Model):

    """Модель Уведомлений"""

    SENDING_STATUS = [
        ('POSTED', 'Отправлено'),
        ('WAITING', 'Ожидает отправки'),
        ('ERROR', 'Ошибка отправления')
    ]

    title = models.CharField("Пуш-уведомление. Заголовок", max_length=255)
    description = models.CharField("Пуш-уведомление. Описание", max_length=255)
    payload_title = models.CharField("Полезная нагрузка. Заголовок", max_length=255)
    payload_body = models.TextField("Полезная нагрузка. Описание")
    to = models.CharField("Токен устройства", max_length=164)
    created = models.DateField("Дата создания", auto_now_add=True)
    sent = models.DateTimeField("Дата отправки", default=None, null=True)
    sending_status = models.CharField("Состояние отправки", choices=SENDING_STATUS, default='WAITING', max_length=25)
    action = models.BooleanField("Отправить?", default=False)
    reaction = models.BooleanField("Отправить повторно", default=False)

    class Meta:
        verbose_name = 'Пуш-уведомление'
        verbose_name_plural = 'Пуш-уведомления'

    def __str__(self):
        return f'id {self.id}'
