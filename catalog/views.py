from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'C:/Users/USER/PycharmProjects/django_project/catalog/templates/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nНомер телефона: {phone_number}\nСообщение: {message}')
    return render(request, 'C:/Users/USER/PycharmProjects/django_project/catalog/templates/contacts.html')
