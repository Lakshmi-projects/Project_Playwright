import pytest
from playwright.async_api import expect
@pytest.mark.asyncio 

async def test_amazon_headings(async_page):
    await async_page.goto("https://www.amazon.com/")
    await async_page.wait_for_load_state("domcontentloaded")
    menu_button = async_page.locator("//div[@class='nav-left']//a[@id='nav-hamburger-menu']")
    await expect(menu_button).to_be_visible()
    
    await menu_button.click()
    await expect(menu_button).to_have_attribute("aria-expanded", "true")
    headings = async_page.locator("xpath=.//div[contains(@class,'hmenu-title')]")
    count = await headings.count()
    for i in range(count):
        heading = (await headings.nth(i).inner_text()).strip()
        if heading:
         print(heading)
    
    