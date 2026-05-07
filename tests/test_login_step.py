from pytest_bdd import given, when, then, parsers, scenarios
from frameworks.pages.login_page import LoginPage
scenarios('../features/login.feature')

@given('I open the login page')
def open_login_page(browser):
    login_page = LoginPage(browser)
    login_page.open_loinpage()
    
    
    
@when(parsers.parse('I login with "{username}" and "{password}"'))
def enter_credentials(browser, username, password):
    login_page = LoginPage(browser)
    login_page.login(username, password)
    
@then('I should see the home page')
def verify_home_page(browser):
    pass
        
        
        

        