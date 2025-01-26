
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage


from store.models import Product,Demande
def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})


def postulerD(request, slug=None):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
      
      
      uploaded_file = request.FILES["document"]
      demande= Demande.objects.create(fichier="uploaded_file")
      demande.save()
     
    return render(request,'store/index.html', context={"products": product})
   
     
    return render(request, 'postuler.html', context={"products": product})