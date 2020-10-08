# Generated by Django 3.1.1 on 2020-10-08 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
        ('library', '0002_auto_20201008_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='bookmark',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doc_bookmarked', to='userauth.userprofile'),
        ),
        migrations.AlterField(
            model_name='document',
            name='voter',
            field=models.ManyToManyField(blank=True, related_name='star_voter', to='userauth.UserProfile'),
        ),
    ]
