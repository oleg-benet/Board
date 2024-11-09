from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db.models import Sum
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy


class User(AbstractUser):
    code = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    # text = models.TextField()
    text = RichTextUploadingField(verbose_name="Содержание")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Объявление')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.post.id)])
