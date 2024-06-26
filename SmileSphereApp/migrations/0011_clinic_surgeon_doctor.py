# Generated by Django 4.2.5 on 2024-02-27 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SmileSphereApp', '0010_patient_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='clinic_photos/')),
                ('location', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Surgeon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('available_days', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='surgeon_photos/')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmileSphereApp.clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('available_days', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='doctor_photos/')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmileSphereApp.clinic')),
            ],
        ),
    ]
