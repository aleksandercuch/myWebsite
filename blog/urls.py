from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.postList, name='postList'),
    path('books/', views.bookList, name='bookList'),
    path('aboutMe/', views.aboutMe, name='aboutMe'),
    path('login/', views.loginTemplate, name='loginTemplate'),
    path('logout/', views.logOut, name='logoutTemplate'),
    path('reviews/', views.reviewsList, name='reviewsList'),
    path('books/<int:id_of_chapter>/', views.showChapterDetails, name='chapterDetails'),
    path('reviews/<int:id_of_review>/', views.showReviewDetails, name='reviewsDetails'),
    path('<int:id_of_post>/', views.showPostDetails, name='postDetails'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^delete/(?P<comment_id>.*)$', views.delete, name='delete-person')
]



