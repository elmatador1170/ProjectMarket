# Generated by Django 3.1.5 on 2021-01-25 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_market', '0003_project_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='is_public',
            new_name='ijs_public',
        ),
    ]