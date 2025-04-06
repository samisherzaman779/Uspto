from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_correspondent_email(driver):
    """
    Dynamically scrapes the 'Correspondent e-mail:' values from the webpage.

    Args:
        driver: Selenium WebDriver instance.

    Returns:
        list: List of extracted email addresses or ['Not Found'] if none are found.
    """
    try:
        # Wait for the row elements to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "row"))
        )

        # Locate all 'row' divs
        elements = driver.find_elements(By.CLASS_NAME, "row")

        # List to store emails
        emails = []

        # Loop through each element to find the key-value pair
        for element in elements:
            # Get all 'key' and 'value' elements inside the row
            keys = element.find_elements(By.CLASS_NAME, "key")
            values = element.find_elements(By.CLASS_NAME, "value")

            # Loop through keys and values
            for key, value in zip(keys, values):
                if "Correspondent e-mail:" in key.text:
                    # Extract email(s) from <a> tags inside the value div
                    email_links = value.find_elements(By.TAG_NAME, "a")
                    emails.extend([email.text.strip() for email in email_links])

        return emails if emails else ["Not Found"]  # Return emails or 'Not Found'

    except Exception as e:
        print(f"❌ Error scraping Correspondent e-mail: {e}")
        return ["Not Found"]  # Return 'Not Found' in case of an error
