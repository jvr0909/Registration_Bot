from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import yaml
import time as t



def register(is_recent, most_recent_notification):
    if is_recent == False:
        print("No new Class")
        return
    else:
        # read credentials.yml
        with open("credentials.yml", "r") as f:
            content = f.read()
        # create driver
        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://banner.apps.uillinois.edu/StudentRegistrationSSB/ssb/registration?mepCode=1UIUC")


        #click on the "Register" button
        button = driver.find_element(By.ID, "registerLink")
        button.click()

        # from credentials.yml import user name and password
        my_credentials = yaml.load(content, Loader=yaml.FullLoader)
        netID, netIDPassword = my_credentials["netID"], my_credentials["illinoisPassword"]
        #login with netID and password
        netID_input = driver.find_element(By.ID, "netid")
        netID_input.send_keys(netID)
        netIDPassword_input = driver.find_element(By.ID, "easpass")
        netIDPassword_input.send_keys(netIDPassword)
        netIDPassword_input.send_keys(Keys.RETURN)

        #click on select term
        select_term = driver.find_element(By.ID, "select2-chosen-1")
        select_term.click()
        t.sleep(1)
        #select term
        term = driver.find_element(By.ID, "120231")
        term.click()
        #click on submit
        submit = driver.find_element(By.ID, "term-go")
        submit.click()

        #click on enter CRN
        t.sleep(1)
        enter_CRN = driver.find_element(By.ID, "enterCRNs-tab")
        enter_CRN.click()


        course_crn = most_recent_notification[2]
        #enter CRN
        crn_input = driver.find_element(By.ID, "txt_crn1")
        crn_input.send_keys(course_crn)
        #click add to summary
        add_to_summary = driver.find_element(By.ID, "addCRNbutton")
        add_to_summary.click()
        #wait 1 second for page to load
        t.sleep(1)
        submit = driver.find_element(By.ID, "saveButton")
        submit.click()
        driver.close()
        driver.quit()
        print("Registration Successful!")






