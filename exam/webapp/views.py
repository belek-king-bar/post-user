from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponseRedirect, request
from webapp.models import Post, UserInfo
from webapp.forms import PostForm, UserInfoForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, Http404
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-created_at')

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_update.html'

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super(PostUpdateView, self).get_object(queryset)
        if self.object.author == self.request.user:
            return self.object
        else:
            raise Http404


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = 'post_list.html'




class UserInfoListView(ListView):
    model = UserInfo
    template_name = 'user_list.html'


class UserInfoDetailView(LoginRequiredMixin, DetailView):
    model = UserInfo
    template_name = 'user_detail.html'


class UserInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'user_update.html'

    def get_success_url(self):
        return reverse('webapp:user_detail', kwargs={'pk': self.object.pk})