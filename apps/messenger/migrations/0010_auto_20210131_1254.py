# Generated by Django 3.1.5 on 2021-01-31 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0009_auto_20210131_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participator',
            old_name='participator',
            new_name='username',
        ),
    ]
