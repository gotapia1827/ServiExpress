# Generated by Django 4.1.2 on 2022-11-19 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_agenda_checklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='checklist',
        ),
    ]
