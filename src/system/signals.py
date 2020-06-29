from django.db import models
from django.dispatch import receiver
from .models import Issue, Book, Genre


@receiver(models.signals.pre_save, sender=Book)
def p_update_book_today_stock(sender, instance, **kwargs):
    instance.today_stock = instance.stock - instance.issue_set.all().count()


@receiver(models.signals.post_save, sender=Issue)
def issue_update_book_today_stock(sender, instance, created, **kwargs):
    instance.book.today_stock = instance.book.stock - instance.book.issue_set.count()
    instance.book.save(update_fields=['today_stock'])


@receiver(models.signals.post_delete, sender=Issue)
def issue_delete_update_book_today_stock(sender, instance, **kwargs):
    instance.book.today_stock = instance.book.stock - instance.book.issue_set.count()
    instance.book.save(update_fields=['today_stock'])

@receiver(models.signals.post_delete, sender=Genre)
def on_del_genre(sender, instance, **kwargs):
    sender.objects.test0001()

def create_genre(sender, *args, **kwargs):
    n=sender.models['genre'].objects.test0001()
    if n > 0:print('Y '*n)
    else: pass
