from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList, name='postList'),
    path('books/', views.bookList, name='bookList'),
    path('aboutMe/', views.aboutMe, name='aboutMe'),
    path('login/', views.loginTemplate, name='loginTemplate'),
    path('reviews/', views.reviewsList, name='reviewsList'),
]