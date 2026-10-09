import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_multiple_products(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    await async_page.wait_for_load_state("domcontentloaded")
    await async_page.locator("//ul[@class='top-menu']//a[normalize-space()='Books']").click()
    await async_page.wait_for_load_state("domcontentloaded")
    products = async_page.locator("xpath=//div[contains(@class,'product-item')]")
    await expect(products.first).to_be_visible()
    product_count = await products.count()
    print(f"\nTotal products displayed: {product_count}\n")
    product_names = []
    for i in range(product_count):
        product = products.nth(i)
        name = (await product.locator("xpath=.//h2[@class='product-title']//a").inner_text()).strip()
        product_names.append(name)
        print(f"{i + 1}. Product: {name}")
        add_to_cart = product.locator("xpath=.//input[contains(@value,'Add to cart')]")
        if await add_to_cart.count() > 0:
         print(f"   Add to Cart button: Found")
        else:
         print(f"   Add to Cart button: Not found")