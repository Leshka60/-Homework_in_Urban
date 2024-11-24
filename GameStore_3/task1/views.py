from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister
from .models import *

users = []
def platform(request):
    return render(request, 'platform.html')


def games(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games':games})


def cart(request):
    return render(request, 'cart.html')


def sign_up_by_html(request, form=None):

    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        users = Buyer.objects.values_list('name', flat=True)
        if password != repeat_password:
            info['error'] = "Пароли не совпадают"
        elif age < 18:
            info['error'] = "Вы должны быть старше 18"
        elif username in users:
            info['error'] = "Пользователь уже существует"
        else:
            Buyer.objects.create(name=username, balance=0.00, age=age)
            return HttpResponse(f"Приветствуем, {username}!")

    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')

            users = Buyer.objects.values_list('name', flat=True)
            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
            elif age < '18':
                info['error'] = "Вы должны быть старше 18"
            elif username in users:
                info['error'] = "Пользователь уже существует"
            else:
                Buyer.objects.create(name=username, balance=0.00, age=age)
                return HttpResponse(f"Приветствуем, {username}!")

    return render(request, 'registration_page.html', info)
