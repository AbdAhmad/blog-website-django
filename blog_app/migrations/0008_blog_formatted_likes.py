# Generated by Django 4.0.1 on 2022-01-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_blog_formatted_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='formatted_likes',
            field=models.CharField(default='', max_length=10),
        ),
    ]
