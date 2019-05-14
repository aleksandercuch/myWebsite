from django.db import models
from django.utils import timezone
from djrichtextfield.models import RichTextField
from froala_editor.fields import FroalaField



class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = FroalaField()
    created_date = models.DateTimeField(default=timezone.now)


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    comments = models.ManyToManyField(Comment, blank=True)
    text = FroalaField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Chapter(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book = models.CharField(max_length = 40)
    title = models.CharField(max_length=200)
    comments = models.ManyToManyField(Comment, blank=True)
    number = models.IntegerField()
    text = FroalaField()
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    book = models.CharField(max_length=40, blank=True, null=True)
    comments = models.ManyToManyField(Comment, blank=True)
    writer = models.CharField(max_length=40, blank=True, null=True)
    text = FroalaField()
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.book



