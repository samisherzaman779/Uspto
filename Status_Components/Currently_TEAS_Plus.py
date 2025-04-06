from selenium.webdriver.common.by import By

def scrape_currently_teas_status(driver):
    try:
        # Find all rows in the table
        rows = driver.find_elements(By.CSS_SELECTOR, ".double.table .row")
        teas_status = "Not Found"  # Default value
        
        for row in rows:
            key_elements = row.find_elements(By.CLASS_NAME, "key")
            value_elements = row.find_elements(By.CLASS_NAME, "value")
            
            for i in range(len(key_elements)):
                key_text = key_elements[i].text.strip()
                value_text = value_elements[i].text.strip()

                # Check for "Currently TEAS Plus" or "Currently TEAS RF"
                if key_text in ["Currently TEAS Plus:", "Currently TEAS RF:"]:
                    print(f"✅ Found: {key_text} {value_text}")
                    return value_text  # Return if found

        print(f"⚠️ Final Value Used: {teas_status}")
        return teas_status  # Return either found value or "Not Found"

    except Exception as e:
        print(f"❌ Error scraping TEAS Status: {e}")
        return "Error"
