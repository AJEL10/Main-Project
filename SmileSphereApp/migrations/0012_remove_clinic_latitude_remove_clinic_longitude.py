# Generated by Django 4.2.5 on 2024-02-27 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SmileSphereApp', '0011_clinic_surgeon_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='longitude',
        ),
    ]
