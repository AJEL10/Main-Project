# Generated by Django 4.2.5 on 2024-02-23 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmileSphereApp', '0009_alter_appointment_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]