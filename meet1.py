from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
webdriver = webdriver.Chrome(options=chrome_options)
webdriver.maximize_window()

time.sleep(1)

webdriver.get('https://teams.microsoft.com/?lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school//?ctx=teamsGrid')

time.sleep(1)

webdriver.find_element_by_xpath("//*[@id='i0116']").send_keys('aman3672.be20@chitkara.edu.in')

time.sleep(1)

webdriver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input").click()

time.sleep(1)

webdriver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input").send_keys('12345#Arora')

time.sleep(1)

webdriver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input").click()

time.sleep(1)

webdriver.find_element_by_xpath("/html/body/div/form/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input").click()

time.sleep(10)

webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/left-rail/div/div/school-app-left-rail/channel-list/div/div[1]/ul/li[1]/ul/li[3]/div/h3/a/div[1]/div/span').click()

time.sleep(2)

webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/middle-messages-stripe/div/messages-header/div[2]/div/message-pane/div/div[1]/div/div/calling-persistent-indicator/div/div/div/ul/li/calling-persistent-indicator-item/div/div/calling-join-button/button').click()

time.sleep(2)

webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]').click()

time.sleep(2)

webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button').click()