from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

import unittest


class functionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        #self.browser.refresh()
        self.browser.quit()       
        
    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows= table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def inserisci_textbox(self,box,text):
            name = self.browser.find_element_by_id(box)
            name.send_keys(text)
            
    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

