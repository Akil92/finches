from django.shortcuts import render

finches = [
    {'name': 'Tweety', 'description': 'yellow', 'age': 6},
    {'name': 'Tucan', 'description': 'rainbow', 'age': 4}
]

# Create your views here.
def about(request):
    return render(request, 'about.html')

def finch_index(request):
    return render(request, 'finch/index.html', { 'finches': finches})   

def home(request):
    return render(request, 'home.html')