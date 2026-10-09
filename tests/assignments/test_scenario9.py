import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_product_details(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    await async_page.wait_for_load_state("domcontentloaded")
    search_box =async_page.locator("//input[@id='small-searchterms']")
    await search_box.fill("computer")                             
    await async_page.locator("//input[@value='Search']").click()
    search_product = async_page.locator("//div[contains(@class,'product-item')]//a[@title='Show details for Simple Computer']")
    await expect(search_product).to_be_visible()
    await search_product.click()
    product_name = async_page.locator("//div[@class='product-name']")
    await expect(product_name).to_contain_text("Simple Computer")
    product_price = async_page.locator("//div[@class='prices']//span[@class='price-value-75']")
    await expect(product_price).to_be_visible()
    print("Product price:", await product_price.inner_text())
    add_to_cart = async_page.locator("//input[@id='add-to-cart-button-75']")
    await expect(add_to_cart).to_be_visible()
    await add_to_cart.click()
    print("Simple Computer Added To Cart")
