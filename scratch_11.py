
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pyautogui

# Properly initialize the Firefox WebDriver using the Service class
fire_fox = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

fire_fox.get('https://www.google.com')
fire_fox.implicitly_wait(5)
pyautogui.typewrite("Islam Way")
pyautogui.press('enter')
