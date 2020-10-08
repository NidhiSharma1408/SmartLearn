# Generated by Django 3.1.1 on 2020-10-08 07:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('file', models.FileField(max_length=50000000, upload_to='library/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('stars', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(choices=[('Book', 'Book'), ('Note', 'Note')], default='Misc', max_length=20)),
                ('college', models.CharField(default=None, max_length=35)),
            ],
            options={
                'ordering': ('-stars',),
            },
        ),
    ]
