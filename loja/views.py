from django.http import HttpResponse
from django.shortcuts import render
from .models import Produto

# Create your views here.

def loja(request):
    # return HttpResponse("loja")
    
    latest_product_list = Produto.objects.all()
    
    print(latest_product_list)
    
    context = {
        "latest_product_list": latest_product_list
    }
    return render(request, 'loja.html', context)

def carrinho(request):
    return render(request, 'base.html')