from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .forms import FeedingForm


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
    id_list = finch.toys.all().values_list('id')
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    print(f"{finch.feeding_set.all()}")
    return render(request, 'finch/details.html', {
        'finch': finch, 
        'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have
        })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        print(f"new feeding{new_feeding}")
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    print(Finch.objects.get(id=finch_id).toys.all())
    return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['description', 'age']    

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'