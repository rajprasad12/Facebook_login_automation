######### AUTHOR : RAJ PRASAD KUIRI #########
######### email id: prasadraj954@gmail.com ########

from selenium import webdriver
driver=webdriver.Chrome(executable_path="G:\\webdriver\\chromedriver.exe")
driver.get("https://www.facebook.com")
driver.find_element_by_name("email").send_keys("prasadraj954@gmail.com")
driver.find_element_by_name("pass").send_keys("rajprasad123")
driver.find_element_by_id("loginbutton").click()
