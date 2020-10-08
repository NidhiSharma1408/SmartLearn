# Generated by Django 3.1.1 on 2020-10-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
        ('forum', '0002_auto_20201008_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmarked', to='userauth.UserProfile'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='voter',
            field=models.ManyToManyField(blank=True, related_name='voted', to='userauth.UserProfile'),
        ),
    ]
