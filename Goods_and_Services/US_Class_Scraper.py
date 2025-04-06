from selenium.webdriver.common.by import By

def scrape_us_classes(driver):
    """
    Scrapes the 'U.S Class(es):' values from the page.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        str: The extracted U.S. classes (e.g., '022, 039') or 'Not Found' if not found.
    """
    try:
        # Locate all the rows containing key-value pairs
        elements = driver.find_elements(By.XPATH, "//div[@class='row']")
        
        # Loop through each element to find the key-value pair
        for element in elements:
            keys = element.find_elements(By.CLASS_NAME, "key")
            values = element.find_elements(By.CLASS_NAME, "value")
            
            # Loop through the keys and corresponding values
            for key, value in zip(keys, values):
                if "U.S Class(es):" in key.text:
                    # Clean and return the value (remove extra spaces)
                    return value.text.strip()
        
        return "Not Found"  # Return 'Not Found' if the key is not found

    except Exception as e:
        print(f"❌ Error scraping U.S Class(es): {e}")
        return "Not Found"  # Return 'Not Found' in case of an error
