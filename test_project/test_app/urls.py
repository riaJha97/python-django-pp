from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^book_movie/$', views.book_movie, name='book_movie'),
    url(r'^pick_cinema/(?P<movie_name>[a-zA-Z0-9\/\-_\s]+)/$', views.available_cinemas, name='available_cinemas'),
    url(r'^admin/', include(admin.site.urls)),
]
