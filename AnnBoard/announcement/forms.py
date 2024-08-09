import random
from string import hexdigits
from allauth.account.forms import SignupForm
from django.conf import settings
from django.core.mail import send_mail
from django import forms
from .models import Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CommonSignupForm(SignupForm):
    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        user.is_active = False
        code = ''.join(random.sample(hexdigits, 5))
        user.code = code
        user.save()
        send_mail(
            subject='Код активации',
            message=f'Код активации аккаунта: {code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return user


class PostForm(forms.ModelForm):
    text = forms.CharField(label="Содержание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            # 'user',
            'category',
        ]


class CommentForm(forms.ModelForm):
    text = forms.CharField(label='Текст комментария')

    class Meta:
        model = Comment
        fields = {
        'text'
        }
