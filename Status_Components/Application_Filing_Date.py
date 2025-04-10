from selenium.webdriver.common.by import By

def scrape_application_filing_date(driver):
    """
    Scrapes the Application Filing Date from the webpage.
    
    :param driver: Selenium WebDriver instance
    :return: Scraped Application Filing Date (or 'Not Found' if missing)
    """
    try:
        # Find all rows inside 'double table'
        rows = driver.find_elements(By.CSS_SELECTOR, ".double.table .row")

        for row in rows:
            # Get all 'key' and 'value' elements inside this row
            keys = row.find_elements(By.CLASS_NAME, "key")
            values = row.find_elements(By.CLASS_NAME, "value")

            # Loop through keys to find "Application Filing Date:"
            for i, key in enumerate(keys):
                if key.text.strip() == "Application Filing Date:":
                    filing_date = values[i].text.strip()  # Get corresponding value
                    print(f"✅ Scraped Application Filing Date: {filing_date}")  # Print it
                    return filing_date

        print("❌ Application Filing Date Not Found")
        return "Not Found"

    except Exception as e:
        print(f"❌ Error: {e}")
        return "Error"
        