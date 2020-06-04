from django.db.models.signals import post_save, pre_save, post_delete, post_init, pre_init
from django.dispatch import receiver
from .models import Issue, Book


@receiver(pre_save, sender=Book)
def p_update_book_today_stock(sender, instance, **kwargs):
    instance.today_stock = instance.stock - instance.issue_set.all().count()

@receiver(post_save, sender=Book)
def post_book_profile(sender, instance, created, **kwargs):
    pass
    # def getsize(size)

@receiver(post_save, sender=Issue)
def issue_update_book_today_stock(sender, instance, created, **kwargs):
    instance.book.today_stock = instance.book.stock - instance.book.issue_set.count()
    instance.book.save(update_fields=['today_stock'])


@receiver(post_delete, sender=Issue)
def issue_delete_update_book_today_stock(sender, instance, created, **kwargs):
    instance.book.today_stock = instance.book.stock - instance.book.issue_set.count()
    instance.book.save(update_fields=['today_stock'])
