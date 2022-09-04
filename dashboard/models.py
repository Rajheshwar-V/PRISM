from statistics import mode
from django.db import models

# Create your models here.

class Study(models.Model):
    study_id = models.BigAutoField(primary_key=True)
    study_name = models.CharField(max_length=256)
    comment = models.TextField()

class StudyImages(models.Model):
    study_image_id = models.BigAutoField(primary_key=True)
    device = models.CharField(max_length=256)
    photo_type = models.CharField(max_length=256)
    image = models.ImageField(upload_to="images")
    highlight = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=50, blank=True)
    study_id = models.ForeignKey(Study, null=True, on_delete=models.SET_NULL)
