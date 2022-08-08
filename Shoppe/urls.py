from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.rdrct, name='rdrct'),
    path('index', views.index, name='index'),
    path('searching', views.searching, name='searching'),
    path('search+q=<str:pk>', views.search, name='search'),
    path('i+<str:pk>', views.view_item, name='view_item'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup')
]

urlpatterns += staticfiles_urlpatterns()