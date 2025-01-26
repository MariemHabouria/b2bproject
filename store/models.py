from django.db import models

from django.urls import reverse

from project.settings import AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):                           
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=128, null=True)
    slug = models.SlugField(max_length=128)
    budget = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    def __str__(self):   
        return self.name
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

class Demande(models.Model): 
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True) 
    
    product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to="fichiers",blank=True)

   
    