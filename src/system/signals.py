# from django.db.models.signals import post_save, pre_save, post_delete, post_init, pre_init
from django.db import models
from django.dispatch import receiver
from .models import Issue, Book


@receiver(models.signals.pre_save, sender=Book)
def p_update_book_today_stock(sender, instance, **kwargs):
	instance.today_stock = instance.stock - instance.issue_set.all().count()

# @receiver(models.signals.post_save, sender=Book)
# def post_book_profile(sender, instance, created, **kwargs):
# 	# instance.refresh_from_db()
	# instance.today_stock = instance.stock - instance.issue_set.all().count()
	# pass
	# def getsize(size)

@receiver(models.signals.post_save, sender=Issue)
def issue_update_book_today_stock(sender, instance, created, **kwargs):
	instance.book.today_stock = instance.book.stock - instance.book.issue_set.count()
	instance.book.save(update_fields=['today_stock'])


@receiver(models.signals.post_delete, sender=Issue)
def issue_delete_update_book_today_stock(sender, instance, **kwargs):
	instance.book.today_stock = instance.book.stock - instance.book.issue_set.count()
	instance.book.save(update_fields=['today_stock'])
