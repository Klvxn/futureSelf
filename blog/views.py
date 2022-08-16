from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from .models import Blog


# Create your views here.
class BlogListView(ListView):

    template_name = 'blog_list.html'
    queryset = Blog.objects.filter(status='published')
    context_object_name = 'blogs_list'


class BlogDetailView(DetailView):

    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'


class BlogCreateView(LoginRequiredMixin, CreateView):

    model = Blog
    fields = ('title', 'content')
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog_create.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Your post has been submitted for review.')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class BlogEditView(LoginRequiredMixin, UpdateView):

    model = Blog
    fields = ('title', 'content')
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog_edit.html'

    def get(self, request, *args, **kwargs):
        if request.user != self.get_object().writer:
            return HttpResponseForbidden()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user != self.get_object().writer:
            return HttpResponseForbidden()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, DeleteView):

    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog_delete.html'

    def get(self, request, *args, **kwargs):
        if request.user != self.get_object().writer:
            return HttpResponseForbidden()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user != self.get_object().writer:
            return HttpResponseForbidden()
        return super().post(request, *args, **kwargs)
