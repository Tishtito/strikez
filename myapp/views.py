from django.shortcuts import render, redirect
from .models import Member


# Create your views here.
def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        username=request.POST['username'],
                        password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html', )


def login(request):
    return render(request, 'login.html')


def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'home.html', {'member': member})
        else:
            return render(request, 'login.html')


def games(request):
    return render(request, 'games.html')


def home2(request):
    return render(request, 'home.html')


def players(request):
    return render(request, 'players.html')


def show(request):
    Players = Member.objects.all()
    return render(request, 'players.html', {'Players': Players})

def hall(request):
    return render(request, 'halloffame.html')

