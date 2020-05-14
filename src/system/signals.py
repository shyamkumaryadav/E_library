from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Issue, Book


@receiver(post_save, sender=Issue)
def update_book_today_stock(sender, instance, **kwargs):
    print("Issue is update!!!")
