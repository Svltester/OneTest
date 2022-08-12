from playwright.sync_api import Playwright, sync_playwright, expect

def test_am():

    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(ignore_https_errors=True)

        # Open new page
        page = context.new_page()
        page.goto("https://ia-test.egisz.rosminzdrav.ru/webadmin")
        # Click text=Вход >> nth=0
        assert page.locator("text=Вход >> nth=0").is_visible(
        
        # ---------------------
        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)
