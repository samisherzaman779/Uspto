from selenium.webdriver.common.by import By

def scrape_notice_of_allowance_date(driver):
    """
    Scrapes the 'Notice of Allowance Date' from the page.
    
    :param driver: Selenium WebDriver instance
    :return: Extracted date as string, or 'Not Found' if not available
    """
    try:
        # Find all div elements with class 'row'
        rows = driver.find_elements(By.CLASS_NAME, "row")

        for row in rows:
            keys = row.find_elements(By.CLASS_NAME, "key")
            values = row.find_elements(By.CLASS_NAME, "value")

            for key, value in zip(keys, values):
                if "Notice of Allowance Date" in key.text:
                    return value.text.strip()

        return "Not Found"  # If the key is not found
    except Exception as e:
        print(f"Error scraping Notice of Allowance Date: {e}")
        return "Not Found"
