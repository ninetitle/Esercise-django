from django.test import TestCase

from lists.forms import (
    DUPLICATE_ITEM_ERROR, EMPTY_ITEM_ERROR,
    ExistingListItemForm, ItemForm
)
from lists.models import List, Item

class ItemFormTest(TestCase):
    def test_form_renders_item_text_imput(self):
        form = ItemForm()
        self.assertIn('placeholder="enter a To-Do item"',form.as_p())
        self.assertIn('class="form-control input-lg"',form.as_p())
        
    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [EMPTY_ITEM_ERROR]
        )
    
    def test_form_handles_saving_a_list(self):
        lista = List.objects.create()
        form = ItemForm(data={'text' : 'do me'})
        new_item = form.save(for_list=lista)
        self.assertEqual(new_item,Item.objects.first())
        self.assertEqual(new_item.text,'do me')
        self.assertEqual(new_item.list, lista)
        
    def test_list_ordering(self):
        list1= List.objects.create()
        item1 =Item.objects.create(list=list1, text='i1')
        item2 =Item.objects.create(list=list1, text='item 2')
        item3 =Item.objects.create(list=list1, text='3')
        self.assertEqual(
            list(Item.objects.all()),
            [item1,item2,item3]
        )
        
    def test_string_representation(self):
        item=Item(text='some text')
        self.assertEqual(str(item),'some text')
        
class ExistingListItemFormTest(TestCase):
    
    def test_form_renders_item_text_input(self):
        lista = List.objects.create()
        form = ExistingListItemForm(for_list=lista)
        self.assertIn('placeholder="enter a To-Do item"', form.as_p())
        
    def test_form_validation_for_blank_items(self):
        lista = List.objects.create()
        form = ExistingListItemForm(for_list=lista, data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])
        

    def test_form_validation_for_duplicate_items(self):
        lista = List.objects.create()
        Item.objects.create(list=lista, text='no twins!')
        form = ExistingListItemForm(for_list=lista,data={'text' : 'no twins!'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'],[DUPLICATE_ITEM_ERROR])