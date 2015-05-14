from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item , List


class ListandItemModelTest(TestCase):
    def test_saving_and_retrieving_item(self):
        lista = List()
        lista.save()
        
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = lista
        first_item.save()
        
        second_item= Item()
        second_item.text = 'Item the second'
        second_item.list = lista
        second_item.save()
        
        saved_list = List.objects.first()
        self.assertEqual(saved_list,lista)
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, lista)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, lista)
    
    
    def cannot_save_empty_list_item(self):
        lista= List.object.create()
        item = Item(list=lista, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()
            
    def test_get_absolute_url(self):
        lista = List.objects.create()
        self.assertEqual(lista.get_absolute_url(), '/lists/%d/' %(lista.id,) )