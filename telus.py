from selenium import webdriver
import time
"""import urllib
import urllib2
    
x = raw_input("https://pharmaconnect.ca/Appointment/8f9b1c44-e98b-4d4c-8d4c-09226873e9e3/Book/ImmunizationCovid")
refreshrate = raw_input("3")
refreshrate = int(refreshrate)
driver = webdriver.Chrome()
driver.get(x)

while True:
    time.sleep(refreshrate)
    driver.refresh()"""

driver = webdriver.Firefox()
driver.get("https://pharmaconnect.ca/Appointment/8f9b1c44-e98b-4d4c-8d4c-09226873e9e3/Book/ImmunizationCovid")

xpath = '/html/body/div[@class="view"]/div[@class="view__content"]/div[@class]/div[@id="select-appointment-availability-page-id"]/div[@class="appointment-availability__layout"]/div[@class="b-appointment__content"]/form/div[@class="appointment-availability__content"]/div[@class="appointment-availability__bottom-content"]/div[@class="appointment-availability__right-content"]'

while True:
    time.sleep(2)
    driver.refresh() 
    
    try:
        """div = driver.find_element_by_xpath(xpath)
        print(div)"""
    except KeyboardInterrupt:
        quit()
        



