# Generated by Django 3.1.1 on 2020-09-17 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coordinates', '0003_requesthistory_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesthistory',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
