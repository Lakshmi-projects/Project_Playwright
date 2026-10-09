import pytest
from playwright.async_api import expect


import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_amazon_product(async_page):
    await async_page.goto("https://www.amazon.com/")

    search = async_page.locator("#twotabsearchtextbox")
    await search.fill("iPhone 16")
    await search.press("Enter")
    titles = async_page.locator("[data-component-type='s-search-result'] h2")
    await expect(titles.first).to_be_visible(timeout=30000)
    product = async_page.locator("[data-component-type='s-search-result']").first
    print("Product:", await product.locator("h2").last.inner_text())
    image = product.locator("img").first
    print("Image URL:", await image.get_attribute("src"))
    price = product.locator(".a-price .a-offscreen").first
    if await price.count() > 0:
        print("Price:", await price.inner_text())
    else:
        print("Price not available")