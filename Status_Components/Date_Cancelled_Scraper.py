from selenium.common.exceptions import NoSuchElementException

def scrape_date_cancelled(driver):
    """
    Scrapes the Date Cancelled from the webpage.

    :param driver: Selenium WebDriver instance
    :return: The cancelled date as a string or "Not Found" if not available
    """
    try:
        # Locate the row that contains "Date Cancelled:"
        row = driver.find_element("xpath", "//div[@class='row'][div[@class='key'][text()='Date Cancelled:']]")
        
        # Find all value elements inside the row
        value_elements = row.find_elements("xpath", ".//div[@class='value']")
        
        for value_element in value_elements:
            cancelled_date = value_element.text.strip()
            if cancelled_date:  # Ensure it's not empty
                print(f"📌 Date Cancelled: {cancelled_date}")  # ✅ Print extracted date
                return cancelled_date

        print("⚠️ Date Cancelled: Not Found")  # ✅ Print when not found
        return "Not Found"

    except NoSuchElementException:
        print("⚠️ Date Cancelled: Not Found (Row Not Found)")  # ✅ Print error case
        return "Not Found"
