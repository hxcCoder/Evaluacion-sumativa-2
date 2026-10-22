
from django.db import models
from django.core.validators import MinValueValidator


class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField(
        validators=[MinValueValidator(1886)]
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
