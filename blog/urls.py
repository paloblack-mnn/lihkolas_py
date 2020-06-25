from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from blog import views

from .views import index,post
app_name = 'blog'
urlpatterns = [
    path('<title>', index, name='blog_title'),
    path('post/<id>/', post, name ='post-details')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
