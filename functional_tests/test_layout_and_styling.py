from .base import functionalTest
class layoutAndStylingTest(functionalTest):
    def test_layout_and_styling(self):
        #Marci go to the homepage
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
           
        #and notice that the input box is nicely centered
            
        inputbox = self.browser.find_element_by_id('id_text')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            505,
            delta = 5        
        )