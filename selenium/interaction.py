from selenium import webdriver
from selenium.webdriver.common.by import By     #helps us to use by class to find elements.
from selenium.webdriver.common.keys import Keys   #helps us to use standard keyboard keys such as enter tab shift etc

#adding chrome options 
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

#getting hold of total articles

article=driver.find_element(By.CSS_SELECTOR,value="div #articlecount li:nth-child(2) a[title='Special:Statistics']")
# article.click()  this will click on the element if it is a href link anchor tag it will drag you directly to the linked page.


#VERY VERY IMPORTANT 👇👇👇👇👇  (how to choose different value attribute and when a list all has same class everythig to choose the sequence we want)
# article=driver.find_element(By.CSS_SELECTOR,value="div #articlecount li:nth-child(2) a[title='Special:Statistics']")

#GETTING HOLD OF THE ELEMENT BY USING LINK TEXT
# link=driver.find_element(By.LINK_TEXT,value='Content portals')   #this method takes the text of the link and then drives you there.

#finding the search bar
search=driver.find_element(By.CSS_SELECTOR,value='.vector-icon.mw-ui-icon-search.mw-ui-icon-wikimedia-search')
search.click()


#after clicking getting hold of the search bar
search_bar=driver.find_element(By.NAME,value="search")   #keep in my mind to get hold of the input search bar not the search bar wrapper or placeholder

#sending out keyboard inputs to the search tab after clicking on it to open the search tab, (see the website you'll understand)
search_bar.send_keys('Python',Keys.ENTER)
# search.send_keys(Keys.ENTER)