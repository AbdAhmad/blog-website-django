# Generated by Django 4.0.1 on 2022-01-29 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_remove_blog_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='formatted_views',
            field=models.CharField(default='', max_length=10),
        ),
    ]