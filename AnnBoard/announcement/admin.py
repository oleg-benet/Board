from .models import Post, User, Category, Comment, Subscriber
from django.contrib import admin
#from modeltranslation.admin import TranslationAdmin

# class PostAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Post._meta.get_fields()]
#     list_display.remove('category')
#     list_display.remove('postcategory')
#     list_display.remove('comment')
#     list_filter = ('title', 'rating', 'author', 'post_time')
#     search_fields = ('id', 'author__user__username')
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

admin.site.register(Post)
admin.site.register(User,)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Subscriber)

