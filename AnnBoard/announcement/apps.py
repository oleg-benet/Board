from django.apps import AppConfig


class AnnouncementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'announcement'

    #def ready(self):
       #import announcement.signals
       #from .signals import send_notifications, notify_category_post
