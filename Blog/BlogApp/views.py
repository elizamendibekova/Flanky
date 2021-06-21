from django.shortcuts import reverse, redirect, render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Post, UserPost, Comment, UserDislike, UserLike
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CommentForm, LikeForm, DislikeForm

class IndexView(generic.ListView):
    template_name = 'BlogApp/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.all().order_by('pub_date')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'BlogApp/detail.html'
    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

class CreatePostView(generic.edit.CreateView):
    fields = ['title', 'body']
    template_name = 'BlogApp/create_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

    def get_success_url(self):
        return reverse('BlogApp:index')

class UpdateQuestionView(generic.edit.UpdateView):
    template_name = "BlogApp/update_question.html"
    fields = ['title', 'body']

    def get_success_url(self):
        return reverse('BlogApp:index')

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

class DeleteQuestionView(generic.edit.DeleteView):
    template_name = "BlogApp/confirm_delete_post.html"

    def get_success_url(self):
        return reverse('BlogApp:index')

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

class RegisterView(generic.edit.FormView):
    form_class = UserCreationForm
    success_url = "/войти/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterView, self).form_invalid(form)

class LoginView(generic.edit.FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "registration/login.html"

    def form_valid(self, form):
        form.save()
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)

def liked(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST'
    form = LikeForm(request.POST)
    if form.is_valid():
        if request.user.is_authenticated:
            if not UserLike.objects.filter(user=request.user, post=post) and not UserDislike.objects.filter(user=request.user, post=post):
                like = UserLike(user=request.user, post=post)
                post.likes += 1
                like.save()
                post.save()
            return redirect('Blog:detail', post.question.id)
        else:
            return redirect('Blog:login')
    else:
        form = LikeForm()
    return redirect('Blog:detail', post.pk)

def disliked(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = DislikeForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                if not UserDislike.objects.filter(user=request.user, post=post) and not UserLike.objects.filter(user=request.user, post=post):
                    dislike = UserDislike(user=request.user, post=post)
                    post.dislikes += 1
                    dislike.save()
                    post.save()
                return redirect('BlogApp:detail', post.id)
            else:
                return redirect('BlogApp:login')
    else:
        form = DislikeForm()
    return redirect('BlogApp:detail', post.pk)