# Generated by Django 5.1.3 on 2024-12-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0019_module_users_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]
