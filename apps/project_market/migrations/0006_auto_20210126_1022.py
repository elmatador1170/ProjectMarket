# Generated by Django 3.1.5 on 2021-01-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_market', '0005_auto_20210125_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='is_public',
        ),
        migrations.AddField(
            model_name='project',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Privat'),
        ),
    ]
