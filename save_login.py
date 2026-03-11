from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.tiktok.com/login")

    print("QR kod ile giriş yap")

    # Kullanıcı login olana kadar bekle
    page.wait_for_url("https://www.tiktok.com/*", timeout=120000)

    print("Login başarılı")

    # cookie kaydet
    context.storage_state(path="cookies.json")

    print("cookies.json kaydedildi")

    browser.close()