# Generated by Django 3.2.15 on 2022-09-11 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
