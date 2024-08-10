from .models import Post, User, Category, Comment #, Subscriber
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


# from modeltranslation.admin import TranslationAdmin

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'user', 'category', 'create_time', 'update_time']
    form = PostAdminForm



# class CommentAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Comment._meta.get_fields()]
#
#
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Author._meta.get_fields()]
#     list_display.remove('all_posts')
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']
#
#
# class TransPostAdmin(PostAdmin, TranslationAdmin):
#     model = Post
#
#
# class TransCategoryAdmin(CategoryAdmin, TranslationAdmin):
#     model = Category

# admin.site.register(Post, TransPostAdmin)
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Category, TransCategoryAdmin)
# admin.site.register(Comment, CommentAdmin)

admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Comment)
# admin.site.register(Subscriber)
