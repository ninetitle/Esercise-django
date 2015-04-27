from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_list_and_retrieve_later(self):
        
        #Marci had heard of a cool new online to-do app.
        #  He goes to check out the homepage
        self.browser.get("http://localhost:8000")

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

        #when he hit enter, the page updates, and now the page list "1:         buy Bloodborne"
        imputbox.send_keys(Keys.ENTER)
        
        imputbox = self.browser.find_element_by_id('id_new_item')
        imputbox.send_keys('Play Bloodborne on ps4')
        imputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows= table.find_elements_by_tag_name('tr')
#        self.assertTrue(
#            any(row.text == '1. Buy Bloodborne' for row in rows),
#            "New to-do items do not appear on the table -- it's text  was:\n%s" %(table.text,)
#        )
        self.assertIn('1. Buy Bloodborne', [row.text for row in rows])
        self.assertIn('2. Play Bloodborne on ps4', [row.text for row in rows])
        #there still is a text box initing him to add another item
        #he enter "Play Bloodborne on ps4"

        #the page update again, and now there are both item on the list

        #Marci wonder if the site will remember the list for him
        #Then he sees that the site had generated an unique url for             him--- there 
        self.fail('finish the test !')
        #is some explanatory text to that effect

        #he visit that url, and the list is still there

        #satisfied, he goes to sleep
if __name__=="__main__":
    unittest.main()


