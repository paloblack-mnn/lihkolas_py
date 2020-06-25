"""lihkolas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='index'),
    path('app/gallery/<int:pk>/', views.GalleryDetailView.as_view(),name='gallery_details'),
    path('gallery/', include('gallery.urls')),
    path('blog/', include('blog.urls')),
    path('portfolio/', views.index,name='portfolio'),
    path('about-us/', views.index,name='about-us'),
    path('base/', views.base,name='base'),
    path('test/', views.test,name='test'),
    path('admin/', admin.site.urls),
    path('tinymce/',include('tinymce.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
