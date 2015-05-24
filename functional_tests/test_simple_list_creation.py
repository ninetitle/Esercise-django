from .base import functionalTest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import sys
class newVisitorTest(functionalTest):
    def test_can_start_list_and_retrieve_later(self):
        
        #Marci had heard of a cool new online to-do app.
        #  He goes to check out the homepage
        self.browser.get(self.server_url)

        #He notice the page title and header mention the to-do list
        self.assertIn("To-Do",self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        
        #He is invited to enter a to-do list straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'enter a To-Do item'
        )
        #he types "Buy bloodborne" in to a text box
        inputbox.send_keys('Buy Bloodborne')

        #when he hit enter, he is taken to another page 
        #with the list "1:buy Bloodborne"
        inputbox.send_keys(Keys.ENTER)
        Marci_list_url = self.browser.current_url
        self.assertRegexpMatches(Marci_list_url,'/lists/.+')
        self.check_for_row_in_list_table('1. Buy Bloodborne')

        #there still is a text box initing him to add another item
        #he enter "Play Bloodborne on ps4"
        inputbox = self.browser.find_element_by_id('id_text')
        inputbox.send_keys('Play Bloodborne on ps4')
        inputbox.send_keys(Keys.ENTER)
        #the page update again, and now there are both item on the list
        self.check_for_row_in_list_table('2. Play Bloodborne on ps4')
        self.check_for_row_in_list_table('1. Buy Bloodborne')
        
        #Now another users, Francesco, come along to the site.
        #We use a new browser session to ensure that no information#
        #of Marci is coming throught cookies etc.#
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        #Fancesco visit the home page, there is no trace of
        #Marci's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy Bloodborne',page_text)
        self.assertNotIn('Play Bloodborn on ps4',page_text)
        
        #Francesco inizia una nuova lista inserendo un nuovo oggetto
        #e' meno interessante di quella di Marci
        inputbox= self.browser.find_element_by_id('id_text')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        
        #Francesco get his own unique url
        Francesco_list_url = self.browser.current_url
        self.assertRegexpMatches(Francesco_list_url,'/lists/.+')
        self.assertNotEqual(Marci_list_url, Francesco_list_url)
        
        #again, no trace of Marci list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy Bloodborne',page_text)
        self.assertIn('Buy milk',page_text)
        