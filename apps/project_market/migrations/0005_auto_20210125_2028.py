# Generated by Django 3.1.5 on 2021-01-25 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_market', '0004_auto_20210125_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='ijs_public',
            new_name='is_public',
        ),
    ]
