from django.contrib import admin

from store.models import Category, Product, Demande
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Demande)

