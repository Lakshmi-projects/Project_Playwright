from playwright.sync_api import expect

def test_locators_get_by_role(page):
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name ="Log in").click()
    page.get_by_role("textbox",name="Email").fill("abc@gmail.com")
    page.get_by_role("textbox",name="password").fill("abc123")
    page.get_by_role("button",name="Log in").click()
    
def test_get_by_text(page):
    page.goto("https://www.facebook.com/?locale=en_US")
    login_to_facebook_text = page.get_by_text("Log in to Facebook")
    expect(login_to_facebook_text).to_be_visible()
    forgot_password_buttons = page.get_by_text("Forgotten Password?")
    forgot_password_buttons.click()
    
    