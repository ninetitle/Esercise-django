from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
        
    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows= table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_list_and_retrieve_later(self):
        
        #Marci had heard of a cool new online to-do app.
        #  He goes to check out the homepage
        self.browser.get(self.live_server_url)

        #He notice the page title and header mention the to-do list
        self.assertIn("To-Do",self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        
        #He is invited to enter a to-do list straight away
        imputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            imputbox.get_attribute('placeholder'),
            'enter a To-Do item'
        )
        #he types "Buy bloodborne" in to a text box
        imputbox.send_keys('Buy Bloodborne')

        #when he hit enter, he is taken to another page with the list "1:buy Bloodborne"
        imputbox.send_keys(Keys.ENTER)
        marci_list_url = self.browser.current_url
        self.assertRegex(marci_list_url,'/lists/.+')
        self.check_for_row_in_list_table('1. Buy Bloodborne')
        
        #there still is a text box initing him to add another item
        #he enter "Play Bloodborne on ps4"
        imputbox = self.browser.find_element_by_id('id_new_item')
        imputbox.send_keys('Play Bloodborne on ps4')
        imputbox.send_keys(Keys.ENTER)
        #the page update again, and now there are both item on the list
        self.check_for_row_in_list_table('2. Play Bloodborne on ps4')
        
        #Now another users, Francesco, come along to the site.
        #We use a new browser session to ensure that no information#
        #of Marci is coming throught cookies etc.#
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        #Fancesco visit the home page, there is no trace of
        #Marci's list
        self.browse.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy Bloodborne',page_test)
        self.assertNotIn('Play Bloodborn on ps4',page_test)
        
        #Francesco inizia una nuova lista inserendo un nuovo oggetto
        #è meno interessante di quella di Marci
        inputbox= self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        
        #Francesco get his own unique url
        self.assertRegex(Francesco_list_url,'/lists/.+')
        selfAssertNotEqual(Marci_list_url, Francesco_list_url)
        
        #again, no trace of Marci list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy Bloodborne',page_test)
        self.assertIn('Buy milk',page_test)
        
        #Marci wonder if the site will remember the list for him
        #Then he sees that the site had generated an unique url for             him--- there 
        self.fail('finish the test !')
        #is some explanatory text to that effect

        #he visit that url, and the list is still there

        #satisfied, he goes to sleep


