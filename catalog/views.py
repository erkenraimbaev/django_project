from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'SkyStore'
    }
    return render(request, 'home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nНомер телефона: {phone_number}\nСообщение: {message}')
    return render(request, 'contacts.html')


def product(request, pk):
    # index_list = Product.objects.all()
    context = {
        'title': 'Карточка товара',
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'product.html', context)
