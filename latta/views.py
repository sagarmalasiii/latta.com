from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def shop(request):
    return render(request,'shop.html')

def why(request):
    return render(request,'why.html')

def testimonial(request):
    return render(request,'testimonial.html')

def contact(request):
    return render(request,'contact.html')
