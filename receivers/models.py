from datetime import datetime
from django.db import models

# Create your models here.
class Receiver(models.Model):
    """ Class for the company that recieves the invoice """
    name = models.CharField(max_length=200)
    address = models.TextField()
    website = models.URLField(blank=True)
    created = models.DateTimeField(default=datetime.now)
    
    #add later
    #logo = 
    
    def __str__(self):
        return self.name