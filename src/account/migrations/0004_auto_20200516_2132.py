# Generated by Django 3.0.6 on 2020-05-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_is_defaulter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_defaulter',
            field=models.BooleanField(default=False),
        ),
    ]