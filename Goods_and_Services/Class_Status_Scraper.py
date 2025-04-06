from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_class_status(driver):
    """
    Dynamically scrapes the 'Class Status:' value from the webpage.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        str: The extracted class status (e.g., 'SECTION 8 - CANCELLED') or 'Not Found' if not found.
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
            try:
                # Wait for key and value elements inside each row
                key_element = WebDriverWait(element, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "key"))
                )
                value_element = WebDriverWait(element, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "value"))
                )

                # Check if key text matches 'Class Status:'
                if "Class Status:" in key_element.text:
                    return value_element.text.strip()  # Extract and return class status
            except:
                continue  # Skip if elements are not found in this row

        return "Not Found"  # Return 'Not Found' if key not found

    except Exception as e:
        print(f"❌ Error scraping Class Status: {e}")
        return "Not Found"  # Return 'Not Found' in case of an error
