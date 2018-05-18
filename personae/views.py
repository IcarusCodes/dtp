from django.shortcuts import render

def index(request):
    return render(request, 'personae/home.html')
