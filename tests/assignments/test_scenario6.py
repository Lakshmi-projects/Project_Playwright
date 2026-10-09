import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_amazon_product(async_page):
 await async_page.goto("https://www.amazon.com/",wait_until="domcontentloaded")
 search_box = async_page.locator("#twotabsearchtextbox")
 await expect(search_box).to_be_visible(timeout=15000)
 await search_box.fill("The Hobbit")
 await async_page.locator("#nav-search-submit-button").click()
 results = async_page.locator("[data-component-type='s-search-result']")
 await expect(results.first).to_be_visible(timeout=20000)

 product = results.filter(has=async_page.locator("h2")).filter(has_text="The Hobbit").first
 await expect(product).to_be_visible(timeout=15000)
 title = product.locator("h2").first
 book_title = (await title.inner_text()).strip()
 print("Book title:", book_title)

 price = product.locator(".a-price .a-offscreen").first
 if await price.count() > 0:
        print("Book price:", (await price.inner_text()).strip())
 else:
        print("Book price is not displayed.")

 product_link = product.locator("a:has(h2)").first
 await expect(product_link).to_be_visible(timeout=10000)
 await product_link.click()
 add_to_cart = async_page.get_by_role("button", name="Add to Cart").first

 await expect(add_to_cart).to_be_visible(timeout=15000)
 await add_to_cart.click()

 print("Add to Cart clicked successfully.")