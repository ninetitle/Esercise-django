from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item , List

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def new_list(request):
    lista = List.objects.create()
    Item.objects.create(text = request.POST['item_text'], list = lista )
    return redirect('/lists/%d/'%(lista.id,))

def add_item(request,list_id):
    lista = List.objects.get(id=list_id)
    Item.objects.create(text = request.POST['item_text'], list = lista )
    return redirect('/lists/%d/'%(lista.id,))   

#def view_list(request,list_id):
#    lista = List.objects.get(id=list_id)
#    return render(request, 'list.html', {'list': lista})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})