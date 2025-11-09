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

#getting hold of the items to purchase in the store.
# store=driver.find_elements(By.CSS_SELECTOR,value='#store div b')
# purchasing_amt=[i.text for i in store]
# amount=[]
# for i in purchasing_amt[:-2]:
#     amount.append(int(i.split('-')[1].strip().replace(',',"")))

#since the store prices change dynamically after each purschase we need to keep it inside loop.

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
#we need id as well to click and choose the affordable items more easily.


#creating a timeout.
timeout=time.time()+5       ## get the current time in seconds since the epoch(epoch in a kind of time measuring reference for python module since 1990)
five_min=time.time()+60*5     #this will return the current time and then add 5 mins ,i.e. 300 secs into our timeout.

value=0

while True:
    #getting hold of the points
    money=int(driver.find_element(By.ID,value='money').text.replace(',',""))
        
    cookie.click()            #to click on the cookie element
    # Every 5 seconds:
    if time.time() > timeout:    #if 5 secs have passed since last time.time()  which means python will call time.time() and check time out , and compare the timeout which was before set to time.time()+5 hence if current time.time() output greater than timeout below conditions will be executed (dynamic typing)
        
        #get all the upgrade <b> tags = amount tags. 
        store=driver.find_elements(By.CSS_SELECTOR,value='#store div b')
        purchasing_amt=[i.text for i in store]
        amount=[]
        for i in purchasing_amt[:-2]:
            amount.append(int(i.split('-')[1].strip().replace(',',"")))


 # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(amount)):
            cookie_upgrades[amount[n]] = item_ids[n]

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if money > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(f" yo the cookie count here bitch--{cookie_per_s}")
        break
            

