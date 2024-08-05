from django.forms import DateInput
from django_filters import FilterSet
from .models import Comment, Post
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostFilter(FilterSet):

    class Meta:
        model = Comment
        fields = {
            'post'
        }

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['post'].quaryset = Post.objects.filter(user__id=kwargs['request'])
        