from selenium import webdriver
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
        header_text = self.browser.find-element_by_tag('h1').text
        self.assertIn('To-Do',header_text)
        #self.fail("Finish the test!")
        #He is invited to enter a to-do list straight away

        #he types "Buy bloodborne" in to a text box

        #when he hit enter, the page updates, and now the page list "1: buy             Bloodborne"

        #there still is a text box initing him to add another item
        #he enter "Play Bloodborne on ps4"

        #the page update again, and now there are both item on the list

        #Marci wonder if the site will remember the list for him
        #Then he sees that the site had generated an unique url for him--- there 
        #is some explanatory text to that effect

        #he visit that url, and the list is still there

        #satisfied, he goes to sleep
if __name__=="__main__":
    unittest.main()


