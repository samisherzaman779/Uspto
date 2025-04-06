from selenium.webdriver.common.by import By

def scrape_date_amended_to_current_register(driver):
    """
    Scrapes the 'Date Amended to Current Register' value from the USPTO website.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        str: The extracted date (e.g., 'Sep. 03, 2009') or 'N/A' if not found.
    """
    try:
        elements = driver.find_elements(By.XPATH, "//div[@class='row']")
        for element in elements:
            keys = element.find_elements(By.CLASS_NAME, "key")
            values = element.find_elements(By.CLASS_NAME, "value")
            
            for key, value in zip(keys, values):
                if "Date Amended to Current Register" in key.text:
                    return value.text.strip()

        return "N/A"  # Return 'N/A' if not found

    except Exception as e:
        print(f"❌ Error scraping Date Amended to Current Register: {e}")
        return "N/A"
