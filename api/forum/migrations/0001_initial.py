# Generated by Django 3.1.1 on 2020-10-08 07:56

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
                ('text', models.TextField()),
                ('is_parent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, max_length=5000, null=True, upload_to='forum_posts')),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-votes'],
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('C++', 'C++'), ('Data Structure', 'Data Structure'), ('Art', 'Art'), ('Science', 'Science'), ('Mathematics', 'Mathematics'), ('Commerce', 'Commerce')], default='None', max_length=20)),
            ],
        ),
    ]
