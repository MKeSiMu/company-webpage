from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Purchaser(AbstractUser):

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class BearingCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class BearingType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bearing_category = models.ForeignKey(
        BearingCategory,
        on_delete=models.CASCADE,
        related_name="bearing_types"
    )

    class Meta:
        ordering = ["bearing_category"]

    def __str__(self):
        return f"{self.name} ({self.bearing_category})"


class Manufacturer(models.Model):
    BUSINESS_MODEL_CHOICES = (
        ("M", "Manufacturer"),
        ("T", "Trader")
    )
    PRICE_LEVEL_CHOICES = (
        ("H", "High"),
        ("A", "Average"),
        ("L", "Low")
    )
    STATUS_CHOICES = (
        ("A", "ACTIVE"),
        ("B", "BLOCKED"),
        ("N", "NEW"),
        ("P", "POTENTIAL"),
    )
    RATING_CHOICES = (
        ("A", "Excellent"),
        ("B", "Good"),
        ("C", "Just so so"),
        ("D", "Bad"),
        ("F", "Disaster")
    )
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    business_model = models.CharField(
        max_length=1,
        choices=BUSINESS_MODEL_CHOICES
    )
    contact_person = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    website = models.URLField(
        max_length=255,
        null=True,
        blank=True
    )
    produce_bearing_type = models.ManyToManyField(
        BearingType,
        related_name="manufacturers"
    )
    responsible_purchaser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    price_level = models.CharField(
        max_length=1,
        choices=PRICE_LEVEL_CHOICES,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        null=True,
        blank=True
    )
    rating = models.CharField(
        max_length=1,
        choices=RATING_CHOICES,
        null=True,
        blank=True
    )
    remark = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.responsible_purchaser})"
