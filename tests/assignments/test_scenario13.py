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
 await async_page.get_by_role("link", name="Accounts Overview", exact=True).click()
 account_links = async_page.locator("//table[@id='accountTable']//tbody/tr/td/a")
 await expect(account_links.nth(1)).to_be_visible(timeout=15000)
 from_account = (await account_links.nth(0).inner_text()).strip()
 to_account = (await account_links.nth(1).inner_text()).strip()
 print("From Account:", from_account)
 print("To Account:", to_account)
 
 await async_page.get_by_role("link", name="Transfer Funds", exact=True).click()
 await async_page.locator("//input[@id='amount']").fill("1.00")
 await async_page.locator("//select[@id='fromAccountId']").select_option(label=from_account)
 await async_page.locator("//select[@id='toAccountId']").select_option(label=to_account)
 await async_page.locator("//input[@value='Transfer']").click()
 await expect(async_page.get_by_text("Transfer Complete!")).to_be_visible(timeout=15000)
 print("Transfer completed successfully")
 
 await async_page.get_by_role("link", name="Accounts Overview", exact=True).click()
 await async_page.locator("//table[@id='accountTable']//tbody/tr/td/a").filter(has_text=from_account).click()
 await expect(async_page.locator("//table[@id='transactionTable']")).to_be_visible(timeout=15000)
 print("Transaction history displayed.")
 await async_page.wait_for_timeout(5000)
 