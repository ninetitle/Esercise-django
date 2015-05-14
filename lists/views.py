from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from lists.models import Item , List

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def new_list(request):
    lista = List.objects.create()
    item = Item.objects.create(text = request.POST['item_text'], list = lista )
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        lista.delete()
        error = "You can't have an empty list item"
        return render(request,'home.html',{'error': error})
        
    return redirect(lista) #use the get_absolute_url function automatically

#def view_list(request,list_id):
#    lista = List.objects.get(id=list_id)
#    return render(request, 'list.html', {'list': lista})

def view_list(request, list_id):
    lista = List.objects.get(id=list_id)
    error = None
    if request.method == 'POST':
        try:
            item = Item(text = request.POST['item_text'], list = lista )
            item.full_clean()
            item.save()
            return redirect(lista)
        except:
            error = "You can't have an empty list item"
    return render(request, 'list.html', {'list': lista,'error': error})