# Generated by Django 4.2.3 on 2023-10-10 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='post_comments', to='posts.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='posts.post'),
        ),
    ]
