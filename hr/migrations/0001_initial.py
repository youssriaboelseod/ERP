# Generated by Django 3.0.7 on 2020-08-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('leave_type', models.CharField(choices=[('Earned', 'Earned/Previledge Leave'), ('sick', 'Sick Leave'), ('casual', 'Casual Leave'), ('other', 'Other leave')], max_length=50)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_id', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=100)),
                ('desgn', models.CharField(max_length=100)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('numdays', models.IntegerField()),
                ('reason', models.TextField()),
            ],
        ),
    ]
