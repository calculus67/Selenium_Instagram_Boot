from ast import YieldFrom
from time import time
from InstagramInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Instagram:
    def __init__(self,email,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login")
        time.sleep(3)
        usernameInput=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        self.browser.find_element_by_xpath("//*[@id='mount_0_0_oe']/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div").click()
        time.sleep(2)





instagram =Instagram(username,password)
instagram.signIn()
instagram.getFollowers()




