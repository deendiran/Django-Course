from django.db import models

# Create your models here.
class Tour(models.Model):
    """
        We need :
        1. a origin country, 
        2. a destination,  
        3. number of nights and 
        4. the price for that tour.
    """
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

