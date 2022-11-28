# Generated by Django 4.1.2 on 2022-11-19 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_rename_tipouser_1_usuarios_tipouser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('patente', models.CharField(max_length=30)),
                ('chassis', models.IntegerField()),
                ('f_ingreso', models.DateField()),
                ('falla', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'agenda',
            },
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='f_crear',
            field=models.DateField(),
        ),
    ]
