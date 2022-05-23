from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255)
    plate_no = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CarInsuarance(models.Model):
    name = models.CharField(max_length=255)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    expire_date = models.DateTimeField()

    def __str__(self):
        return self.name


class CarMonitoring(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    distance = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return str(self.speed)
