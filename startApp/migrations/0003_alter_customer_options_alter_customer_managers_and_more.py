# Generated by Django 5.0.4 on 2024-05-13 10:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startApp', '0002_answer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelManagers(
            name='customer',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]