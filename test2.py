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

'''
0. inform user for starting test
1. load page
2. check if page is fully loaded
3. find text element
4. send keys
5. press button
6. check if page is fully loaded
7. get first element
8. download pdf / check full text
9. finish test
10. inform user for finished test
'''
# https://icproxy.sabanciuniv.edu:2047/login?url=https://search.proquest.com/abicomplete?accountid=13638


def ABI_INFORM(timeOut=15):
    print("ABI / INFORM testi başlıyor")

    browser.get('https://icproxy.sabanciuniv.edu:2047/login?url=https://search.proquest.com/abicomplete?accountid=13638')
    
    try:
        element_present = EC.presence_of_element_located((By.ID, 'searchTerm'))
        WebDriverWait(browser, timeOut).until(element_present)
    except TimeoutException:
        print ("ABI / INFORM load error, exceed timeout time")
        return
    
    searchTerm = browser.find_element_by_id('searchTerm')
    searchTerm.send_keys("modern")

    expandedSearch = browser.find_element_by_id("expandedSearch")
    expandedSearch.click()

    try:
        element_present = EC.presence_of_element_located((By.ID, 'addFlashPageParameterformat_fulltextPDF'))
        WebDriverWait(browser, timeOut).until(element_present)
    except TimeoutException:
        print ("ABI / INFORM result page load error, exceed timeout time")
        return

    addFlashPageParameterformat_fulltextPDF = browser.find_element_by_id("expandedSearch")
    addFlashPageParameterformat_fulltextPDF.click()
    
    print("ABI / INFORM testi bitti")
    

ABI_INFORM()
