from playwright.sync_api import expect
# def test_locators_get_by_label(page):
#     page.goto("https://demowebshop.tricentis.com/")
#     register_link = page.get_by_text ("Register")
#     register_link.click()
#     #page.get_by_role("radio", name ="Female").check()
#     page.get_by_label("Male").nth(0).check()
#     page.get_by_label("First name:").fill('abc')
#     page.get_by_label("Last name:").fill('xyz')
#     page.get_by_label("Email:").fill('abc@gmail.com')
#     page.get_by_label("Password:").nth(0).fill('abc123')
#     page.get_by_label("Confirm password:").nth(0).fill('abc123')
#     page.get_by_role("button", name = "Register").click()
    
# def test_get_by_placeholder(page):
#       page.goto("https://www.amazon.com/")  
#       page.get_by_placeholder("Search Amazon.in").fill("books")
#       page.keyboard("Enter")
      
      
# def test_get_by_alt_text(page):
#     page.goto("https://demowebshop.tricentis.com/")
#     logo = page.get_by_alt_text("Tricentis Demo Web Shop")
#     expect(logo).to_be_visible()

def test_get_by_title(page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    logo = page.get_by_title("Tricentis Academy")
    expect(logo).to_be_visible()
    