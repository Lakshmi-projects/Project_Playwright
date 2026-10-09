import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_product_price(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    await async_page.wait_for_load_state("domcontentloaded")
    await async_page.locator("//ul[@class='top-menu']//a[normalize-space()='Books']").click()
    await async_page.wait_for_load_state("domcontentloaded")
    product_name = "Computing and Internet"
    product = async_page.locator(f"//div[contains(@class,'product-item')]"f"[.//h2/a[normalize-space()='{product_name}']]")
    name = await product.locator("xpath=.//h2/a").inner_text()
    print("Product Name:", name)
    rating = await product.locator("xpath=.//div[@class='rating']//div").get_attribute("style")
    print("Rating:",rating)
    await async_page.wait_for_timeout(5000)