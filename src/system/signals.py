from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Issue, Book


@receiver(post_save, sender=Book)
def update_book_today_stock(sender, instance, **kwargs):
    print("Issue is update!!!")


@receiver(pre_save, sender=Book)
def p_update_book_today_stock(sender, instance, **kwargs):
    print("Issue is p_update!!!")
