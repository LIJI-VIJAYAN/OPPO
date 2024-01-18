from django.db import models

# Create your models here.
class ProductDetails(models.Model):
    Name=models.CharField(max_length=100) 
    Price=models.IntegerField()
    Description=models.CharField(max_length=450)
    Storagespace=models.IntegerField()
    Imagename=models.ImageField(upload_to='product_images/', null=True, blank=True)
    Stock = models.IntegerField()

class ProductBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    quantity = models.IntegerField()
    product = models.ForeignKey('ProductDetails', on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.name} - {self.product.name}"
