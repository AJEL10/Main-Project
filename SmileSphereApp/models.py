from django.db import models
from django.contrib.auth.models import User
class Usertable(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=100)  # You should consider using a secure password hashing library
    # You can add more fields as needed

    def __str__(self):
        return self.username
