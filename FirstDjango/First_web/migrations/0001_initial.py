# Generated by Django 2.0.5 on 2018-05-22 02:49
#coding=UTF-8
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tab1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=1)),
                ('age', models.FloatField()),
            ],
        ),
    ]
