from django.urls import path

from . import views

urlpatterns = [
    path('', views.webtoon_list, name='webtoon-list'),
]
