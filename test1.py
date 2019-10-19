from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome("C:\\exes\\chromedriver.exe")


def ABI_INFORM():
    print("ABI / INFORM testi bitti")
    



# ABI / INFORM 




browser.get('https://icproxy.sabanciuniv.edu:2047/login?url=https://search.proquest.com/abicomplete?accountid=13638')
timeout = 15
try:
    element_present = EC.presence_of_element_located((By.ID, 'searchTerm'))
    WebDriverWait(browser, timeout).until(element_present)
    searchTerm = browser.find_element_by_id('searchTerm')
    searchTerm.send_keys("modern")

    try:
        element_present = EC.presence_of_element_located((By.ID, 'expandedSearch'))
        WebDriverWait(browser, timeout).until(element_present) 

        expandedSearch = browser.find_element_by_id("expandedSearch")
        expandedSearch.click()

    except TimeoutException:
        print ("Timed out waiting for page to load")



    
except TimeoutException:
    print ("ABI / INFORM => Timed out")

print("ABI / INFORM => Test OK")






print("Test işlemleri tamamlandı")
