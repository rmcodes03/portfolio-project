from django.db import models

class Projects(models.Model):
    project_image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=1000)
