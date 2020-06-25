from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import DetailView, ListView, FormView
from .models import Post, Category
from .forms import CommentForm
from tinymce.views import render_to_image_list

def index(request,title):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    category = Category.objects.all()
    context = {
        'object_list': featured,
        'latest': latest,
        'category': category,
    }
    return render(request,'blog-posts.html',context)

def post(request,id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
    context = {
        'form': form,
        'post':post,

    }
    return render(request,'blog-post.html',context)

class CategoryView(DetailView):
    model = Category

    def get_queryset(self):
        category = super(CategoryView, self).get_queryset()
        return category

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        images = context['album'].images.all()
        context['images'] = sorted(images, key=lambda i: i.date_taken)
        return context
