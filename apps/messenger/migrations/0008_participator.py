# Generated by Django 3.1.5 on 2021-01-31 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0007_remove_conversation_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participator', models.CharField(max_length=100)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger.conversation')),
            ],
        ),
    ]
