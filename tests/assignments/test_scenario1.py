import pytest
from playwright.async_api import expect

@pytest.mark.asyncio

async def test_demo(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    await async_page.get_by_role("link", name ="Books").nth(0).click()
    product_name = "Computing and Internet"
    product = async_page.locator(f"//div[contains(@class,'details')]"f"[.//a[normalize-space()='{product_name}']]")
    await expect(product).to_be_visible()

    await product.locator(f"xpath=.//a[normalize-space()='{product_name}']").click()
   
    add_to_cart = async_page.locator(f"//div[@class='product-essential']"f"//input[@value='Add to cart']")
    await expect(add_to_cart).to_be_visible()
    await add_to_cart.click()

    print(f"'{product_name}' added to the cart")
    