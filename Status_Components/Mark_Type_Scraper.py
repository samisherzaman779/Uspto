from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_mark_type(driver):
    """
    Scrapes the 'Mark Type' value dynamically from the webpage.

    :param driver: Selenium WebDriver instance
    :return: Scraped Mark Type value (or 'N/A' if missing)
    """
    try:
        # ✅ Wait for all 'row' elements to be present
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.row"))
        )
        
        for row in rows:
            try:
                # ✅ Locate the 'key' and 'value' elements within each row
                key_element = row.find_element(By.CSS_SELECTOR, "div.key")
                value_element = row.find_element(By.CSS_SELECTOR, "div.value.single")

                # ✅ Check if the key text is "Mark Type:"
                if key_element.text.strip() == "Mark Type:":
                    mark_type_value = value_element.text.strip()
                    print(f"✅ Scraped Mark Type Value: {mark_type_value}")  # Print the scraped value
                    return mark_type_value  # Return the value

            except Exception:
                continue  # If an element is missing in a row, continue to the next row

    except Exception as e:
        print(f"❌ Error in scrape_mark_type: {e}")

    print("❌ Mark Type value not found!")
    return "N/A"  # ✅ Return 'N/A' if not found
