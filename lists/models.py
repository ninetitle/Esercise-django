from django.db import models

# Create your models here.
class List(models.Model):
    pass
    # nota anche se e' vuoto la classe inerita il metodo che produce il campo id

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List,default=None)


    