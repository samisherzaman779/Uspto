from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_tm5_common_status_descriptor(driver):
    """
    Scrapes the correct TM5 Common Status Descriptor from multiple div.value elements.

    :param driver: Selenium WebDriver instance
    :return: Scraped TM5 Common Status Descriptor text (or 'N/A' if missing)
    """
    try:
        # ✅ Find ALL div.value elements
        value_divs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.value"))
        )

        # ✅ Loop through all divs to find the correct one
        for div in value_divs:
            paragraphs = div.find_elements(By.TAG_NAME, "p")  # Find all <p> tags inside div

            # ✅ Check if <p> tags are present
            if paragraphs:
                status_text = " ".join(p.text.strip() for p in paragraphs if p.text.strip())

                if status_text:
                    print(f"✅ Scraped TM5 Common Status Descriptor:\n{status_text}")
                    return status_text  # Return first valid text found

        print("⚠️ No relevant TM5 Common Status Descriptor found.")
        return "N/A"

    except Exception as e:
        print(f"❌ Error in scrape_tm5_common_status_descriptor: {e}")
        return "N/A"
