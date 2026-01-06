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


class BusinessGlossary_KPIPage():
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
        self.detect_calculation_descp = "//p[text() = 'Calculation Description']"
        self.enter_calculation_description = "calculation_description"
        self.enter_formula = "formula"
        self.enter_sql_code = "//div[@class = 'cm-activeLine cm-line']"
        self.enter_dimensions = "(//input[@class = 'flex-1 min-w-[120px] bg-transparent border-none outline-none text-sm'])[1]"
        self.detect_frequency_page = "//p[text() = 'Add Business Glossary']"
        self.click_frequency = "react-select-16-input"
        self.enter_minimum_expected_value = "min_value"
        self.enter_maximum_expected_value = "max_value"
        self.enter_baseline_year = "baseline_year"
        self.enter_baseline_value = "baseline_value"
        self.enter_baseline_unit = "react-select-17-input"
        self.enter_unit_of_measure = "unit_of_measure"
        self.enter_target = "target"
        self.enter_data_retention = "//input[@class = 'w-full h-10 px-3 py-2 border-0 rounded-none focus:outline-none focus:ring-0 text-sm placeholder-gray-500 bg-white [&::-webkit-inner-spin-button]:opacity-100 [&::-webkit-outer-spin-button]:opacity-100']"
        self.detect_stewardship_page = "//p[text() = 'Business Executive']"
        self.click_consumer = "react-select-24-input"
        self.click_finish_btn = "//button[text() = 'Finish']"
        self.click_action_btn = "(//button[@class = 'rounded-full '])[1]"
        self.click_edit_btn = "//span[text() = 'Edit']"
        self.click_view_btn = "//span[text() = 'View']"
        self.click_hierarchy_btn = "//span[text() = 'Hierarchy']"
        self.click_attributes_btn = "//span[text() = 'Attributes']"
        self.click_frequency_btn = "//span[text() = 'Frequency']"
        self.click_stewardship_btn = "//span[text() = 'Stewardship']"
        self.click_cross_btn = "//div[@class = 'hover:bg-background-tertiary me-2 cursor-pointer rounded-lg p-1']"
        self.detect_view_page = "//button[text() = 'Add']"
        self.click_delete_btn = "//span[text() = 'Delete']"
        self.detect_delete_bg = "//p[text() = 'Connected Glossaries']"
        self.click_confirm_btn  = "//button[text() = 'Confirm']"
        self.click_calculation = "//span[text() = 'Calculation']"

    def Click_Calculation(self):
        self.driver.find_element(by=By.XPATH, value=self.click_calculation).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.click_frequency_btn).click()


    def Assert_Glossary_Deleted(self):
        try:
            toast = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@role='alert']")
                )
            )

            toast_text = toast.text.strip().lower()
            print("Toast message:", toast_text)

            # ✅ ONLY delete success message allowed
            assert "deleted successfully" in toast_text, (
                f"Glossary delete FAILED. Actual toast message: '{toast_text}'"
            )

        except TimeoutException:
            assert False, "Glossary delete FAILED. No toast message appeared."


    # def Click_Delete_BG(self):
    #      self.driver.find_element(by=By.XPATH, value= self.click_delete_btn).click()
    #

    def Click_Delete_Btn(self):
        self.driver.find_element(by=By.XPATH, value= self.click_delete_btn).click()
        time.sleep(2)


    def Click_Delete_Confirm_Btn(self):
        self.driver.find_element(by=By.XPATH, value=self.click_confirm_btn).click()
        time.sleep(1)



    def Detect_View_Page(self):
        if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.detect_view_page))):
            return True
        else:
            return False


    def Click_Cross_Btn(self):
        self.driver.find_element(by=By.XPATH, value= self.click_cross_btn).click()
        time.sleep(2)


    def Click_Stewardship_Btn(self):
        self.driver.find_element(by=By.XPATH, value= self.click_stewardship_btn).click()
        time.sleep(2)


    def Click_Frequency_Btn(self):
        self.driver.find_element(by=By.XPATH, value= self.click_frequency_btn).click()
        time.sleep(2)


    def Click_Attributes_Btn(self):
        self.driver.find_element(by=By.XPATH, value= self.click_attributes_btn).click()
        time.sleep(2)


    def Click_Hierarchy_Btn(self):
        self.driver.find_element(by=By.XPATH, value= self.click_hierarchy_btn).click()
        time.sleep(2)


    def Click_View_Btn(self):
        self.driver.find_element(by=By.XPATH, value= self.click_view_btn).click()
        time.sleep(2)

    def Assert_Glossary_Updated(self):
        try:
            toast = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@role='alert']")
                )
            )

            toast_text = toast.text.strip().lower()
            print("Toast message:", toast_text)

            # ✅ ONLY update success message allowed
            assert "updated successfully" in toast_text, (
                f"Glossary update FAILED. Actual toast message: '{toast_text}'"
            )

        except TimeoutException:
            assert False, "Glossary update FAILED. No toast message appeared."


    def set_browser_zoom_100(self):
        # Browser zoom 80%
        self.driver.execute_script("document.body.style.zoom='100%'")

    def Click_Edit_Btn(self):
        self.driver.find_element(by=By.XPATH, value= self.click_edit_btn).click()
        time.sleep(2)



    def set_browser_zoom_75(self):
        # Browser zoom 80%
        self.driver.execute_script("document.body.style.zoom='75%'")

    def Business_Glossary_ScrollToDown(self):

        self.driver.execute_script("""
            const scrollDiv = document.querySelector('div.overflow-auto');
            if (scrollDiv) {
                scrollDiv.scrollTop = scrollDiv.scrollHeight + 700;
            }
        """)

    def Action_Btn(self):
        self.driver.find_element(by=By.XPATH, value= self.click_action_btn).click()
        time.sleep(2)

    def Click_Finish_Btn(self):
        self.driver.find_element(by=By.XPATH, value= self.click_finish_btn).click()
        time.sleep(2)


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



    def Click_Consumer(self):
        self.driver.find_element(by=By.ID, value=self.click_consumer).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_consumer).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)



    def Enter_Data_Retention(self):
        self.driver.find_element(by=By.XPATH, value=self.enter_data_retention).send_keys("34")
        time.sleep(2)

    def Enter_Target(self):
        self.driver.find_element(by=By.NAME, value=self.enter_target).send_keys("iowe")
        time.sleep(2)

    def Enter_Unit_of_Measure(self):
        self.driver.find_element(by=By.NAME, value=self.enter_unit_of_measure).send_keys("23")
        time.sleep(2)


    def Enter_Baseline_Unit(self):
        self.driver.find_element(by=By.ID, value=self.enter_baseline_unit).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.enter_baseline_unit).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)


    def Enter_Baseline_Value(self):
        self.driver.find_element(by=By.NAME, value=self.enter_baseline_value).send_keys("1950")
        time.sleep(1)



    def Enter_Baseline_Year(self):
        self.driver.find_element(by=By.NAME, value=self.enter_baseline_year).send_keys("1950")
        time.sleep(1)


    def Enter_Maximum_Expected_Value(self):
        self.driver.find_element(by=By.NAME, value=self.enter_maximum_expected_value).send_keys("25")
        time.sleep(1)


    def Enter_Minimum_Expected_Value(self):
        self.driver.find_element(by=By.NAME, value=self.enter_minimum_expected_value).send_keys("12")
        time.sleep(1)

    def Click_Frequency(self):
        self.driver.find_element(by=By.ID, value=self.click_frequency).click()
        time.sleep(1)
        self.driver.find_element(by=By.ID, value=self.click_frequency).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)

    def Detect_Stewardship_Page(self):
        if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.detect_stewardship_page))):
            return True
        else:
            return False



    def Detect_Frequency_Page(self):
        if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.detect_frequency_page))):
            return True
        else:
            return False


    def Enter_Dimensions(self):
        self.driver.find_element(by=By.XPATH, value=self.enter_dimensions).send_keys(" enter after each value to add multiple dimensions" + ''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(1)



    def Enter_Sql_Code(self):
        self.driver.find_element(by=By.XPATH, value= self.enter_sql_code).send_keys("INSERT INTO business_glossary (name) VALUES ('Test Glossary');")
        time.sleep(1)


    def Enter_Formula(self):
        self.driver.find_element(by=By.NAME, value=self.enter_formula).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value=self.enter_formula).send_keys("34")
        time.sleep(1)


    def Enter_Calculation_Descp(self):
        self.driver.find_element(by=By. NAME, value=self.enter_calculation_description).send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        time.sleep(2)



    def Calculation_ScrollToTop(self):
        scroll_container = WebDriverWait(self.driver, 10).until(
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

    def Detect_Calculation_Descp(self):
        if WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.detect_calculation_descp))):
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
        time.sleep(3)


    def Click_Service_Catalog(self):
        self.driver.find_element(by=By.ID, value= self.click_service_catalog).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=self.click_service_catalog).send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    def Enter_Term_Definition_Arabic(self):
        self.driver.find_element(by=By.NAME, value=self.enter_term_definition_arabic).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=self.enter_term_definition_arabic).send_keys("KPI Flow: Create Business Glossary by Manan in arabic" + ''.join(random.choice(string.ascii_lowercase) for i in range(1)))
        time.sleep(1)

    def Enter_Term_Definition(self):
        self.driver.find_element(by=By.NAME, value=self.enter_term_definition).send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=self.enter_term_definition).send_keys("KPI Flow: Create Business Glossary by Manan in English"+ ''.join(random.choice(string.ascii_lowercase) for i in range(1)))
        time.sleep(1)



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