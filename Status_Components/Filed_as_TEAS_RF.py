from selenium.webdriver.common.by import By

def scrape_filed_as_teas(driver):
    try:
        # Find all rows in the 'double table' div
        rows = driver.find_elements(By.CSS_SELECTOR, ".double.table .row")
        teas_rf_value = "N/A"  # Default value
        
        for row in rows:
            key_elements = row.find_elements(By.CLASS_NAME, "key")
            value_elements = row.find_elements(By.CLASS_NAME, "value")
            
            for i in range(len(key_elements)):
                key_text = key_elements[i].text.strip()
                value_text = value_elements[i].text.strip()

                # Check for "Filed as TEAS RF"
                if key_text == "Filed as TEAS RF:":
                    print(f"✅ Filed as TEAS RF: {value_text}")
                    return value_text  # Return "Filed as TEAS RF" value

                # Check for "Filed as TEAS Plus" if "Filed as TEAS RF" is missing
                elif key_text == "Filed as TEAS Plus:":
                    print(f"⚠️ Filed as TEAS RF Not Found, Using TEAS Plus: {value_text}")
                    teas_rf_value = value_text  # Save "Filed as TEAS Plus" value

        print(f"⚠️ Final Value Used: {teas_rf_value}")
        return teas_rf_value  # Return either TEAS Plus value or "N/A"

    except Exception as e:
        print(f"❌ Error scraping Filed as TEAS RF: {e}")
        return "Error"

