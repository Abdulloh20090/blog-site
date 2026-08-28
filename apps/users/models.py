from django.db import models
from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    
    def __str__(self):
        return self.full_name