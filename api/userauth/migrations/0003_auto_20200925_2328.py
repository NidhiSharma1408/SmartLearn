# Generated by Django 3.1.1 on 2020-09-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_auto_20200925_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]