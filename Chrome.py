from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')


username="aman_jai_2002"
password="amanjaisingh"

username_input=driver.find_element_by_
username_input.send_keys(username)

password_input=driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
password_input.send_keys(password)

loginbutton=driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
loginbutton.click()