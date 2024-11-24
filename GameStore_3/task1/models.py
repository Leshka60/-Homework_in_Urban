from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    size = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    age_limited = models.BooleanField(default=False, validators=[MinValueValidator(18)])
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title
