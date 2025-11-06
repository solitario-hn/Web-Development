from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://secure-retreat-92358.herokuapp.com/')

#getting hold of first name box.
fname=driver.find_element(By.NAME,value='fName')
lname=driver.find_element(By.NAME,value='lName')
email=driver.find_element(By.NAME,value='email')
signup_button=driver.find_element(By.CLASS_NAME,value='btn.btn-lg.btn-primary.btn-block')
#sending out the details

fname.send_keys("HEM")
lname.send_keys("Bablu")
email.send_keys("xtraa56789@gmail.com")

#clicking up the signup button
signup_button.send_keys(Keys.ENTER)