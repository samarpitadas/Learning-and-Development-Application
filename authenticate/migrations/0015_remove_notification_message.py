# Generated by Django 5.1.3 on 2024-12-13 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0014_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='message',
        ),
    ]
