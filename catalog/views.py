from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


# Create your views here.

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name_product', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:home')


class ProductListView(ListView):
    model = Product

    # template_name = 'product_list.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        for product in context_data['object_list']:
            active_version = Version.objects.filter(product=product, current_version=True).last()
            if active_version:
                product.active_version_number = active_version.version
                product.active_version_name = active_version.name_version
            else:
                product.active_version_number = None
                product.active_version_name = None
        return context_data


class ProductDetailView(DetailView):
    model = Product
    # template_name = 'product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ('name_product', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


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

# class VersionCreateView(CreateView):
#     model = Version
#     form_class = VersionForm
#     # fields = ('name_product', 'description', 'image', 'category', 'price')
#     success_url = reverse_lazy('catalog:home')
