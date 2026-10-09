import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_parabank_registration(async_page):
 await async_page.goto("https://parabank.parasoft.com/parabank/index.htm")
 await async_page.wait_for_load_state("domcontentloaded")
 username = "testlak"
 password = "12345"
 await async_page.locator('input[name="username"]').fill(username)
 await async_page.locator('input[name="password"]').fill(password)
 await async_page.locator("//input[@value='Log In']").click()
 await async_page.wait_for_timeout(5000)
 await async_page.get_by_role("link", name="Open New Account").click()
 account_type = async_page.locator("#type")
 await account_type.select_option(label = "SAVINGS")
 await async_page.get_by_role("link", name="Open New Account").click()
 existing_account = async_page.locator("#fromAccountId")
 await existing_account.select_option(label = "24555")
 await async_page.get_by_role("button", name="Open New Account").click()
 await expect(async_page.get_by_text("Congratulations, your account is now open.",)).to_be_visible(timeout=15000)
 new_account_number = async_page.locator("#newAccountId")  
 await expect(new_account_number).to_be_visible()
 account_number = (await new_account_number.inner_text()).strip()
 print("New account number:", account_number)
 
 await async_page.get_by_role("link", name="Accounts Overview").click()
 await expect(async_page.locator("#accountTable")).to_contain_text(account_number, timeout=15000)
 print("New account verified in Accounts Overview.")
 await async_page.wait_for_timeout(5000)
 