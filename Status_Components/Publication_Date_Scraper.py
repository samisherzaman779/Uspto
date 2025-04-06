from selenium.webdriver.common.by import By

def scrape_publication_date(driver):
    try:
        # Locate the row containing "Publication Date:"
        publication_row = driver.find_element(By.XPATH, "//div[contains(@class, 'row') and div[contains(@class, 'key') and contains(text(), 'Publication Date:')]]")

        # Extract the key
        key_element = publication_row.find_element(By.XPATH, "./div[contains(@class, 'key')]")
        key = key_element.text.strip() if key_element.text.strip() else "Publication Date"

        # Extract the value
        value_element = publication_row.find_element(By.XPATH, "./div[contains(@class, 'value')]")
        value = value_element.text.strip() if value_element.text.strip() else "Not Found"

        # Print extracted key-value pair
        print(f"📌 {key}: {value}")

        return value
    
    except Exception:
        print("⚠️ Publication Date: Not Found")
        return "Not Found"
