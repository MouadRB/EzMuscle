# Generated by Django 5.0.4 on 2024-05-03 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='UserProfile.user'),
        ),
        migrations.AlterField(
            model_name='athlet',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='UserProfile.user'),
        ),
    ]
