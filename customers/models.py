from django.db import models


class Customer(models.Model):
    persian_name = models.CharField(max_length=255, null=True)
    english_name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    city = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.persian_name
