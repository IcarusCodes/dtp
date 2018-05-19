from django.shortcuts import render

def index(request):
    return render(request, 'personae/home.html')

def contact(request):
    return render(request, 'personae/basic.html', {'content':['If you would like to contact me, please email me', 'stoian.alex94@yahoo.com']})
