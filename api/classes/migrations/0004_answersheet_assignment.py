# Generated by Django 3.1.1 on 2020-09-24 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0007_auto_20200925_0048'),
        ('classes', '0003_auto_20200923_2248'),
    ]

    operations = [
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
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_linked', models.FileField(blank=True, max_length=1500000, upload_to='class/answers')),
                ('marks_scored', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('late_submitted', models.BooleanField(default=False)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.assignment', verbose_name='question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.userprofile')),
            ],
        ),
    ]