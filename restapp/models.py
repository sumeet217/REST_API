from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    enrolled_date = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.name