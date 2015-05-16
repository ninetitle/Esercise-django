from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from lists.models import Item , List
from lists.forms import ItemForm
# Create your views here.

def home_page(request):
    return render(request,'home.html',{'form' : ItemForm()})

def new_list(request):
    form = ItemForm(data=request.POST) #si passa request.post data al costruttore del form
    if form.is_valid():                #usiamo .is_valid per determinare se l'inserzione è valida
        lista = List.objects.create()
        item = Item.objects.create(text = request.POST['text'], list = lista )
        return redirect(lista)
    else:
        return render(request, 'home.html',{'form' : form}) #in caso di fallimento invece di inserire una stringa di errore passiamo il form al template
        


def view_list(request, list_id):
    lista = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            item = Item.objects.create(text = request.POST['text'], list = lista )
            return redirect(lista)
    return render(request, 'list.html', {'list': lista, 'form': form})