from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime


def index(request):
    request.session['counter'] = 0
    return render(request, 'index.html')
    
def get_farm(request):
    rand = random.randint(10,20)
    request.session['counter'] += rand
    # request.session[].append(f"Earned {rand} golds from the farm!")
    return redirect('/process_money')

def get_cave(request):
    rand = random.randint(5,10)
    request.session['counter'] += rand
    return redirect('/process_money')

def get_house(request):
    rand = random.randint(2,5)
    request.session['counter'] += rand
    return redirect('/process_money')

def get_casino(request):
    rand = random.randint(-50,50)
    request.session['counter'] += rand
    return redirect('/process_money')

def process_money(request):
    return render(request, 'index.html')


