# Generated by Django 4.2.5 on 2024-02-22 04:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SmileSphereApp', '0007_alter_superadmin_email_alter_superadmin_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
