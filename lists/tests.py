from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string


from lists.models import Item , List
from lists.views import home_page

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
        
    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected_html)
        
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


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response,'list.html')
        
    def test_display_all_items(self):
        lista = List.objects.create()
        Item.objects.create(text= 'Oggetto 1', list = lista)
        Item.objects.create(text= 'Oggetto 2', list = lista)
        
        response= self.client.get('/lists/the-only-list-in-the-world/')
        
        self.assertContains(response,'Oggetto 1')
        self.assertContains(response,'Oggetto 2')
        
        
class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post(
            '/lists/new',
            data ={'item_text':'A new list item'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
    
    def test_page_redirect_after_post(self):
        response = self.client.post(
            '/lists/new',
            data ={'item_text':'A new list item'}
        )
        
        self.assertRedirects(response ,'/lists/the-only-list-in-the-world/')