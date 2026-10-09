import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_parabank_registration(async_page):
 await async_page.goto("https://parabank.parasoft.com/parabank/index.htm")
 await async_page.wait_for_load_state("domcontentloaded")
 await async_page.get_by_role("link", name="Register", exact=True).click()
 await async_page.locator('input[id="customer.firstName"]').fill("ROY")
 await async_page.locator('input[id="customer.lastName"]').fill("David")
 await async_page.locator('input[id="customer.address.street"]').fill("Edapally")
 await async_page.locator('input[id="customer.address.city"]').fill("Cochin")
 await async_page.locator('input[id="customer.address.state"]').fill("Kerala")
 await async_page.locator('input[id="customer.address.zipCode"]').fill("123456")
 await async_page.locator('input[id="customer.phoneNumber"]').fill("1234567890")
 await async_page.locator('input[id="customer.ssn"]').fill("123456789")
 await async_page.locator('input[id="customer.username"]').fill("Roy3")
 await async_page.locator('input[id="customer.password"]').fill("123456789")
 await async_page.locator("#repeatedPassword").fill("123456789")
 await async_page.locator("//input[@value='Register']").click()
 await async_page.wait_for_timeout(5000)
 await async_page.get_by_role("link", name="Accounts Overview", exact=True).click()
 await async_page.wait_for_timeout(5000)
 await async_page.get_by_role("link", name="Log Out", exact=True).click()
 print("Registration and account verification verified successfully.")
 