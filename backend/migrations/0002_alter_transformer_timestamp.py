# Generated by Django 4.0 on 2021-12-23 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transformer',
            name='TimeStamp',
            field=models.DateTimeField(),
        ),
    ]