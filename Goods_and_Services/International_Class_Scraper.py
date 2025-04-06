from selenium.webdriver.common.by import By

def scrape_international_class(driver):
    """
    Scrapes the 'International Class(es):' value from the USPTO website.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        str: The extracted international class (e.g., '025 - Primary Class') or 'Not Found' if not found.
    """
    try:
        # Locate all the rows
        elements = driver.find_elements(By.XPATH, "//div[@class='row']")
        
        # Loop through each element to find the key-value pair
        for element in elements:
            keys = element.find_elements(By.CLASS_NAME, "key")
            values = element.find_elements(By.CLASS_NAME, "value")
            
            # Loop through keys and corresponding values
            for key, value in zip(keys, values):
                if "International Class(es):" in key.text:
                    return value.text.strip()  # Return the found international class text
        
        return "Not Found"  # Return 'Not Found' if the key is not found

    except Exception as e:
        print(f"❌ Error scraping International Class(es): {e}")
        return "Not Found"  # Return 'Not Found' in case of an error
