# # Import necessary modules
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# import undetected_chromedriver as uc
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException

# # Status_Components
# from Status_Components.Generated_Scraper import scrape_generated_text
# from Status_Components.Mark_Scraper import scrape_mark_text
# from Status_Components.US_Serial_Number import scrape_us_serial_number
# from Status_Components.Application_Filing_Date import scrape_application_filing_date
# from Status_Components.US_Registration_Number import scrape_us_registration_number
# from Status_Components.Registration_Date import scrape_registration_date
# from Status_Components.Filed_as_TEAS_RF import scrape_filed_as_teas
# from Status_Components.Currently_TEAS_Plus import scrape_currently_teas_status
# from Status_Components.Register_Scraper import scrape_register
# from Status_Components.Mark_Type_Scraper import scrape_mark_type
# from Status_Components.TM5_Common_Status_Descriptor import scrape_tm5_common_status_descriptor
# from Status_Components.Status_Scraper import scrape_status_text
# from Status_Components.Status_Date_Scraper import scrape_status_date
# from Status_Components.Publication_Date_Scraper import scrape_publication_date
# from Status_Components.Notice_of_Allowance_Date_Scraper import scrape_notice_of_allowance_date
# from Status_Components.Date_Abandoned_Scraper import scrape_date_abandoned
# from Status_Components.Date_Cancelled_Scraper import scrape_date_cancelled
# from Status_Components.Amended_to_Principal_Register import scrape_amended_to_principal_register
# from Status_Components.Date_Amended_to_Current_Register_Scraper import scrape_date_amended_to_current_register

# # Goods_and_Services
# from Goods_and_Services.For_Scraper import scrape_for_item  # ✅ New Import
# from Goods_and_Services.International_Class_Scraper import scrape_international_class
# from Goods_and_Services.US_Class_Scraper import scrape_us_classes
# from Goods_and_Services.Class_Status_Scraper import scrape_class_status
# from Goods_and_Services.First_Use_Scraper import scrape_first_use
# from Goods_and_Services.Use_in_Commerce_Scraper import scrape_use_in_commerce
 
# # Attorney_Correspondence_Information
# from Attorney_Correspondence_Information.Correspondent_Name_Address_Scraper import scrape_correspondent_address
# from Attorney_Correspondence_Information.Phone_Scraper import scrape_phone_number
# from Attorney_Correspondence_Information.Fax_Scraper import scrape_fax_number
# from Attorney_Correspondence_Information.Correspondent_e_mail_Scraper import scrape_correspondent_email
# from Attorney_Correspondence_Information.Correspondent_e_mail_Authorized_Scraper import scrape_correspondent_email_authorized

# # Google Sheets Authentication
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name(
#     "G:\\My_Projects\\Uspto\\web-sracping-fc26a07ab6b1.json", scope
# )
# client = gspread.authorize(creds)

# # Open the target Google Sheet
# sheet = client.open("Uspto").sheet1
# print("✅ Google Sheets connected successfully.")

# # **Column Headers**
# column_headers = [
#     "URL", "Scraped Text", "Mark Text", "US Serial Number", "Application Filing Date", 
#     "US Registration Number", "Registration Date", "Filed as TEAS RF", "Currently TEAS Status", 
#     "Register Value", "Mark Type", "TM5 Status", "Amended to Principal Register", 
#     "Date Amended to Current Register", "Status Text", "Status Date", "Publication Date",
#     "Notice of Allowance Date",  # ✅ Added Header After "Publication Date"
#     "Date Abandoned", "Date Cancelled", "For", "International Class(es)", "U.S Class(es)", 
#     "Class Status", "First Use", "Use in Commerce", "Correspondent Name/Address", "Phone Number", 
#     "Fax Number", "Correspondent Email", "Correspondent Email Authorized"
# ]

# # Check if headers exist, if not, add them
# existing_headers = sheet.row_values(1)
# if not existing_headers or existing_headers != column_headers:
#     sheet.insert_row(column_headers, 1)
#     print("📌 Column headers added successfully.")

# # **Read URLs from the text file**
# file_path = "G:\\My_Projects\\Uspto\\scraped_urls.txt"
# with open(file_path, "r") as file:
#     urls = [url.strip() for url in file.readlines() if url.strip()]  # Reading the URLs

# # Initialize undetected Chrome
# driver = uc.Chrome(version_main=133)

# # **Scrape and Save Data**
# for url in urls:
#     driver.get(url)
#     time.sleep(5)  # Wait for the page to load

#     # **Click the necessary elements first**
#     try:
#         # First Click Path
#         first_click_path = "/html/body/div[5]/div[4]/div[6]/div[3]/ul/li[1]/div[2]/div[3]"
#         first_element = driver.find_element(By.XPATH, first_click_path)
#         ActionChains(driver).move_to_element(first_element).click().perform()
#         time.sleep(2)  # Wait for the page content to load after the click

#         # Second Click Path (if necessary)
#         second_click_path = "/html/body/div[5]/div[4]/div[6]/div[3]/ul/li[1]/div[2]/div[6]"
#         second_element = driver.find_element(By.XPATH, second_click_path)
#         ActionChains(driver).move_to_element(second_element).click().perform()
#         time.sleep(2)  # Wait for the page content to load after the second click

#     except NoSuchElementException as e:
#         print(f"⚠️ Error occurred during clicks: {str(e)}")
#         continue  # Skip this URL and move to the next one

#     # Scrape Data after clicking the elements
#     scraped_text = scrape_generated_text(driver, url)
#     mark_text = scrape_mark_text(driver)
#     us_serial_number = scrape_us_serial_number(driver)
#     application_filing_date = scrape_application_filing_date(driver)
#     us_registration_number = scrape_us_registration_number(driver)
#     registration_date = scrape_registration_date(driver)
#     filed_as_teas_rf = scrape_filed_as_teas(driver)
#     currently_teas_status = scrape_currently_teas_status(driver)
#     register_value = scrape_register(driver)
#     mark_type = scrape_mark_type(driver)
#     tm5_status = scrape_tm5_common_status_descriptor(driver)
#     status_text = scrape_status_text(driver)
#     status_date = scrape_status_date(driver)
#     publication_date = scrape_publication_date(driver)
#     notice_of_allowance_date = scrape_notice_of_allowance_date(driver)
#     date_abandoned = scrape_date_abandoned(driver)
#     date_cancelled = scrape_date_cancelled(driver)
#     amended_to_principal_register = scrape_amended_to_principal_register(driver)
#     date_amended_to_current_register = scrape_date_amended_to_current_register(driver)

#     # Scrape Data for "For" Item
#     for_item = scrape_for_item(driver)  # Scrape after clicking the necessary path

#     # Scrape Data for International Classes
#     international_class_info = scrape_international_class(driver)  # Scrape International Class(es)
#     us_class = scrape_us_classes(driver)
#     class_status = scrape_class_status(driver)
#     first_use = scrape_first_use(driver)
#     use_in_commerce = scrape_use_in_commerce(driver)
#     correspondent_name_address = scrape_correspondent_address(driver)
#     phone_number = scrape_phone_number(driver)
#     fax_number = scrape_fax_number(driver)
#     email_address = scrape_correspondent_email(driver)
#     email_authorized = scrape_correspondent_email_authorized(driver)    

#     # Append data to the sheet only if valid data exists
#     if any([scraped_text, mark_text, us_serial_number, application_filing_date, us_registration_number, 
#             registration_date, filed_as_teas_rf, currently_teas_status, register_value, mark_type, 
#             tm5_status, amended_to_principal_register, date_amended_to_current_register, status_text, 
#             status_date, publication_date, notice_of_allowance_date, date_abandoned, date_cancelled, 
#             for_item, international_class_info, us_class, class_status, first_use, use_in_commerce,
#             correspondent_name_address, phone_number, fax_number, 
#             ", ".join(email_address) if isinstance(email_address, list) else email_address, email_authorized
#             ]):  # Ensure International Class data is included
        
#         sheet.append_row([
#             url, scraped_text, mark_text, us_serial_number, application_filing_date, us_registration_number, 
#             registration_date, filed_as_teas_rf, currently_teas_status, register_value, mark_type, 
#             tm5_status, amended_to_principal_register, date_amended_to_current_register, 
#             status_text, status_date, publication_date, notice_of_allowance_date, 
#             date_abandoned, date_cancelled, for_item, international_class_info, us_class, class_status, 
#             first_use, use_in_commerce, correspondent_name_address, phone_number, fax_number, 
#             ", ".join(email_address) if isinstance(email_address, list) else email_address, email_authorized  # ✅ Convert list to string
#             ])


# # Close the browser
# driver.quit()
# print("✅ Scraping completed and browser closed.")



















# # Import necessary modules
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# import undetected_chromedriver as uc
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException

# # Status_Components
# from Status_Components.Generated_Scraper import scrape_generated_text
# from Status_Components.Mark_Scraper import scrape_mark_text
# from Status_Components.US_Serial_Number import scrape_us_serial_number
# from Status_Components.Application_Filing_Date import scrape_application_filing_date
# from Status_Components.US_Registration_Number import scrape_us_registration_number
# from Status_Components.Registration_Date import scrape_registration_date
# from Status_Components.Filed_as_TEAS_RF import scrape_filed_as_teas
# from Status_Components.Currently_TEAS_Plus import scrape_currently_teas_status
# from Status_Components.Register_Scraper import scrape_register
# from Status_Components.Mark_Type_Scraper import scrape_mark_type
# from Status_Components.TM5_Common_Status_Descriptor import scrape_tm5_common_status_descriptor
# from Status_Components.Status_Scraper import scrape_status_text
# from Status_Components.Status_Date_Scraper import scrape_status_date
# from Status_Components.Publication_Date_Scraper import scrape_publication_date
# from Status_Components.Notice_of_Allowance_Date_Scraper import scrape_notice_of_allowance_date
# from Status_Components.Date_Abandoned_Scraper import scrape_date_abandoned
# from Status_Components.Date_Cancelled_Scraper import scrape_date_cancelled
# from Status_Components.Amended_to_Principal_Register import scrape_amended_to_principal_register
# from Status_Components.Date_Amended_to_Current_Register_Scraper import scrape_date_amended_to_current_register

# # Goods_and_Services
# from Goods_and_Services.For_Scraper import scrape_for_item
# from Goods_and_Services.International_Class_Scraper import scrape_international_class
# from Goods_and_Services.US_Class_Scraper import scrape_us_classes
# from Goods_and_Services.Class_Status_Scraper import scrape_class_status
# from Goods_and_Services.First_Use_Scraper import scrape_first_use
# from Goods_and_Services.Use_in_Commerce_Scraper import scrape_use_in_commerce
 
# # Attorney_Correspondence_Information
# from Attorney_Correspondence_Information.Correspondent_Name_Address_Scraper import scrape_correspondent_address
# from Attorney_Correspondence_Information.Phone_Scraper import scrape_phone_number
# from Attorney_Correspondence_Information.Fax_Scraper import scrape_fax_number
# from Attorney_Correspondence_Information.Correspondent_e_mail_Scraper import scrape_correspondent_email
# from Attorney_Correspondence_Information.Correspondent_e_mail_Authorized_Scraper import scrape_correspondent_email_authorized

# # Google Sheets Authentication
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name(
#     "G:\\My_Projects\\Uspto\\web-sracping-fc26a07ab6b1.json", scope
# )
# client = gspread.authorize(creds)

# # Open the target Google Sheet
# sheet = client.open("Uspto").sheet1
# print("✅ Google Sheets connected successfully.")

# # **Column Headers**
# column_headers = [
#     "URL", "Scraped Text", "Mark Text", "US Serial Number", "Application Filing Date", 
#     "US Registration Number", "Registration Date", "Filed as TEAS RF", "Currently TEAS Status", 
#     "Register Value", "Mark Type", "TM5 Status", "Amended to Principal Register", 
#     "Date Amended to Current Register", "Status Text", "Status Date", "Publication Date",
#     "Notice of Allowance Date", "Date Abandoned", "Date Cancelled", "For", "International Class(es)", 
#     "U.S Class(es)", "Class Status", "First Use", "Use in Commerce", "Correspondent Name/Address", 
#     "Phone Number", "Fax Number", "Correspondent Email", "Correspondent Email Authorized"
# ]

# # Check if headers exist, if not, add them
# existing_headers = sheet.row_values(1)
# if not existing_headers or existing_headers != column_headers:
#     sheet.insert_row(column_headers, 1)
#     print("📌 Column headers added successfully.")

# # **Read URLs from the text file**
# file_path = "G:\\My_Projects\\Uspto\\scraped_urls.txt"
# with open(file_path, "r") as file:
#     urls = [url.strip() for url in file.readlines() if url.strip()]  # Reading the URLs

# # Initialize undetected Chrome
# driver = uc.Chrome(version_main=133)

# # **Scrape and Save Data**
# for url in urls:
#     driver.get(url)
#     time.sleep(5)  # Wait for the page to load

#     # **Click the necessary elements first**
#     try:
#          # Find the section with data-sectiontitle="Goods and Services"
#             section = driver.find_element(By.XPATH, "//span[@data-sectiontitle='Goods and Services']/a")
    
#         # Click on it
#             ActionChains(driver).move_to_element(section).click().perform()
#             time.sleep(2)
    
#             print("✅ Successfully clicked on 'Goods and Services' section.")

#         # Locate the section using its unique attribute
#             attorney_section = driver.find_element(By.XPATH, "//span[@data-sectiontitle='Attorney/Correspondence Information']/a")
    
#         # Click on it
#             ActionChains(driver).move_to_element(attorney_section).click().perform()
#             time.sleep(2)
    
#             print("✅ Successfully clicked on 'Attorney/Correspondence Information' section.")

#     except NoSuchElementException as e:
#         print(f"⚠️ Error occurred during clicks: {str(e)}")
#         continue  # Skip this URL

#     # Scrape Data after clicking the elements
#     scraped_data = [
#         url,
#         scrape_generated_text(driver, url),
#         scrape_mark_text(driver),
#         scrape_us_serial_number(driver),
#         scrape_application_filing_date(driver),
#         scrape_us_registration_number(driver),
#         scrape_registration_date(driver),
#         scrape_filed_as_teas(driver),
#         scrape_currently_teas_status(driver),
#         scrape_register(driver),
#         scrape_mark_type(driver),
#         scrape_tm5_common_status_descriptor(driver),
#         scrape_amended_to_principal_register(driver),
#         scrape_date_amended_to_current_register(driver),
#         scrape_status_text(driver),
#         scrape_status_date(driver),
#         scrape_publication_date(driver),
#         scrape_notice_of_allowance_date(driver),
#         scrape_date_abandoned(driver),
#         scrape_date_cancelled(driver),
#         scrape_for_item(driver),
#         scrape_international_class(driver),
#         scrape_us_classes(driver),
#         scrape_class_status(driver),
#         scrape_first_use(driver),
#         scrape_use_in_commerce(driver),
#         scrape_correspondent_address(driver),
#         scrape_phone_number(driver),
#         scrape_fax_number(driver),
#         ", ".join(scrape_correspondent_email(driver)) if isinstance(scrape_correspondent_email(driver), list) else scrape_correspondent_email(driver),
#         scrape_correspondent_email_authorized(driver)
#     ]

#     # Append data if at least one field is valid
#     if any(scraped_data[1:]):  
#         sheet.append_row(scraped_data)

# # Close the browser
# driver.quit()
# print("✅ Scraping process completed successfully.")
















# Main_Scraper.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials # type: ignore
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# Status_Components
from Status_Components.Generated_Scraper import scrape_generated_text
from Status_Components.Mark_Scraper import scrape_mark_text
from Status_Components.US_Serial_Number import scrape_us_serial_number
from Status_Components.Application_Filing_Date import scrape_application_filing_date
from Status_Components.US_Registration_Number import scrape_us_registration_number
from Status_Components.Registration_Date import scrape_registration_date
from Status_Components.Filed_as_TEAS_RF import scrape_filed_as_teas
from Status_Components.Currently_TEAS_Plus import scrape_currently_teas_status
from Status_Components.Register_Scraper import scrape_register
from Status_Components.Mark_Type_Scraper import scrape_mark_type
from Status_Components.TM5_Common_Status_Descriptor import scrape_tm5_common_status_descriptor
from Status_Components.Status_Scraper import scrape_status_text
from Status_Components.Status_Date_Scraper import scrape_status_date
from Status_Components.Publication_Date_Scraper import scrape_publication_date
from Status_Components.Notice_of_Allowance_Date_Scraper import scrape_notice_of_allowance_date
from Status_Components.Date_Abandoned_Scraper import scrape_date_abandoned
from Status_Components.Date_Cancelled_Scraper import scrape_date_cancelled
from Status_Components.Amended_to_Principal_Register import scrape_amended_to_principal_register
from Status_Components.Date_Amended_to_Current_Register_Scraper import scrape_date_amended_to_current_register

# Goods_and_Services
from Goods_and_Services.For_Scraper import scrape_for_item
from Goods_and_Services.International_Class_Scraper import scrape_international_class
from Goods_and_Services.US_Class_Scraper import scrape_us_classes
from Goods_and_Services.Class_Status_Scraper import scrape_class_status
from Goods_and_Services.First_Use_Scraper import scrape_first_use
from Goods_and_Services.Use_in_Commerce_Scraper import scrape_use_in_commerce

# Attorney_Correspondence_Information
from Attorney_Correspondence_Information.Correspondent_Name_Address_Scraper import scrape_correspondent_address
from Attorney_Correspondence_Information.Phone_Scraper import scrape_phone_number
from Attorney_Correspondence_Information.Fax_Scraper import scrape_fax_number
from Attorney_Correspondence_Information.Correspondent_e_mail_Scraper import scrape_correspondent_email
from Attorney_Correspondence_Information.Correspondent_e_mail_Authorized_Scraper import scrape_correspondent_email_authorized

def run_scraper(urls):
    # Google Sheets Authentication
    scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "G:\\My_Projects\\Uspto\\web-sracping-fc26a07ab6b1.json", scopes=scopes
    )
    client = gspread.authorize(creds)
    sheet = client.open("Uspto").sheet1
    print("✅ Google Sheets connected successfully.")

    # Headers setup
    column_headers = [
        "URL", "Scraped Text", "Mark Text", "US Serial Number", "Application Filing Date", 
        "US Registration Number", "Registration Date", "Filed as TEAS RF", "Currently TEAS Status", 
        "Register Value", "Mark Type", "TM5 Status", "Amended to Principal Register", 
        "Date Amended to Current Register", "Status Text", "Status Date", "Publication Date",
        "Notice of Allowance Date", "Date Abandoned", "Date Cancelled", "For", "International Class(es)", 
        "U.S Class(es)", "Class Status", "First Use", "Use in Commerce", "Correspondent Name/Address", 
        "Phone Number", "Fax Number", "Correspondent Email", "Correspondent Email Authorized"
    ]

    existing_headers = sheet.row_values(1)
    if not existing_headers or existing_headers != column_headers:
        sheet.insert_row(column_headers, 1)
        print("📌 Column headers added successfully.")

    # Start driver
    driver = uc.Chrome(version_main=133)
    all_scraped = []

    for url in urls:
        try:
            driver.get(url)
            time.sleep(5)

            # Click Goods and Services
            try:
                section = driver.find_element(By.XPATH, "//span[@data-sectiontitle='Goods and Services']/a")
                ActionChains(driver).move_to_element(section).click().perform()
                time.sleep(2)

                attorney_section = driver.find_element(By.XPATH, "//span[@data-sectiontitle='Attorney/Correspondence Information']/a")
                ActionChains(driver).move_to_element(attorney_section).click().perform()
                time.sleep(2)
            except NoSuchElementException:
                print(f"⚠️ Skipping {url} — Clickable section not found.")
                continue

            # Scraping data
            scraped_data = [
                url,
                scrape_generated_text(driver, url),
                scrape_mark_text(driver),
                scrape_us_serial_number(driver),
                scrape_application_filing_date(driver),
                scrape_us_registration_number(driver),
                scrape_registration_date(driver),
                scrape_filed_as_teas(driver),
                scrape_currently_teas_status(driver),
                scrape_register(driver),
                scrape_mark_type(driver),
                scrape_tm5_common_status_descriptor(driver),
                scrape_amended_to_principal_register(driver),
                scrape_date_amended_to_current_register(driver),
                scrape_status_text(driver),
                scrape_status_date(driver),
                scrape_publication_date(driver),
                scrape_notice_of_allowance_date(driver),
                scrape_date_abandoned(driver),
                scrape_date_cancelled(driver),
                scrape_for_item(driver),
                scrape_international_class(driver),
                scrape_us_classes(driver),
                scrape_class_status(driver),
                scrape_first_use(driver),
                scrape_use_in_commerce(driver),
                scrape_correspondent_address(driver),
                scrape_phone_number(driver),
                scrape_fax_number(driver),
                ", ".join(scrape_correspondent_email(driver)) if isinstance(scrape_correspondent_email(driver), list) else scrape_correspondent_email(driver),
                scrape_correspondent_email_authorized(driver)
            ]

            if any(scraped_data[1:]):
                sheet.append_row(scraped_data)
                all_scraped.append(url)

        except Exception as e:
            print(f"❌ Error processing {url}: {str(e)}")
            continue

    driver.quit()
    print("✅ Scraping process completed successfully.")
    return all_scraped
