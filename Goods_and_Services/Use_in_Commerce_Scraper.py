from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_use_in_commerce(driver):
    """
    Dynamically scrapes the 'Use in Commerce:' value from the webpage.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        str: The extracted 'Use in Commerce' date (e.g., 'Jun. 01, 2009') or 'Not Found' if not found.
    """
    try:
        # Wait until at least one 'row' div is visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "row"))
        )
        
        # Locate all 'row' divs
        elements = driver.find_elements(By.CLASS_NAME, "row")

        # Loop through each element to find the key-value pair
        for element in elements:
            # Get all 'key' and 'value' elements inside the row
            keys = element.find_elements(By.CLASS_NAME, "key")
            values = element.find_elements(By.CLASS_NAME, "value")

            # Loop through keys and values
            for key, value in zip(keys, values):
                if "Use in Commerce:" in key.text:
                    return value.text.strip()  # Extract and return Use in Commerce date
        
        return "Not Found"  # Return 'Not Found' if key is not found

    except Exception as e:
        print(f"❌ Error scraping Use in Commerce: {e}")
        return "Not Found"  # Return 'Not Found' in case of an error
