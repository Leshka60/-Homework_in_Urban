from django.shortcuts import render
from .forms import UserRegister

# Create your views here.
users = ['Aleks', 'Pit', 'Kat']


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            users.append(username)
            info['message'] = f'Приветствуем, {username}!'
    else:
        info['username'] = request.POST.get('username', '')
    return render(request, 'registration_page.html', {'form': info})


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password']
            repeat_password = form.cleaned_data.get['repeat_password']
            age = form.cleaned_data.get['age']

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                users.append(username)
                info['message'] = f'Приветствуем, {username}!'
        else:
            form = UserRegister()
            info['message'] = form
        return render(request, 'registration_page.html', {'form': info})
