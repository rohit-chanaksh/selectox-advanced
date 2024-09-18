from selectolax.parser import HTMLParser
from playwright.sync_api import sync_playwright


def getHtml(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state('networkidle')
        htmlData = page.inner_html('body')
        
        pageData = HTMLParser(htmlData)

        return pageData
         