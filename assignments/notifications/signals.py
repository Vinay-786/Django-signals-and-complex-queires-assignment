from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post, DeletePost
from django.utils.text import slugify
from django.db.models.signals import (
    post_save,
    pre_save,
    pre_delete,
    m2m_changed
)


def send_welcome_email(user_email: str):
    print(f"Email sent to {user_email}")


@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, update_fields, *args, **kwargs):
    if created or update_fields:
        send_welcome_email(instance.username)
        # django admin don't require email stricly to create user hence
        # username as dummy mail
    else:
        print(f'{instance.username} saved')


@receiver(pre_save, sender=Post)
def post_pre_save_handler(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


@receiver(pre_delete, sender=Post)
def post_pre_delete_handler(sender, instance, *args, **kwargs):
    # print(args, kwargs)
    postobj = kwargs.get("origin")
    delete_post_instance = DeletePost(
        title=postobj.title, slug=postobj.slug, active=False)
    delete_post_instance.save()


@receiver(m2m_changed, sender=Post.tags.through)
def post_m2m_handler(sender, instance, action, model, *args, **kwargs):
    if action == "pre_add":
        qs = model.objects.filter(pk__in=kwargs.get('pk_set'))
        for user in qs:
            print(
                f"User(s) tagged:\n{user.id}:{user.username} {timezone.now()}\n")
    if action == "post_remove":
        qs = model.objects.filter(pk__in=kwargs.get('pk_set'))
        for user in qs:
            print(
                f"User(s) untagged:\n{user.id}:{user.username} {timezone.now()}\n")
