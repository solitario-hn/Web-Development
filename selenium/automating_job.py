from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
# from webdriver_manager.chrome import ChromeDriverManager
import time
URL='https://www.linkedin.com/jobs/search/?currentJobId=4318073502&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom'
EMAIL_ID='xtraa56789aa@gmail.com'
PASSWORD='SayO8980%'


# Optional - Automatically keep your chromedriver up to date.
# from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager
# chrome_driver_path = ChromeDriverManager(path=YOUR CHROME DRIVER FOLDER).install()


# Optional - Keep the browser open if the script crashes.
# service = ChromeService(executable_path=chrome_driver_path)   from selenium.webdriver.chrome.service import Service as ChromeService
#driver = webdriver.Chrome(service=service, options=chrome_options)

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(url=URL)


time.sleep(2)
cross_pop_up=driver.find_element(By.XPATH,value='//*[@id="base-contextual-sign-in-modal"]/div/section/button')
cross_pop_up.click()

time.sleep(2)
sign_in=driver.find_element(By.LINK_TEXT,value='Sign in')
sign_in.click()

time.sleep(2)
email_input=driver.find_element(By.ID,value='username')
email_input.send_keys(EMAIL_ID)

password_input=driver.find_element(By.ID,value='password')
password_input.send_keys(PASSWORD)

signin_button=driver.find_element(By.CSS_SELECTOR,value='.login__form_action_container button')
signin_button.click()


#getting hold of all the listings in the panel
time.sleep(2)
job_lists=driver.find_elements(By.CSS_SELECTOR,value="ul.aXAnFHqprWGyZXmazmHqfgWhYHIucWRPhUtQ li")
job_ids=[]
#getting hold of all the id of the listings 
for i in job_lists:
    ids=i.get_attribute('id')
    if ids != '':
        job_ids.append(ids)
        
        
job_click=driver.find_element(By.ID, value='ember170')
job_click.click()
apply_button=driver.find_element(By.ID,value='jobs-apply-button-id')
apply_button.click()  

#   
        
        
        
#trying clicking on each job title (by id)
# for i in job_ids:
#     job_click=driver.find_element(By.ID,value=i)
#     job_click.click()
    
#     #Clicking on the easy apply button 
#     try:
#         apply_button=driver.find_element(By.ID,value='jobs-apply-button-id')
#         apply_button.click()
        
    
        
    



