# Generated by Django 4.0.1 on 2022-01-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
