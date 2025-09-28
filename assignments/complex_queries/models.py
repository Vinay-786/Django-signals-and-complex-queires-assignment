from django.db import models


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        MEXICAN = 'MX', 'Mexican'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        CHINESE = 'CH', 'Chinese'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length=120)
    restaurant_type = models.CharField(
        max_length=2,
        choices=TypeChoices.choices,
    )
    date_opened = models.DateField()


class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    expenditure = models.DecimalField(max_digits=10, decimal_places=2)
