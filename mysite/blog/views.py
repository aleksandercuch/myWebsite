from django.utils import timezone
from .models import Post, Chapter, Review
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def postList(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/postList.html', {'posts': posts})


def bookList(request):
    chapters = Chapter.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'books/bookList.html', {'chapters': chapters})


def aboutMe(request):
   return render(request, 'about/aboutMe.html', {})



def loginTemplate(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('../')
        else:
            return render(request, 'login/loginTemplate.html', {'form': form})
    else:
        return render(request, 'login/loginTemplate.html', {'form': form})


def reviewsList(request):
    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'reviews/reviewsList.html', {'reviews': reviews})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode,
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Proszę potwierdzić adres e-mail w celu dokończenia rejestracji.')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Dziękujemy za potwierdzenie rejestracji. Możesz teraz zalogować się na swoje konto!')
    else:
        return HttpResponse('Link aktywacyjny jest już nieważny!')


def logOut(request):
    logout(request)
    return redirect('/')


def showChapterDetails(request, id_of_chapter):
    chapter = Chapter.objects.get(id=id_of_chapter)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            chapter.comments.add(form)
            chapter.save()
            form = CommentForm()

    return render(request, 'books/chapterDetails.html', {'chapter': chapter, 'form': form})


def showPostDetails(request, id_of_post):
    post = Post.objects.get(id=id_of_post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            post.comments.add(form)
            post.save()
            form = CommentForm()

    return render(request, 'blog/postDetails.html', {'post': post, 'form': form})


def showReviewDetails(request, id_of_review):
    review = Review.objects.get(id=id_of_review)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            review.comments.add(form)
            review.save()
            form = CommentForm()

    return render(request, 'reviews/reviewsDetails.html', {'review': review, 'form': form})