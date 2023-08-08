from django.shortcuts import render
from .models import Finch


# Create your views here.
def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finch/index.html', { 'finches': finches})   

def home(request):
    return render(request, 'home.html')

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finch/details.html', {'finch': finch})