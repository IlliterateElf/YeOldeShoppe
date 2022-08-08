from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('searching', views.searching, name='searching'),
    path('search+q=<str:pk>', views.search, name='search')
]

urlpatterns += staticfiles_urlpatterns()