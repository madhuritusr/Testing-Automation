# the code chekchs if the website is working properly or not using code nd this process is extremely fast compared to humans checking
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path='./chromedriver.exe')

chrome_browser = webdriver.Chrome(service=service)
chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
# print("Selenium Easy Demo" in chrome_browser.title) - to check whether the correct page is opened up by chckin title of the page in the tab
assert "Selenium Easy Demo" in chrome_browser.title # will say if its true  or not..if its false then it will show an error, thats wat assert is used for
#syntax of this of how to grab the html attributes in selenium provided in python cheatsheat
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default') # class name-btn default..we r grabbing the class by seeing the HTML
# print(show_message_button.get_attribute("innerHTML")) #we grabbing the inner HTML nd printing the title of the button
assert "Show Message" in chrome_browser.page_source # true or not nd page source is the entire html version of the page

user_message = chrome_browser.find_element(By.ID, "user-message")
user_message.clear() #to clear whatever is in the imput
user_message.send_keys("Glassesssss")
chrome_browser.implicitly_wait(2)
show_message_button.click()
chrome_browser.implicitly_wait(4)
time.sleep(10)
output_message = chrome_browser.find_element(By.ID, "display")
print(output_message.get_attribute("innerHTML"))
assert "Glassesssss" in chrome_browser.page_source
chrome_browser.close()  # to close browser
chrome_browser.quit()  # to quite the driver
#Automation can be used unfairly also in voting contests or a facebook post to give likes or send messages to ur frnds using python or upvoting ur posts
#But websities are smarter they will know when a bot is using and a human...cus no human can do things this fast
#So something like wait helps us to not get detected

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
