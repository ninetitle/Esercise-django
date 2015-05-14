from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class List(models.Model):
    def get_absolute_url(self):
        return reverse('view_list', args =[self.id] )
        #Reverse ritorna un url prendendolo da 'view_list' sotto urls con come argomento 
        #l'id dell'oggetto
        
    # nota anche se e' vuoto la classe inerita il metodo che produce il campo id e lo applica

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List,default=None)


    