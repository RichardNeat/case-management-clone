from django.db import models

# Create your models here.

class Application(models.Model):
    applicant_name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    submission_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")
    supporting_document = models.FileField(upload_to="uploads/", null=True, blank=True)

    def __str__(self):
        return f"{self.applicant_name} ({self.status})"
    
class DataUpload(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at= models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.name
    