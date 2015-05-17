from django.test import TestCase

from lists.forms import ItemForm, EMPTY_ITEM_ERROR
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