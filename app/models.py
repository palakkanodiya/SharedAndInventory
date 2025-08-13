from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Variant(models.Model):
    product_id = models.CharField(max_length=255)  
    sku = models.CharField(max_length=255, unique=True)
    attributes = models.JSONField()
    inventory = models.JSONField()
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)