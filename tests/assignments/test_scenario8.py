import pytest
from playwright.async_api import expect
@pytest.mark.asyncio 

async def test_amazon_navigation_menu(async_page):
    await async_page.goto("https://www.amazon.com/")
    await async_page.wait_for_load_state("domcontentloaded")
    menu_button = async_page.locator("//div[@class='nav-left']//a[@id='nav-hamburger-menu']")
    await expect(menu_button).to_be_visible()
    await menu_button.click()
    menu = async_page.get_by_role("dialog").locator("#hmenu-content")
    await expect(menu).to_be_visible()
    heading_name = "Programs & Features"
    heading = menu.locator(f"xpath=.//div[normalize-space()='{heading_name}']")
    await heading.click()
    sub_category = menu.locator("xpath=.//div[normalize-space()='Programs & Features']/..//a[contains(@class,'hmenu-item')]")
    #sub_category = menu.locator("xpath=.//a[contains(@class,'hmenu-item')]")
    #sub_category = menu.locator("xpath=.//div[@class='hmenu-item hmenu-title' ""and normalize-space()='Programs & Features']""/following-sibling::a[contains(@class,'hmenu-item')]")
    print(f"\nSubcategories under {heading_name}:")
    names = await sub_category.all_inner_texts()
    print(names)
    #select_category = sub_category.locator("xpath=.//a[contains(@class,'hmenu-item')""and normalize-space()='Gift Cards']")
    select_category= menu.locator("xpath=.//a[contains(@class,'hmenu-item') and .//div[normalize-space()='Gift Cards']]")
    await expect(select_category).to_be_visible()
    await select_category.click()