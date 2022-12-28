from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=30)


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    related_person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_resolved = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.item_name
