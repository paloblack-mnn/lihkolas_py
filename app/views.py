from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from app.models import Pages,Gallery
from gallery.models import Image, Album
from gallery import models
from blog.models import Category
from blog import models
from . import models
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

# Create your views here.


def index(request):
        obj = Pages.objects.get(name='home')
        gallery = Album.objects.all()
        category = Category.objects.all()
        date_dict = {'pages':obj,'gallery':gallery,'category':category}
        return render(request,'app/index.html',context=date_dict)

def test(request):
    return render(request,'app/test.html')

class GallerylListView(ListView):
        # If you don't pass in this attribute,
        # Django will auto create a context name
        # for you with object_list!
        # Default would be 'school_list'

        # Example of making your own:
        # context_object_name = 'schools'
        model = models.Gallery

class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'gallery.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context

class GalleryDetailView(DetailView):
    context_object_name = 'gallery_details'
    model = models.Gallery
    template_name = 'app/gallery.html'

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

def base(request):
        category = Category.objects
        category_dict = {'category':category}
        return render(request,'app/base.html',context=category_dict)
