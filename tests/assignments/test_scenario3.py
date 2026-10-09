import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_product_price(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    await async_page.locator("//ul[@class='top-menu']//a[normalize-space(@href)='/digital-downloads']").click()
    price = "10.00"
    product_price = async_page.locator("//div[contains(@class,'item-box')][.//span[contains(@class,'price') and normalize-space()='10.00']]")
    product_name = await product_price.locator("xpath=.//h2[contains(@class,'product-title')]/a").inner_text()
    await product_price.locator("xpath=.//div[contains(@class,'buttons')]//input[@value='Add to cart']").click()
    cart = async_page.locator("//span[contains(@class,'cart-qty')]")
    await cart.wait_for()
    print(f"Product: {product_name} Price: {price} added to cart successfully.")
    await async_page.wait_for_timeout(5000)