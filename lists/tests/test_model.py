from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item , List


class ItemModelTest(TestCase):

    def cannot_save_empty_list_item(self):
        lista= List.object.create()
        item = Item(list=lista, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()
            

        
    def test_duplicate_items_are_invalid(self):
        lista = List.objects.create()
        Item.objects.create(list=lista, text='bla')
        with self.assertRaises(ValidationError):   #il test passa se raise validation error
            item = Item(list = lista,text='bla')   #and the code after is always run
            item.full_clean()
            
            
    def test_CAN_save_item_to_different_list(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1,text='bla')
        item = Item(list=list2, text='bla')
        item.full_clean()   #should not raise
        
    def test_default_text(self):
        item= Item()
        self.assertEqual(item.text,'')
        
    def test_item_is_related_to_list(self):
        lista = List.objects.create()
        item = Item()
        item.list = lista
        item.save()
        self.assertIn(item,lista.item_set.all())
        

class ListModelTest(TestCase):
        def test_get_absolute_url(self):
            lista = List.objects.create()
            self.assertEqual(lista.get_absolute_url(), '/lists/%d/' %(lista.id,) )