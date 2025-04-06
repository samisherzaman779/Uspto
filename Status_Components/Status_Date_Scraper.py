from selenium.webdriver.common.by import By

def scrape_status_date(driver):
    """
    Dynamically scrapes the 'Status Date' value by identifying the key-value structure.

    :param driver: Selenium WebDriver instance
    :return: Extracted Status Date (e.g., "Jul. 19, 2019") or "Not Found" if unavailable.
    """
    try:
        # Find all rows containing key-value pairs
        rows = driver.find_elements(By.XPATH, "//div[@class='row']")
        
        for row in rows:
            try:
                # Locate the key element
                key_element = row.find_element(By.CLASS_NAME, "key")
                key_text = key_element.text.strip()

                # Check if the key is "Status Date:"
                if "Status Date:" in key_text:
                    # Locate the corresponding value element
                    value_element = row.find_element(By.CLASS_NAME, "value")
                    status_date = value_element.text.strip()
                    
                    print(f"✅ Scraped Status Date: {status_date}")
                    return status_date

            except Exception as inner_exception:
                continue  # If the current row doesn't match, move to the next one

    except Exception as e:
        print("❌ Status Date not found.")
    
    return "Not Found"
