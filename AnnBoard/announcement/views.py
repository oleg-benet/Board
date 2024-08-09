from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment, User, Post
from .filters import PostFilter
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm



class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'invalid_code.html')
        return redirect('account_login')


class ProfileView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'profile.html'
    context_object_name = 'comments'

    def get_queryset(self):
        queryset = Comment.objects.filter(post__user__id=self.request.user.id)
        self.filterset = PostFilter(self.request.GET, queryset, request=self.request.user.id)
        if self.request.GET:
            return self.filterset.qs
        return Comment.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        return super().form_valid(form)




class PostEdit(LoginRequiredMixin, UpdateView):
    # permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    pk_url_kwarg = 'id'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'


class PostList(ListView):
    model = Post
    ordering = '-update_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    # paginate_by = 10


class CommentCreate(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    model = Comment
    template_name = 'comment_create.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.request.path[1::]
        context['post_id'] = post_id
        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        post_id = self.request.path[1::]
        comment.post = Post.objects.get(id=post_id)
        comment.user = self.request.user
        comment.save()
        message = f"Поступил новый отклик на объявление {post_id}"
        rec = comment.post.user
        send_mail(
            subject='Новый отклик',
            message=message,
            from_email='benetal@yandex.ru',
            recipient_list=[rec.email, ]
        )
        return super().form_valid(form)


class AcceptedCommentList(ListView):
    model = Comment
    template_name = 'comment_list.html'
    context_object_name = 'comments'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Comment.objects.filter(status=True)
        length = queryset.count()
        context['length'] = length
        return context


class CommentDelete(DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


def accept(request, id):
    Comment.objects.filter(id=id).update(status=True)
    comment = Comment.objects.get(id=id)
    rec = comment.user
    message = f"Ваш отклик на объявление {comment.post.id} принят"
    send_mail(
        subject='Отклик принят',
        message=message,
        from_email='benetal@yandex.ru',
        recipient_list=[rec.email, ]
    )

    return redirect('profile')
