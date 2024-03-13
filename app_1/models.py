from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'Clientname: {self.name}, email: {self.email}'
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_of_products = models.IntegerField()
    add_date = models.DateField()
    image = models.ImageField(upload_to='media/upload', null=True, blank=True)
    
    def __str__(self):
        return f'Product: {self.name}, with price {self.price}'
    
    

class Order(models.Model):
    clients = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField()
    
    
    def __str__(self):
        return f'{self.clients}, ordered {self.products} with total price: {self.total_price}'
    

