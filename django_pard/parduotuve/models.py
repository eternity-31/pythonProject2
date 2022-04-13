from django.db import models

class Product(models.Model):

    name = models.CharField('ID', max_length=200, help_text='Please make an order')

    def __str__(self):
        return self.name


 #
from django.urls import reverse

class Order(models.Model):

    """Modelis reprezentuoja uzsakyma"""
    ID = models.CharField('ID', max_length=200)
    Customer_ID = models.ForeignKey('Customer_ID', on_delete=models.SET_NULL, null=True)
    Date = models.TextField('date', max_length=1000, help_text='product ordered date')
    Status_ID = models.CharField('Status_ID', max_length=13)
    Product= models.ManyToManyField(Product, help_text='Choose the correct product for that order')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Nurodo konkretaus uzsakymo atlikima"""
        return reverse('order-detail', args=[str(self.id)])
import uuid

class Product_order(models.Model):
    """Modelis, aprašantis produkto užsakymą"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus užsakymo_ID')
    product_ID = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    quantity = models.DateField('yra', null=True, blank=True)

    ORDER_STATUS = (
        ('o', 'Ordering'),
        ('b', 'Basket'),
        ('c', 'completed'),
        ('p', 'Paid'),
    )

    Status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS,
        blank=True,
        default='o',
        help_text='Status',
    )

    class Meta:
        ordering = ['paid']

    def __str__(self):
        return f'{self.id} ({self.book.title})'

    class Customer(models.Model):
        """Model representing a Customer."""
        first_name = models.CharField('Name', max_length=100)
        last_name = models.CharField('Lastname', max_length=100)

        class Meta:
            ordering = ['last_name', 'first_name']

        def get_absolute_url(self):
            """Returns the url to access a particular customer instance."""
            return reverse('customer-detail', args=[str(self.id)])

        def __str__(self):
            """String for representing the Model object."""
            return f'{self.last_name} {self.first_name}'

