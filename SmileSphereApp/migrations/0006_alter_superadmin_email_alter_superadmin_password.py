# Generated by Django 5.0.2 on 2024-02-18 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmileSphereApp', '0005_appointment_created_at_appointment_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superadmin',
            name='email',
            field=models.EmailField(default='admin@example.com', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='superadmin',
            name='password',
            field=models.CharField(default='your_default_password', max_length=100),
        ),
    ]