from django.db import models

# Create your models here.
class medicine(models.Model):
    age=models.FloatField()
    sex=models.FloatField()
    bmi=models.FloatField()
    children=models.FloatField()
    smoker=models.FloatField()
    region=models.FloatField()
    charges=models.FloatField()
