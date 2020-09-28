# Generated by Django 3.1.1 on 2020-09-28 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_linked', models.FileField(blank=True, max_length=1500000, upload_to='class/answers')),
                ('marks_scored', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('late_submitted', models.BooleanField(default=False)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('time_created', models.DateTimeField(auto_now=True)),
                ('submit_by', models.DateTimeField(blank=True, null=True)),
                ('max_marks', models.DecimalField(decimal_places=1, default=100, max_digits=5)),
                ('file_linked', models.FileField(blank=True, max_length=1500000, null=True, upload_to='class/assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=50, unique=True)),
                ('subject_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='DoubtSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('doubt_text', models.TextField(max_length=300)),
                ('file', models.FileField(blank=True, max_length=1500, null=True, upload_to='doubt-pdf/')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom', to='classes.classroom', verbose_name='Classroom')),
            ],
        ),
    ]
