# Generated by Django 4.1.2 on 2022-11-19 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_rename_chassis_agenda_chasis'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='checklist',
            field=models.CharField(max_length=30, null=True),
        ),
    ]