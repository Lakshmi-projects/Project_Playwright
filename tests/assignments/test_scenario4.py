import pytest
from playwright.async_api import expect
@pytest.mark.asyncio 

async def test_amazon_product(async_page):
    await async_page.goto("https://www.amazon.com/")
    await async_page.wait_for_load_state("domcontentloaded")
    search_box = async_page.locator("//input[@id='twotabsearchtextbox']")
    await search_box.fill("Mobiles")
    search_button = async_page.locator ("xpath=//input[@id='nav-search-submit-button']")
    await search_button.click()
    await async_page.wait_for_load_state("domcontentloaded")
    product_name = "Samsung Galaxy S26 Ultra, Unlocked Android Smartphone, 512GB, Black"
    product = async_page.locator("//div[@data-component-type='s-search-result']").filter(has_text=product_name)
    name = await product.locator("xpath=.//h2//span").inner_text()
    price = await product.locator("xpath=.//span[contains(@class,'a-price')]//span[@class='a-offscreen']").first.inner_text()
    print("Product Name:", name)
    print("Price:", price)
    # product = async_page.locator("//div[contains(@class, 'a-section a-spacing-none a-text-center')]/..""//span[text()='Samsung Galaxy S26 Ultra, Unlocked Android Smartphone, 512GB, Black']")