from django.shortcuts import render

def home(request):
    return render(request, 'weather/home.html')

def aboutus_view(request):
    return render(request, 'aboutus.html')