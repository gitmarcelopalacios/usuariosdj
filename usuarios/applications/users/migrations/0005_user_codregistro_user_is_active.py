# Generated by Django 4.2.6 on 2024-02-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='codregistro',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
