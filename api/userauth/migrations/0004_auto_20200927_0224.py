# Generated by Django 3.1.1 on 2020-09-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_otpmodel_is_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='is_teacher',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
