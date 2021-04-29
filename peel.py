from selenium import webdriver
import time

PATH = "./chromedriver"

driver = webdriver.Chrome(PATH)
#driver.get("https://peelregion.ca/coronavirus/vaccine/book-appointment/default.asp#18")
driver.get("file:///Users/Adrian/Desktop/telus_health_script/peel_html/peel2.html")

xpath1 = '/html/body/div[@id="content-main"]/div/div[@id="page-acco-1"]/div[1]/div[@id="18"]/div[1]/p[3]/a'
xpath2 = '/html/body/div[@id="content-main"]/div/div[@id="page-acco-1"]/div[1]/div[@id="18"]/div[1]/p[5]/a'
        
try: 
    tag = driver.find_element_by_xpath(xpath1)
    print("a tag found.")
except Exception:
    print("no a tag found.")






 