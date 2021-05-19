class TestMainPage1:
    def test_add_to_basket_button(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        add_to_basket_button = browser.find_element_by_class_name("btn-add-to-basket")
        assert add_to_basket_button.is_displayed() == True, 'Button is not displayed'
