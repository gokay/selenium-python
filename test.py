from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome(options=options)

browser = webdriver.Chrome("C:\\exes\\chromedriver.exe")

# ABI / INFORM 
try:
    browser.get('https://search.proquest.com/abicomplete/index?accountid=13638')
    
    time.sleep(5)
    print(browser.title)
    print(browser.current_url)
    searchTerm = browser.find_element_by_id('searchTerm')
    if searchTerm.is_displayed:
        if searchTerm.is_enabled:
            searchTerm.send_keys("modern")
            id="expandedSearch"
            expandedSearch = browser.find_element_by_id("expandedSearch")
            expandedSearch.click()
            time.sleep(5)

            print("OK : ABI / INFORM")
except:
    print("ERROR : ABI / INFORM")
    browser.quit()

print("Test işlemleri tamamlandı")

# Close current open page
# browser.close()

'''
# Close all open pages
browser.quit()

browser.back()

browser.forward()
'''