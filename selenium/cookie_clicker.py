from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')


#getting hold of the cookie to click.
cookie=driver.find_element(By.CSS_SELECTOR,value='#cookie')

#getting hold of the points
money=driver.find_element(By.ID,value='money')

#getting hold of the items to purchase in the store.
store=driver.find_elements(By.CSS_SELECTOR,value='#store div b')
purchasing_amt=[i.text for i in store]
print(purchasing_amt)
amount=purchasing_amt[0].lstrip(' - ').strip(',')
print(amount)



# #creating a timeout.
# timeout=time.time()+5       ## get the current time in seconds since the epoch(epoch in a kind of time measuring reference for python module since 1990)
# five_min=time.time()+60*5     #this will return the current time and then add 5 mins ,i.e. 300 secs into our timeout.





# while True:
#     cookie.click()            #to click on the cookie element
#     # Every 5 seconds:
#     if time.time() > timeout:    #if 5 secs have passed since last time.time()  which means python will call time.time() and check time out , and compare the timeout which was before set to time.time()+5 hence if current time.time() output greater than timeout below conditions will be executed (dynamic typing)
        
#         #get all the upgrade <b> tags
        

