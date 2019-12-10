from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

##path of chromedriver file. please change to path where chromedriver.exe file exits
driver = webdriver.Chrome("C:\\Users\\ac30243\\AppData\\Local\\Programs\\Python\\Python38-32\\chromedriver.exe")

## calling the browser to create incident page
driver.get("https://mysupportdesk.service-now.com/incident.do?sys_id=-1&sysparm_query=active=true&sysparm_stack=incident_list.do?sysparm_query=active=true")


##Search for the ticket
tixnum = driver.find_element_by_id("sysparm_search")
tixnum.send_keys("INC2305756")
tixnum.send_keys(Keys.RETURN)
time.sleep(4)

driver.switch_to.frame("gsft_main")

time.sleep(10)

#State
sta = Select(driver.find_element_by_id("incident.state"))
sta.select_by_value("3")

time.sleep(5)


#Close reason
rea = Select(driver.find_element_by_id("incident.close_code"))
rea.select_by_value("Solved Remotely (Work Around)")

#Closure Information
#cloinfo = driver.find_element_by_id("section_tab.992099dd0a0006413c77c9a4b7d410c0")
#cloinfo.send_keys(Keys.RETURN)

#closenotes = driver.find_element_by_id("incident.close_notes")
#closenotes.send_keys("Solved")

