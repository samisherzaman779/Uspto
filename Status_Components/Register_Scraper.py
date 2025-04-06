from selenium.webdriver.common.by import By

def scrape_register(driver):
    try:
        # Find all rows inside the div with class 'single table'
        rows = driver.find_elements(By.CSS_SELECTOR, "div.single.table div.row")
        
        for row in rows:
            key_element = row.find_element(By.CSS_SELECTOR, "div.key")
            value_element = row.find_element(By.CSS_SELECTOR, "div.value.single")

            # Check if the key text is "Register:"
            if key_element.text.strip() == "Register:":
                register_value = value_element.text.strip()
                print(f"✅ Scraped Register Value: {register_value}")  # Print the scraped value
                return register_value  # Return the value

    except Exception as e:
        print(f"❌ Error in scrape_register: {e}")

    print("❌ Register value not found!")
    return None  # Return None if not found
