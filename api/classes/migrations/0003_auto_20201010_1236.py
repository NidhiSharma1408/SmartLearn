# Generated by Django 3.1.1 on 2020-10-10 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20201009_0500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignment',
            options={'ordering': ('-time_created',)},
        ),
        migrations.AlterModelOptions(
            name='classroom',
            options={'ordering': ('-id',)},
        ),
    ]
