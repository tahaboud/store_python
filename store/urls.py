# from django.conf.urls import url

# from . import views

# app_name = 'store'
# urlpatterns = [
#     url(r'^listing$', views.listing, name='listing'),
#     url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^search/$', views.search, name='search'),
# ]
##################################################################################

from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [

    path('listing/', views.listing, name='listing'),
    path('<album_id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]
