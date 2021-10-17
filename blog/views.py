from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Blog
from .forms import BlogForm, BlogCategoryForm
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'bloglist'

    def get_queryset(self):
        category = self.request.GET.get('category')
        if( category != 'All' and category != None):
            new_context = Blog.objects.filter(
                is_draft = False,
                category = category,
            )
        else:
            new_context = Blog.objects.filter(
                is_draft = False,
            )
        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCategoryForm(initial={'category':self.request.GET.get('category')})
        return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

class BlogCreateView(CreateView):
    success_url = reverse_lazy('blog:blog_list_view')
    template_name = 'blog_create.html'
    form_class = BlogForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BlogCreateView, self).form_valid(form)

class MyBlogListView(ListView):
    model = Blog
    template_name = 'my_blog.html'
    context_object_name = 'bloglist'

    def get_queryset(self):
        new_context = Blog.objects.filter(
            author = self.request.user.id,
        )
        return new_context
