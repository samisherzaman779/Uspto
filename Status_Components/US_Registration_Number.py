from selenium.webdriver.common.by import By

def scrape_us_registration_number(driver):
    try:
        # Find all rows in the 'double table' div
        rows = driver.find_elements(By.CSS_SELECTOR, ".double.table .row")
        registration_number = "Not Found"  # Default value
        
        for row in rows:
            key_elements = row.find_elements(By.CLASS_NAME, "key")
            value_elements = row.find_elements(By.CLASS_NAME, "value")
            
            for i in range(len(key_elements)):
                key_text = key_elements[i].text.strip()
                value_text = value_elements[i].text.strip()

                # Check for "US Registration Number"
                if key_text == "US Registration Number:":
                    print(f"✅ US Registration Number: {value_text}")
                    return value_text  # Return if found

        print(f"⚠️ Final Value Used: {registration_number}")
        return registration_number  # Return either found value or "Not Found"

    except Exception as e:
        print(f"❌ Error scraping US Registration Number: {e}")
        return "Error"
