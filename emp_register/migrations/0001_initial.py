# Generated by Django 3.0.7 on 2020-08-04 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('aadhar', models.CharField(max_length=12)),
                ('pan', models.CharField(max_length=20)),
                ('whrs', models.IntegerField()),
                ('oemail', models.EmailField(max_length=254)),
                ('pemail', models.EmailField(max_length=254)),
                ('designation', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('doj', models.DateField()),
                ('address', models.TextField()),
                ('job_loc', models.TextField()),
                ('bank_name', models.CharField(max_length=100)),
                ('ba_no', models.BigIntegerField()),
                ('pfno', models.CharField(max_length=25)),
                ('salary', models.CharField(max_length=15)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_register.Department')),
            ],
        ),
    ]