from django.shortcuts import render
from django.utils import timezone
from .models import Post, Chapter, Review

def postList(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/postList.html', {'posts': posts})

def bookList(request):
    chapters = Chapter.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'books/bookList.html', {'chapters': chapters})

def aboutMe(request):
   return render(request, 'about/aboutMe.html', {})

def loginTemplate(request):
   return render(request, 'login/loginTemplate.html', {})

def reviewsList(request):
    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'reviews/reviewsList.html', {'reviews': reviews})