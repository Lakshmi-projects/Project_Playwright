from playwright.sync_api import sync_playwright,expect

def test_google(page):
    page.goto("https://www.google.com")
    print(page.title())
    expect(page).to_have_title("Google") 
 