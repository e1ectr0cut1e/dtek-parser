import json
import os
import re
import sys
from datetime import datetime

from playwright.sync_api import sync_playwright, ViewportSize

SHUTDOWNS_URL = os.getenv("SHUTDOWNS_URL", "https://www.dtek-krem.com.ua/ua/shutdowns")
BROWSERLESS_TOKEN = os.environ["BROWSERLESS_TOKEN"]
USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

def scrape_dtek():
    browserless_url = f"wss://production-sfo.browserless.io/chromium/playwright?token={BROWSERLESS_TOKEN}&stealth=true"
    
    print(f"[{datetime.now()}] Connecting to Browserless.io with stealth mode...", file=sys.stderr)
    
    with sync_playwright() as p:
        browser = p.chromium.connect(browserless_url)
        context = browser.new_context(
            viewport=ViewportSize(width=1920, height=1080),
            user_agent=USER_AGENT
        )
        page = context.new_page()
        
        page.goto(SHUTDOWNS_URL, wait_until="networkidle")

        page.wait_for_function('typeof DisconSchedule !== "undefined" && DisconSchedule.fact')
        page.wait_for_timeout(1000)
        
        html = page.content()
        
        browser.close()
        print(f"[{datetime.now()}] ✓ Page scraped successfully", file=sys.stderr)

    match = re.search(r"DisconSchedule\.fact\s*=\s*(\{.+?})\s*</script>", html, re.DOTALL)

    if not match:
        print("❌ Failed to extract data", file=sys.stderr)
        return

    json_text = match.group(1)
    data = json.loads(json_text)

    json.dump(data, sys.stdout, ensure_ascii=False, indent=2)

    print(f"✓ Data extracted successfully", file=sys.stderr)

if __name__ == "__main__":
    scrape_dtek()
