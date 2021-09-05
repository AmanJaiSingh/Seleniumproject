from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fwww.google.com%2F&_ga=2.73969618.1729295755.1615401744-865914429.1615401744&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('chhavi3644.be20@chitkara.edu.in')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys('Engineerchd2001')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()
time.sleep(3)
driver.get('https://meet.google.com/dqp-rqiw-wkh')
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/div[3]/div/span/span').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
