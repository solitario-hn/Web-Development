from selenium import webdriver      #importing webdriver in order to open web creating a driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#creating chrome options to enable diff options such aas one to keep the tab open.
chrome_options=webdriver.ChromeOptions()  #creates a new class object . <class'selenium.webdriver.chrome.options.Options'>
chrome_options.add_experimental_option('detach',True)

#creating the driver to dirve though the web pages
driver=webdriver.Chrome(options=chrome_options)  #now passing on the chrome options so tab doesn't close
# driver.get("https://www.amazon.com")    #it opens and closes immediately. hence we need some options to keep the tab open.


# driver.close()   #closes the tab opened at the moment only.

# driver.quit()   #closes the entire browser 

#USING SELENIUM WEB DRIVER TO COMPLETE THE AMAZON PRICE TRACKER PROJECT
# driver.get('https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX2F5QT/ref=sr_1_2_sspa?sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY')
# #using find element method along with 'BY' class to get hold of the price tag.

# time.sleep(8)
# price_symbol=driver.find_element(By.CSS_SELECTOR,".a-price-symbol")
# price=driver.find_element(By.CLASS_NAME,"a-price-whole")    #<class 'selenium.webdriver.remote.webelement.WebElement'>
# #to get text out from the class obj of selenium web element.

# print(price.text)
# print(price_symbol.text)


try:
    # Open the Amazon page
    driver.get('https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX2F5QT/ref=sr_1_2_sspa?sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY')
    
    # Wait for the price element to load (up to 10 seconds)  webdriver wait waits until (ec which is checking each element until it finds teh passed onto class html elemnt then only wait is over and web driver loads after 10 secs.
    # )
    price = WebDriverWait(driver, 10).until(    
        EC.presence_of_element_located((By.CLASS_NAME, "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"))
    )
    print(price)
    
    #------------"a-price aok-align-center reinventPricePriceToPayMargin priceToPay"---------
    #instead of using spaces we need to write it as ""a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay""
    #so it wouldn;t confuse it for class into class (selenium only issue.) 
    #try diff class name or attributes if getting blank or wrong result.
    
    
    
    
    
    # Print the price text
    # print(f"Price: {price.class_}")
    
except Exception as e:
    print(f"Error occurred: {e}")
    
finally:
    # Uncomment the line below if you want to close the browser automatically
    # driver.quit()
    pass
driver.quit()