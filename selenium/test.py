from selenium import webdriver      #importing webdriver in order to open web creating a driver
from selenium.webdriver.common.by import By

#creating chrome options to enable diff options such aas one to keep the tab open.
# chrome_options=webdriver.ChromeOptions()  #creates a new class object . <class'selenium.webdriver.chrome.options.Options'>
# chrome_options.add_experimental_option('detach',True)


#creating the driver to dirve though the web pages
# driver=webdriver.Chrome(options=chrome_options)  #now passing on the chrome options so tab doesn't close

#USING SELENIUM WEB DRIVER TO COMPLETE THE AMAZON PRICE TRACKER PROJECT
# driver.get('https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX2F5QT/ref=sr_1_2_sspa?sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY')

# #using find element method along with 'BY' class to get hold of the price tag.
# # price_symbol=driver.find_element(By.CSS_SELECTOR,".a-price-symbol")

# price=driver.find_element(By.CLASS_NAME,value="a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay")    #<class 'selenium.webdriver.remote.webelement.WebElement'>
# # #to get text out from the class obj of selenium web element.

# print(f"The current price of the iphone is {price.text}")   #.text returns the text from the selemnium class object.
# # print(price_symbol.text)


# #SELENIUM IS MUCH FASTER AND LESS LINE OF CODE THAN BEAUTIFUL SOUP BECAUSE WE'RE ACTUALLY DRIVING THE BROWSER
# #THE BROWSERS ALREADY SENDING ALL OF THE INFO TO AMAZON SITE - HEADER GET REQUESTS ETC THT WE NEEDED DO IN BEAUTIFUL SOUP TO GET REQUEST RESPONSE FORM AMAZON SITE.


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


#Using diff attributes to search through.
search_bar=driver.find_element(By.NAME,value="q")
# print(search_bar.get_attribute("placeholder"))    'Search'   we can get attrbute value by passing out the attribute name onto the get attribute function.
# print(search_bar.get_attribute("role"))    'textbox'
# print(search_bar.tag_name)                'input'   #.tag_name returns the name of the tag.

button=driver.find_element(By.ID,value='submit')   #.size  returns the size of the element.
# print(button.size)                               {'height': 40, 'width': 46}

#using css selectors. to get elemnt.
docs=driver.find_element(By.CSS_SELECTOR,".small-widget.documentation-widget p a")
print(docs.text)           #docs.python.org

#IF NONE OF THE ABOVE METHOD WORKS WE USE XPATH 
bug=driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')   #remmeber to use single quotes as path already  contains double quotations.
print(bug.text)    #Submit Website Bug


driver.find_elements(By.CSS_SELECTOR)


driver.quit()
#to clear the browser each time we run the file again.