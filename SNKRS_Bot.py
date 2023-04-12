import time
import asyncio
from pyppeteer import launch
from pyppeteer import launcher
from pyppeteer_stealth import stealth


async def main():
    # -------------------MAIN FUNCTION WITH PRE-DEFINED START ARGUMENTS--------------------------------
    argumenty = ["--start-maximized", "--disable-blink-features=AutomationControlled",
    "--disable-infobars", "--disable-dev-shm-usage",
    '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 71.0.3542.0 Safari / 537.36"','--ignore-certifcate-errors',
    '--ignore-certifcate-errors-spki-list', "--lang=en"]
    browser = await launcher.launch(options={"headless": False, "args": argumenty, "ignoreHTTPSErrors": True})
    page = await browser.newPage()
    # -------------------STEALTH PLUGIN------------------------
    await stealth(
        page=page,
        run_on_insecure_origins=False,
        languages=["pl-PL", "pl", "en-US", "en"],
        vendor="Google Inc.",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3542.0 Safari/537.36",
        locale="pl-Pl,pl",
        mask_linux=True,
        webgl_vendor="Google Inc. (NVIDIA)",
        renderer="ANGLE (NVIDIA, NVIDIA GeForce GTX 1060 6GB Direct3D11 vs_5_0 ps_5_0, D3D11)",

    )
    await page.setViewport(viewport={'width': 1920, 'height': 1080})
    await page.goto("https://www.nike.com/pl")

    time.sleep(3)

    # --------------------FINDING ELEMENTS ON A WEBSITE (COOKIE,LOGIN)---------------------------------------------
    await page.waitForXPath('//*[@id="hf_cookie_text_cookieAccept"]',
                            options={"visible": True})

    time.sleep(1)

    await page.click('.mb7-sm > div:nth-child(2) > button:nth-child(1)')

    time.sleep(2)

    await page.click(
        '#gen-nav-commerce-header-v2 > div.pre-l-header-container > div.pre-l-brand-header.d-sm-h.d-lg-b.z3 > div > div > div:nth-child(4) > div > button')
    time.sleep(3)
    await page.waitForXPath('//*[@id="username"]', options={"visible": True})
    await page.click("#username")
    time.sleep(1)

    async def send_keys_delay(keys, delay=1):
        for key in keys:
            await page.focus("#username")
            await page.keyboard.type(key)
            time.sleep(delay)
        time.sleep(2)
        await page.keyboard.press('Enter')

    email = "wt666888000@gmail.com"
    await send_keys_delay(email)
    time.sleep(120)
    await page.screenshot(options={"path": "result.png"})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())