#SCRAOING OUT DATES FROM A PYTHON.ORG WEBSITE.

from selenium import webdriver
from selenium.webdriver.common.by import By


#adding chrome options to guard the closing of the browser
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)


#creating a driver.
driver=webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')


#finding date element along with By class,
date_element=driver.find_elements(By.CSS_SELECTOR,value='.medium-widget.event-widget.last .menu li time')
name_element=driver.find_elements(By.CSS_SELECTOR,value='.medium-widget.event-widget.last .menu li a')
# print(type(date_element))  checking
dates=[item.text for item in date_element]
name=[item.text for item in name_element]
events={}

# for elements in date_element:
#     dates.append(elements.text)
    
# for elements in 

for n in range(len(date_element)):
    events[n]={
        'time':dates[n],
        'name':name[n]
    }
    
    
print(events)