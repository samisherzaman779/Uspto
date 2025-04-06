from selenium.common.exceptions import NoSuchElementException  # Import this for NoSuchElementException
from selenium.webdriver.common.by import By  # Import this for By class
import time

def scrape_for_item(driver):
    """
    Scrapes the item name (e.g., 'T-shirts') under the 'For:' label from the webpage.

    :param driver: Selenium WebDriver instance
    :return: The item name (e.g., 'T-shirts') or "Not Found" if not available
    """
    try:
        # Directly scrape the data without clicks
        item_name = scrape_item_name(driver)
        print(f"📌 Item Name: {item_name}")

        # Return the result from the scrape
        if item_name != "Not Found":
            return item_name

        print("⚠️ Item Name Not Found")
        return "Not Found"

    except NoSuchElementException as e:
        print(f"⚠️ Error occurred: {str(e)}")
        return "Not Found"

def scrape_item_name(driver):
    """
    Helper function to scrape the item name from the 'For:' label on the page.

    :param driver: Selenium WebDriver instance
    :return: Item name or "Not Found"
    """
    try:
        # Locate the row that contains "For:"
        row = driver.find_element(By.XPATH, "//div[@class='row'][div[@class='key'][text()='For:']]")
        
        # Find the value element inside the row that contains the item name (e.g., 'T-shirts')
        value_element = row.find_element(By.XPATH, ".//div[@class='value']")
        
        item_name = value_element.text.strip()
        if item_name:  # Ensure it's not empty
            return item_name

        return "Not Found"

    except NoSuchElementException:
        return "Not Found"
