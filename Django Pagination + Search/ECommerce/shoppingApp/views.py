from django.shortcuts import render
from .models import*
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    product_objects = Products.objects.all()
   
    # search
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
   
    # paginator
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
        
    return render(request,'shoppingApp/index.html',{'product_objects':product_objects})

# ! pagination has to be under the search codes ! #


def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shoppingApp/detail.html',{'product_object':product_object})