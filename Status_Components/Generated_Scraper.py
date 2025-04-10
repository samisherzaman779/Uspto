from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc # type: ignore
import time

def scrape_generated_text(driver, url):
    """
    Scrapes the generated text from the specified page using an existing WebDriver instance.

    Args:
        driver (webdriver): Selenium WebDriver instance.
        url (str): The URL of the page to scrape.

    Returns:
        str: The extracted text or None if not found.
    """
    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Locate the div with class "value single"
        element = driver.find_element(By.CSS_SELECTOR, "div.value.single")
        extracted_text = element.text.strip()

        return extracted_text

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None