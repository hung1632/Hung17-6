from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'index.html')
def phone(request):
    return render (request, 'phone.html')
def jobs(request):
    return render (request, 'jobs.html')
def invest(request):
    return render (request, 'invest.html')
def celeb(request):
    return render (request, 'celeb.html')
def sports(request):
    return render (request, 'sports.html')