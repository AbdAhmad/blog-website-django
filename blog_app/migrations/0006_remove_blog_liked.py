# Generated by Django 4.0.1 on 2022-01-29 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_blog_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='liked',
        ),
    ]
