from playwright.sync_api import Playwright, sync_playwright, expect

def test_am():

    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        page.goto("https://ia-test.egisz.rosminzdrav.ru/webadmin")

        # Click text=Вход >> nth=0
        page.locator("text=Вход").first.click()

        # Click text=Вход через ЕСИА (тестовая)
        page.locator("text=Вход через ЕСИА (тестовая)").click()
        page.wait_for_url("https://esia-portal1.test.gosuslugi.ru/login/")
        # Click text=Главная >> nth=1
        assert page.locator("text=Единая система<br/> идентификации и аутентификации").is_visible()
        # Click text=Единая система<br/> идентификации и аутентификации
        page.locator("text=Единая система<br/> идентификации и аутентификации").click()


        # ---------------------
        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)
