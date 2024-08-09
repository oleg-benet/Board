from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import  User, Post
from django.core.mail import send_mail

@receiver(post_save, sender=Post)
def notify_about_announcement(sender, instance, **kwargs):
    subject = 'На доске объявлений изменения'
    message = f'Появилось новое или отредактированное объявление с заголовком: {instance.title}'
    all_users = User.objects.all()
    recepients = []
    for user in all_users:
        recepients.append(user.email)
    send_mail(
        subject=subject,
        message=message,
        from_email='benetal@yandex.ru',
        recipient_list=recepients
    )