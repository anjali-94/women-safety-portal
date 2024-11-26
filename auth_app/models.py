from django.db import models

# Create your models here.
class Story(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Story {self.id}"


# Custom User Registration Model
class UserRegistration(models.Model):
    # Custom fields for registration
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)  # Email is unique
    contact_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Store password (hashed)
    confirm_password = models.CharField(max_length=128)  # Confirmation password
    emergency_contact1 = models.CharField(max_length=15, blank=True, null=True)
    emergency_contact2 = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

