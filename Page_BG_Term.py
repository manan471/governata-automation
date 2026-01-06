import unittest
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import time
import os


class BusinessGlossary_TermPage():
    def __init__(self, driver):
        self.driver = driver
        self.click_addbtn = "//button[text() = 'Add']"
        self.click_businessglossary = "//span[text() = 'Business Glossary']"
        self.enter_term_definition = "name"
        self.enter_term_definition_arabic = "name_ar"
        self.click_service_catalog = "react-select-10-input"
        self.click_parent_category = "react-select-11-input"
        self.click_domain = "react-select-12-input"
        self.click_folder = "react-select-13-input"
        self.click_related = "react-select-14-input"
        self.enter_descp = "description"
        self.click_nextbtn = "//button[text() = 'Next']"
        self.detect_attributes_page = "//h3[text() = 'Attributes type']"
        self.enter_attribute_name_eng = "name"
        self.enter_attribute_name_ar = "name_ar"
        self.click_data_type = "react-select-16-input"
        self.click_classification = "react-select-17-input"
        self.enter_attribute_descp = "description"
        self.enter_attribute_descp_ar = "description_ar"
        self.detect_stewardship_page = "//h3[text() = 'Attach any file']"
        self.click_business_executive = "react-select-18-input"
        self.click_business_steward = "react-select-19-input"
        self.click_data_steward = "react-select-20-input"
        self.click_legal_advisor = "react-select-21-input"
        self.click_department = "react-select-22-input"
        self.click_data_office_employee = "react-select-23-input"
        self.enter_document = "//p[text() ='Click here or drop files to upload']"
        self.click_finish_btn = "//button[text() = 'Finish']"


    def Click_FinishBtn(self):
        self.driver.find_element(by=By.XPATH, value= self.click_finish_btn).click()

    def Assert_Glossary_Created(self):
        try:
            toast = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@role='alert']")
                )
            )

            toast_text = toast.text.strip()
            print("Toast message:", toast_text)

            assert "created successfully" in toast_text.lower(), \
                f"BG is not created. Actual message: {toast_text}"

        except TimeoutException:
            assert False, "BG is not created. No toast message appeared."




    def Upload_Document(self, file_path):
        file_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='file']")
            )
        )

        file_input.send_keys("C:\\Users\\Dell\\Downloads\\testing purpose document.pdf")

    def Click_Data_Office_Employee(self):
        self.driver.find_element(by=By.ID, value= self.click_data_office_employee).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_data_office_employee).send_keys(Keys.ARROW_DOWN + Keys.ENTER)



    def Click_Department(self):
        self.driver.find_element(by=By.ID, value= self.click_department).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_department).send_keys(Keys.ARROW_DOWN + Keys.ENTER)



    def Click_Legal_Advisor(self):
        self.driver.find_element(by=By.ID, value= self.click_legal_advisor).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_legal_advisor).send_keys(Keys.ARROW_DOWN + Keys.ENTER)



    def Click_Data_Steward(self):
        self.driver.find_element(by=By.ID, value= self.click_data_steward).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_data_steward).send_keys(Keys.ARROW_DOWN + Keys.ENTER)



    def Click_Business_Steward(self):
        self.driver.find_element(by=By.ID, value= self.click_business_steward).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_business_steward).send_keys(Keys.ARROW_DOWN + Keys.ENTER)




    def Click_Business_Executive(self):
        self.driver.find_element(by=By.ID, value= self.click_business_executive).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_business_executive).send_keys(Keys.ARROW_DOWN + Keys.ENTER)


    def Stewardship_ScrollModalToTop(self):
        scroll_container = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'flex-1') and contains(@class,'overflow-auto')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollTop = 0;",
            scroll_container
        )

    def Detect_Stewardship_Page(self):
        if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.detect_stewardship_page))):
            return True
        else:
            return False


    def Enter_Attribute_Descp_Ar(self):
        self.driver.find_element(by=By.NAME, value=self.enter_attribute_descp_ar).send_keys("Created Trem flow by Manan in english" + ''.join(random.choice(string.ascii_lowercase) for i in range(5)))


    def Enter_Attribute_Descp(self):
        self.driver.find_element(by=By.NAME, value=self.enter_attribute_descp).send_keys("Created Trem flow by Manan in Arabic" + ''.join(random.choice(string.ascii_lowercase) for i in range(5)))

    def Click_Classification(self):
        self.driver.find_element(by=By.ID, value= self.click_classification).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_classification).send_keys(Keys.ARROW_DOWN + Keys.ENTER)


    def Click_Data_type(self):
        self.driver.find_element(by=By.ID, value= self.click_data_type).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_data_type).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)

    def Enter_Attribute_Name_Ar(self):
        self.driver.find_element(by=By.NAME, value= self.enter_attribute_name_ar).send_keys("Create Attribute by Manan in english" +  ''.join(random.choice(string.ascii_lowercase) for i in range(3)))
        time.sleep(2)

    def Enter_Attribute_Name(self):
        self.driver.find_element(by=By.NAME, value=self.enter_attribute_name_eng).send_keys("Create Attribute by Manan in english" +  ''.join(random.choice(string.ascii_lowercase) for i in range(3)))
        time.sleep(2)

    def Attribute_ScrollModalToBottom(self):
        scroll_container = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'flex-1') and contains(@class,'overflow-auto')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight;",
            scroll_container
        )

    def DetectServiceCatalogPage(self):
        if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.detect_attributes_page))):
            return True
        else:
            return False



    def Click_NextBtn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_nextbtn).click()
        time.sleep(2)

    def Enter_Descp(self):
        self.driver.find_element(by=By.NAME, value=self.enter_descp).send_keys("Created Trem flow by Manan" + ''.join(random.choice(string.ascii_lowercase) for i in range(5)))

    def Click_Related(self):
        self.driver.find_element(by=By.ID, value= self.click_related).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_related).send_keys(Keys.ARROW_DOWN + Keys.ENTER)



    def Click_Folder(self):
        self.driver.find_element(by=By.ID, value= self.click_folder).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_folder).send_keys(Keys.ARROW_DOWN + Keys.ENTER)


    def Click_Domain(self):
        self.driver.find_element(by=By.ID, value= self.click_domain).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_domain).send_keys(Keys.ARROW_DOWN + Keys.ENTER)




    def Click_Parent_Category(self):
        self.driver.find_element(by=By.ID, value= self.click_parent_category).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_parent_category).send_keys(Keys.ARROW_DOWN + Keys.ENTER)


    def Click_Service_Catalog(self):
        self.driver.find_element(by=By.ID, value= self.click_service_catalog).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_service_catalog).send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    def Enter_Term_Definition_Arabic(self):
        self.driver.find_element(by=By.NAME, value=self.enter_term_definition_arabic).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=self.enter_term_definition_arabic).send_keys("Create GB by Manan in arabic" + ''.join(random.choice(string.ascii_lowercase) for i in range(3)))
        time.sleep(1)

    def Enter_Term_Definition(self):
        self.driver.find_element(by=By.NAME, value=self.enter_term_definition).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=self.enter_term_definition).send_keys("Term Flow: Create Business Glossary by Manan in English"+ ''.join(random.choice(string.ascii_lowercase) for i in range(1)))
        time.sleep(1)



    # def Enter_Term_Definition(self):
    #     self.driver.find_element(by=By.NAME, value=self.enter_term_definition).send_keys("Create GB by Manan"+ ''.join(random.choice(string.ascii_lowercase) for i in range(3)))
    #     time.sleep(1)



    def Click_BusinessGlossary(self):
        self.driver.find_element(by=By.XPATH, value=self.click_businessglossary).click()
        time.sleep(2)


    def Click_Add_Btn(self):
        self.driver.find_element(by=By.XPATH, value="//button[text() = 'Add']").click()
        time.sleep(2)


    def ScrollModalToBottom(self):
        scroll_container = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'flex-1') and contains(@class,'overflow-auto')]")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight;",
            scroll_container
        )

    # ==========================================
    # SAFE scroll to Next button (after scroll)
    # ==========================================
    def ScrollToNextButton(self):
        self.ScrollModalToBottom()

        next_btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[.//span[normalize-space()='Next']]")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            next_btn
        )