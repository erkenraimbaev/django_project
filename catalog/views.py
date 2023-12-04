from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    # template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    # template_name = 'product_detail.html'


# def home(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'SkyStore'
#     }
#     return render(request, 'product_list.html', context)

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone_number = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nНомер телефона: {phone_number}\nСообщение: {message}')
        return redirect(reverse('catalog:contacts'))


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone_number = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'Имя: {name}\nНомер телефона: {phone_number}\nСообщение: {message}')
#     return render(request, 'contacts.html')

# def product(request, pk):
#     # index_list = Product.objects.all()
#     context = {
#         'title': 'Карточка товара',
#         'object': Product.objects.get(pk=pk)
#     }
#     return render(request, 'product_detail.html', context)
