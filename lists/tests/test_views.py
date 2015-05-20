from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape
from unittest import skip 

from lists.models import Item , List
from lists.views import home_page
from lists.forms import ItemForm, EMPTY_ITEM_ERROR

class HomePageTest(TestCase):

    def test_home_page_render_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
        
    def test_home_page_uses_item_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], ItemForm)
        

class ListViewTest(TestCase):
    
    def post_invalid_input(self):
        lista = List.objects.create()
        return self.client.post(
            '/lists/%d/' %(lista.id,),
            data={'text' : ''}
        )
    def test_for_invalid_input_nothing_saved_to_db(self):
        self.post_invalid_input()
        self.assertEqual(Item.objects.count(),0)
        
    def test_for_invalid_input_render_list_template(self):
        response = self.post_invalid_input()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        
    def test_for_invalid_imput_passes_form_to_template(self):
        response = self.post_invalid_input()
        self.assertIsInstance(response.context['form'], ItemForm)
    
    def test_for_invalid_imput_shows_error_message(self):
        response = self.post_invalid_input()
        self.assertContains(response, escape(EMPTY_ITEM_ERROR))
        
    def test_diplay_item_form(self):
        lista = List.objects.create()
        response = self.client.get('/lists/%d/' %(lista.id,))
        self.assertIsInstance(response.context['form'], ItemForm)
        self.assertContains(response,'name="text"')
    
    
    def test_uses_list_template(self):
        lista = List.objects.create()
        response = self.client.get('/lists/%d/' %(lista.id,))
        self.assertTemplateUsed(response,'list.html')
        
    def test_display_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text= 'Oggetto 1', list = correct_list)
        Item.objects.create(text= 'Oggetto 2', list = correct_list)
        
        other_list = List.objects.create()
        Item.objects.create(text='Altra lista 1', list= other_list)
        Item.objects.create(text='Altra lista 2', list= other_list)
        
        response= self.client.get('/lists/%d/' %(correct_list.id,))
        
        self.assertContains(response,'Oggetto 1')
        self.assertContains(response,'Oggetto 2')
        
        self.assertNotContains(response,'Altra lista 1')
        self.assertNotContains(response,'Altra lista 2')
        
    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertEqual(response.context['list'], correct_list)
    
    @skip
    def test_duplicate_item_validation_error_end_up_on_list_page(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1,text='textey')
        response = self.client.post(
            '/lists/%d/' %(list1.id,),
            data={'text' : 'textey'}
        )
        
        expected_error = escape("You have already got this in your list")
        self.assertContains(response, 'list.html')
        self.assertTemplateUsed(response,'list.html')
        self.assertEqual(Item.objects.all().count(),1)

        
class NewListTest(TestCase):
#    def test_saving_a_POST_request(self):
#        self.client.post(
#            '/lists/new',
#            data ={'text':'A new list item'}
#        )
#        self.assertEqual(Item.objects.count(), 1)
#        new_item = Item.objects.first()
#        self.assertEqual(new_item.text, 'A new list item')
    
    
    def test_page_redirect_after_post(self):
        response = self.client.post(
            '/lists/new',
            data ={'text':'A new list item'}
        )
        new_list = List.objects.first()
        self.assertRedirects(response ,'/lists/%d/'%(new_list.id,))
        
    
    def test_for_invalid_input_renders_home_template(self):
        response = self.client.post('/lists/new', data = {'item_text':''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_validation_error_are_shown_on_home_page(self):
        response = self.client.post('/lists/new', data = {'item_text':''})
        self.assertContains(response, escape(EMPTY_ITEM_ERROR))
        
    def test_for_invalid_input_passes_form_to_template(self):
        response = self.client.post('/lists/new', data = {'item_text':''})
        self.assertIsInstance(response.context['form'], ItemForm)
        

    def test_invalid_list_items_arent_saved(self):
        response = self.client.post('/lists/new', data = {'item_text':''})
        self.assertEqual(List.objects.count(),0)
        self.assertEqual(Item.objects.count(),0)
        
    
    def test_can_save_a_post_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        
        self.client.post(
            '/lists/%d/' %(correct_list.id,),
            data={'text': 'A new item for an existing list'}
            )
        
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new item for an existing list')
        self.assertEqual(new_item.list,correct_list)
        
    
    def test_POST_redirect_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()  
        
        response =self.client.post(
            '/lists/%d/' %(correct_list.id,),
            data={'text': 'A new item for an existing list'}
            )
        
        self.assertRedirects(response,'/lists/%d/' %(correct_list.id,))
        
    

        
