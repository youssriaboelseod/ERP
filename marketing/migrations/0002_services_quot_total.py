# Generated by Django 3.0.7 on 2020-09-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services_quot',
            name='total',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
