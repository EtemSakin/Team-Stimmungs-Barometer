"""Real Chromium smoke tests for the deployed development HTTP server."""
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:8000"
ARTIFACT_DIR = Path("artifacts")
ARTIFACT_DIR.mkdir(exist_ok=True)


def wait_until_ready():
    for _ in range(45):
        try:
            with urlopen(BASE_URL, timeout=2) as response:
                if response.status == 200:
                    return
        except (URLError, TimeoutError):
            pass
        time.sleep(1)
    raise RuntimeError("Local Django server did not start in time")


def main():
    wait_until_ready()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        pages = []
        try:
            for index in range(5):
                context = browser.new_context(
                    viewport={"width": 1280, "height": 900},
                    locale="de-DE",
                )
                page = context.new_page()
                pages.append(page)
                page.goto(BASE_URL)
                assert page.locator("h1").is_visible(), "Hero is not visible"
                assert page.locator("label.mood-option").count() == 5
                page.locator("label.mood-option").nth(3).click()
                page.get_by_role("button", name="Stimmung absenden").click()
                page.wait_for_url("**/?status=thanks")
                assert page.locator(".already-done").is_visible(), "Voting did not complete"
                if index == 0:
                    page.screenshot(path=str(ARTIFACT_DIR / "after-vote-desktop.png"), full_page=True)
            first = pages[0]
            first.reload()
            assert first.locator("#mood-trend-chart .trend-dot").count() == 1, "Chart did not render the eligible day"
            assert "5" in first.locator(".metrics").inner_text()
            first.set_viewport_size({"width": 375, "height": 812})
            first.reload()
            first.screenshot(path=str(ARTIFACT_DIR / "mobile-dashboard.png"), full_page=True)
            overflow = first.evaluate("document.documentElement.scrollWidth > window.innerWidth")
            assert not overflow, "Horizontal mobile overflow"
            print("BROWSER SMOKE TEST PASSED: voting, privacy threshold, SVG and mobile layout")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
