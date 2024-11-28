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


class Complaint(models.Model):
    INCIDENT_TYPES = [
        ('harassment', 'Harassment'),
        ('domestic_violence', 'Domestic Violence'),
        ('workplace_discrimination', 'Workplace Discrimination'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=255, help_text="City or Area")
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPES, default='other')
    incident_date = models.DateField(help_text="Date of Incident")
    complaint = models.TextField(help_text="Describe the incident in detail")
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.incident_type} on {self.incident_date}"



class Feedback(models.Model):
    email = models.EmailField(max_length=255)
    feedback = models.TextField(help_text="Provide your feedback")
    rating = models.CharField(
        max_length=10,
        choices=[('average', 'Average'), ('good', 'Good'), ('poor', 'Poor')],
        default='good'
    )
    suggestion = models.TextField(help_text="Any suggestions?", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.email} on {self.created_at}"
