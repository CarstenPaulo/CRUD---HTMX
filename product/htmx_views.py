from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def check_product(request):
    name = request.GET.get("name")
    products = Product.objects.filter(name=name)
    return render(request, "partials/check_product.html")


def save_product(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    
    objSave = Product(
        name=name,
        price=price,
    )
    objSave.save()
    products = Product.objects.all()
    return render(request,'partials/list_product.html',{"products":products})


from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_product(request,id):
    obj_delete = Product.objects.get(id=id)
    obj_delete.delete()
    products = Product.objects.all()
    return render(request,'partials/list_product.html',{"products":products})
