from playwright.sync_api import sync_playwright,expect

def test_application():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        #user
        
        end_user_context = browser.new_context() #create a new browser context
        end_user_page = end_user_context.new_page() # Create a new page in the end user context
        end_user_page.goto("https://agents.akbartravelsonline.com/b2bplus/login")
        expect(end_user_page).to_have_title("Cheap Flights ; Domestic ; International Flight Offers in India")
        
        #admin
        
        admin_context = browser.new_context() #create a new browser context
        admin_page = admin_context.new_page() # Create a new page in the end user context
        admin_page.goto("https://agents.akbartravelsonline.com/b2bplus/login")
        expect(admin_page).to_have_title("Cheap Flights ; Domestic ; International Flight Offers in India")
