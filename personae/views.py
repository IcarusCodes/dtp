from django.shortcuts import render

def index(request):
    return render(request, 'personae/home.html')

def contact(request):
    return render(request, 'personae/basic.html', {'content':['Do franzen DIY butcher ut cred excepteur roof party, consectetur fugiat meh cardigan in. Put a bird on it pinterest lorem, scenester pok pok schlitz banh mi bespoke crucifix cred culpa food truck vaporware sustainable.']})
