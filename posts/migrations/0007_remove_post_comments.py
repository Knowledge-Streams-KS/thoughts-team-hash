# Generated by Django 4.2.5 on 2023-10-16 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_is_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
