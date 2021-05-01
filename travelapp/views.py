from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Travelapp
# Create your views here.

def start(request):
    travelapps = Travelapp.objects.all()
    return render(request,'start.html',{'travelapps':travelapps})

def click(request, id):
    travelapp = get_object_or_404(Travelapp, pk=id)
    return render(request,'click.html',{'travelapp':travelapp})

def update(request):
    return render(request,'update.html')

def made(request):
    new_travelapp = Travelapp()
    new_travelapp.head = request.POST['head']
    new_travelapp.traveler = request.POST['traveler']
    new_travelapp.content = request.POST['content']
    new_travelapp.load_date = timezone.now()
    new_travelapp.save()
    return redirect('click',new_travelapp.id)

def fix(request,id):
    fix_travelapp = Travelapp.objects.get(id = id)
    return render(request,'fix.html',{'travelapp':fix_travelapp})

def reupdate(request,id):
    reupdate_travelapp = Travelapp.objects.get(id = id)
    reupdate_travelapp.head = request.POST['head']
    reupdate_travelapp.traveler = request.POST['traveler']
    reupdate_travelapp.content = request.POST['content']
    reupdate_travelapp.load_date = timezone.now()
    reupdate_travelapp.save()
    return redirect('click',reupdate_travelapp.id)

def erase(request, id):
    erase_travelapp = Travelapp.objects.get(id=id)
    erase_travelapp.delete()
    return redirect('start')