from django.db import models

# Create your models here.
class Url(models.Model):
	shortened_url = models.CharField(max_length=8)
	original_url = models.CharField(max_length=4000)
	created_at = models.DateTimeField(auto_now_add=True)