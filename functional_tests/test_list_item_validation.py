from .base import functionalTest
class itemValidationTest(functionalTest):  
    
    def test_cannot_add_empty_list_items(self):
        #Marci go to the home page and accidently try to submit an empty item
        #He hit enter on the empty box
        self.browser.get(self.live_server_url)
        self.inserisci_textbox('id_text','\n')
        #The home page refresh and now these is an error message saying
        #that the list item cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text,"You can't have an empty list item")
        
        #He tries with a real item that work
        self.browser.find_element_by_id('id_text').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1. Buy milk')
        #now he tries the add another blank list item
        #and receive a similar warning on the list page
        
        self.browser.find_element_by_id('id_text').send_keys('\n')
        self.check_for_row_in_list_table('1. Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text,"You can't have an empty list item")
        
        #and he can correct it by filling some text in
        self.browser.find_element_by_id('id_text').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1. Buy milk')
        self.check_for_row_in_list_table('2. Make tea')
    
    def test_cannot_add_duplicate_items(self):
        #Marci goes to the home page and start a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy the witcher 3\n')
        self.check_for_row_in_list_table('1. Buy the witcher 3')
        
        #He incidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy the witcher 3\n')
        
        #He sees an helpful error message
        self.check_for_row_in_list_table('1. Buy the witcher 3')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You have already got this in your list")