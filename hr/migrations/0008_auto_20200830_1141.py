# Generated by Django 3.0.7 on 2020-08-30 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0007_salaryemp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salaryemp',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='salaryemp',
            name='emp_name',
        ),
        migrations.RemoveField(
            model_name='salaryemp',
            name='sal',
        ),
    ]
