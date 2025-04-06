from selenium.webdriver.common.by import By

def scrape_registration_date(driver):
    try:
        # Find all rows in the table
        rows = driver.find_elements(By.CSS_SELECTOR, ".double.table .row")
        registration_date = "Not Found"  # Default value
        
        for row in rows:
            key_elements = row.find_elements(By.CLASS_NAME, "key")
            value_elements = row.find_elements(By.CLASS_NAME, "value")
            
            for i in range(len(key_elements)):
                key_text = key_elements[i].text.strip()
                value_text = value_elements[i].text.strip()

                # Check for "Registration Date"
                if key_text == "Registration Date:":
                    print(f"✅ Registration Date: {value_text}")
                    return value_text  # Return if found

        print(f"⚠️ Final Value Used: {registration_date}")
        return registration_date  # Return either found value or "Not Found"

    except Exception as e:
        print(f"❌ Error scraping Registration Date: {e}")
        return "Error"
