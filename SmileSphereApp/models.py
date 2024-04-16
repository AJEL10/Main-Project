from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class SuperAdmin(models.Model):
    email = models.EmailField(unique=True, default='admin@admin.com')
    password = models.CharField(max_length=100, default='admin123')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class Patient(models.Model):
    
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class Appointment(models.Model):
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Accepted'),
        (3, 'Rejected'),
    )
    date = models.DateField()
    description = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES)
    patient_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    appointment_time = models.DateTimeField()
    


    def __str__(self):
        return f"Appointment {self.id} for {self.patient.email} on {self.date}"
    def save(self, *args, **kwargs):
        # Check if appointment_time is not set and set it to current time
        if not self.appointment_time:
            self.appointment_time = timezone.now()
        super().save(*args, **kwargs)





class Clinic(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='clinic_photos/')
    location = models.CharField(max_length=200)
    password = models.CharField(max_length=100, default='default_value_here')

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    available_days = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctor_photos/')
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

class Surgeon(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    available_days = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='surgeon_photos/')
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)


