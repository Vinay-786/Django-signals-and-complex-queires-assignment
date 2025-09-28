from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    tags = models.ManyToManyField(User, blank=True)
    notify_users = models.BooleanField(default=False)
    notify_users_timestamp = models.DateTimeField(
        blank=True, null=True, auto_now_add=False)
    active = models.BooleanField(default=True)


class DeletePost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    tags = models.ManyToManyField(User, blank=True)
    notify_users = models.BooleanField(default=False)
    notify_users_timestamp = models.DateTimeField(
        blank=True, null=True, auto_now_add=False)
    active = models.BooleanField(default=False)
