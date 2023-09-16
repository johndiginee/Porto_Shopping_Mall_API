
from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class OrderStatus(models.TextChoices):
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'

class PaymentStatus(models.TextChoices):
    PAID = 'PAID'
    UNPAID = 'UNPAID'

class PaymentMode(models.TextChoices):
    COD = 'COD'
    CARD = 'CARD'

class Order(models.Model):
    """Represent an Order.
    
    Attributes:
        address: The name of the company as a string.
        city: The establishment date of the company as a positive integer.
        state: The city where the company is located as a string.
        zip_code: The state where the company is located as a string.
        phone_no: The state where the company is located as a string.
        country: The state where the company is located as a string.
        total_amount: The state where the company is located as a string.
        payment_status: The state where the company is located as a string.
        status: The state where the company is located as a string.
        payment_mode: The state where the company is located as a string.
    """
    address = models.CharField(max_length=500, default="", blank=False)
    city = models.CharField(max_length=100, default="", blank=False)
    state = models.CharField(max_length=100, default="", blank=False)
    zip_code = models.CharField(max_length=100, default="", blank=False)
    phone_no = models.CharField(max_length=100, default="", blank=False)
    country = models.CharField(max_length=100, default="", blank=False)
    total_amount = models.IntegerField(default=0)
    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNPAID
    )
    status = models.CharField(
        max_length=50,
        choices=OrderStatus.choices,
        default=OrderStatus.PROCESSING
    )

    payment_mode = models.CharField(
        max_length=50,
        choices=PaymentMode.choices,
        default=PaymentMode.COD
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    """Represent an OrderItem.
    
    Attributes:
        product: A foreign key of a product as a positive integer.
        order: A foreign key of an order as a positive integer.
        name: The name of the product as a string.
        quantity: The quantity of the product as an integer.
        price: The price of the item as a floating point.
        image: The image of the product as a string.
    """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name="orderitems")
    name = models.CharField(max_length=200, default="", blank=False)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    image = models.CharField(max_length=500, default="", blank=False)

    def __str__(self):
        return str(self.name)
