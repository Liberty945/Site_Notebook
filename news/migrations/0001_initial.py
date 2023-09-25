# Generated by Django 4.2.2 on 2023-06-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер задачи')),
                ('title', models.CharField(max_length=50, verbose_name='Название задачи')),
                ('text', models.CharField(max_length=250, verbose_name='Описание задачи')),
            ],
            options={
                'verbose_name': 'Задачу',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
