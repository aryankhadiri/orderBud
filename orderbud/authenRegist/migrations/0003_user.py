# Generated by Django 3.1.6 on 2021-02-23 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authenRegist', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('manager', models.BooleanField(default=False, null=True)),
                ('username', models.TextField(max_length='15', unique=True, verbose_name='username')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
