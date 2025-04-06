from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_correspondent_email_authorized(driver):
    """
    Scrapes the 'Correspondent e-mail Authorized:' value from the webpage.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        str: The extracted authorization value or 'Not Found' if not available.
    """
    try:
        # Wait until the table containing data appears
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "row"))
        )

        # Locate all 'row' divs
        elements = driver.find_elements(By.CLASS_NAME, "row")

        # Loop through each row to find the key-value pair
        for element in elements:
            keys = element.find_elements(By.CLASS_NAME, "key")
            values = element.find_elements(By.CLASS_NAME, "value")

            for key, value in zip(keys, values):
                if "Correspondent e-mail Authorized:" in key.text:
                    return value.text.strip()  # Extract the corresponding value

        return "Not Found"  # Return if not found

    except Exception as e:
        print(f"❌ Error scraping Correspondent e-mail Authorized: {e}")
        return "Not Found"  # Return 'Not Found' in case of an error
