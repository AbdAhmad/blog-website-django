# Generated by Django 4.0.1 on 2022-01-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_rename_likes_blog_likes_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user_likes',
            field=models.ManyToManyField(blank=True, related_name='user_likes', to='blog_app.Like'),
        ),
    ]
