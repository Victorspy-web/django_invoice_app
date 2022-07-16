from django.db import models
from profiles.models import Profile
from receivers.models import Receiver

class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# Create your models here.
class Invoice(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reciever = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    number = models.CharField(max_length=150)
    completion_date = models.DateField()
    issue_date = models.DateField()
    payment_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    # if closed then hide the positions and ability add new ones
    closed = models.BooleanField(default=False)
    # for educational purposes only
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return f"Invoice number: {self.number}, PK: {self.pk}"
    
    @property
    def tags(self):
        return self.tags.all()
    
    @property
    def positions(self):
        return self.position_set.all()
    
    @property
    def total_amount(self):
        total = 0
        qs = self.get_positions
        for position in qs:
            total += position.amount
        return total