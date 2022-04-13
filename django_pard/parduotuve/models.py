from django.db import models
from django.urls import reverse
import uuid

class Product(models.Model):
    name = models.CharField(max_length=200, help_text='Please make an order')

    def __str__(self):
        return self.name

class Status(models.Model):
    id = models.IntegerField(primary_key=1)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    """Model representing a Customer."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular customer instance."""
        return reverse('customer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name} {self.first_name}'


class Order(models.Model):
    """Modelis reprezentuoja uzsakyma"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus užsakymo_ID')
    Customer_ID = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    Date = models.DateTimeField(help_text='product ordered date')
    Status_ID = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    Product = models.ManyToManyField(Product, help_text='Choose the correct product for that order')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Nurodo konkretaus uzsakymo atlikima"""
        return reverse('order-detail', args=[str(self.id)])


class Product_order(models.Model):
    """Modelis, aprašantis produkto užsakymą"""
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus užsakymo_ID')
    product_ID = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} ({self.book.title})'


