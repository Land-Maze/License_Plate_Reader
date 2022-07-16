from django.db import models

# Create your models here.

class License(models.Model):
    license_number = models.CharField(max_length=100, blank=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title