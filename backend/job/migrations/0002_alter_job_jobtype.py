# Generated by Django 5.0.1 on 2024-01-11 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobType',
            field=models.CharField(choices=[('Permanent', 'Permanent'), ('Temporary', 'Temporary'), ('Internship', 'Intership')], default='Permanent', max_length=20),
        ),
    ]
