# Generated by Django 3.2.8 on 2021-11-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_posts_sub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='commentss',
        ),
        migrations.AddField(
            model_name='posts',
            name='commentss',
            field=models.ManyToManyField(blank=True, to='post.Comment'),
        ),
    ]
