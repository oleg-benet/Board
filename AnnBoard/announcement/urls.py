from django.urls import path
from .views import (ConfirmUser, ProfileView, PostCreate, PostEdit, PostDetail, PostList, CommentCreate,
                    AcceptedCommentList, CommentDelete, accept)

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('confirm/', ConfirmUser.as_view(), name='confirm_user'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:id>/edit/', PostEdit.as_view(), name='post_edit'),
    path('post/<int:id>', PostDetail.as_view(), name='post_detail'),
    path('<int:id>', CommentCreate.as_view(), name='comment_create'),
    path('comments/<int:id>', AcceptedCommentList.as_view(), name='comment_list'),
    path('comment/<int:id>/delete/', CommentDelete.as_view(), name='comment_delete'),
    path('comment/<int:id>/accept/', accept, name='accept')
]
