# Generated by Django 3.0.7 on 2020-09-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_services_quot_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='services_quot',
            name='technology',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]