from selenium.webdriver.common.by import By

def scrape_us_serial_number(driver):
    """
    Scrapes the US Serial Number from the webpage.
    
    :param driver: Selenium WebDriver instance
    :return: Scraped US Serial Number (or 'Not Found' if missing)
    """
    try:
        # Find all elements with class 'row' inside 'double table'
        rows = driver.find_elements(By.CSS_SELECTOR, ".double.table .row")

        for row in rows:
            # Find all 'key' elements inside this row
            keys = row.find_elements(By.CLASS_NAME, "key")
            values = row.find_elements(By.CLASS_NAME, "value")

            # Check if 'US Serial Number:' is in keys
            for i, key in enumerate(keys):
                if key.text.strip() == "US Serial Number:":
                    serial_number = values[i].text.strip()  # Get corresponding value
                    print(f"✅ Scraped US Serial Number: {serial_number}")  # Print it
                    return serial_number

        print("❌ US Serial Number Not Found")
        return "Not Found"

    except Exception as e:
        print(f"❌ Error: {e}")
        return "Error"
