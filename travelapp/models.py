from django.db import models

# Create your models here.
class Travelapp(models.Model):
    head = models.CharField(max_length=300)
    traveler = models.CharField(max_length=150)
    load_date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.head

    def summary(self):
        return self.content[:200]