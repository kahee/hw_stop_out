from django.urls import path

from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.webtoon_list, name='webtoon-list'),
    # localhost:8000/1
    path('<int:pk>/', views.webtoon_detail, name='webtoon-detail')
]
