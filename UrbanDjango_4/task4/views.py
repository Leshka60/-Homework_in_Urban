from django.shortcuts import render


# Create your views here.
def platform(request):
    return render(request, 'platform.html')


def games(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'Pay Day 2']
    context = {'games': games}
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')
