from .base import functionalTest
from unittest import skip
class itemValidationTest(functionalTest):
    @skip    
    def test_cannot_add_empty_list_items(self):
        #Marci go to the home page and accidently try to submit an empty item
        #He hit enter on the empty box
        
        #The home page refresh and now these is an error message saying
        #that the list item cannot be blank
        
        #He tries with a real item that work
        
        #now he tries the add another blank list item
        #and receive a similar warning on the list page
        
        #and he can correct it by filling some text in
        
        self.fail('Write me')