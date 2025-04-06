from selenium.common.exceptions import NoSuchElementException

def scrape_date_abandoned(driver):
    """
    Scrapes the Date Abandoned from the webpage.

    :param driver: Selenium WebDriver instance
    :return: The abandoned date as a string or "Not Found" if not available
    """
    try:
        # Locate the row that contains "Date Abandoned:"
        row = driver.find_element("xpath", "//div[@class='row'][div[@class='key'][text()='Date Abandoned:']]")
        
        # Find the first non-empty value inside the row
        value_elements = row.find_elements("xpath", ".//div[@class='value']")
        
        for value_element in value_elements:
            abandoned_date = value_element.text.strip()
            if abandoned_date:  # Ensure it's not empty
                print(f"📌 Date Abandoned: {abandoned_date}")  # ✅ Print extracted date
                return abandoned_date

        print("⚠️ Date Abandoned: Not Found")  # ✅ Print when not found
        return "Not Found"

    except NoSuchElementException:
        print("⚠️ Date Abandoned: Not Found (Row Not Found)")  # ✅ Print error case
        return "Not Found"
