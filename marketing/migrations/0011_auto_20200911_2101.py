# Generated by Django 3.0.7 on 2020-09-11 15:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0010_auto_20200911_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_quot',
            name='executive',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emp_quot',
            name='project_end_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emp_quot',
            name='project_leader',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emp_quot',
            name='project_start_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emp_quot',
            name='project_status',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emp_quot',
            name='remarks',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emp_quot',
            name='source_code',
            field=models.FileField(default=0, upload_to='source'),
            preserve_default=False,
        ),
    ]
