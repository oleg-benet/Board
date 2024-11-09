from .models import Post, User, Category, Comment  # , Subscriber
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'user', 'category', 'create_time', 'update_time']
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Comment)
