import codecs
import time
import webbrowser
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
# Options for headless and to circumvent captchas
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
a=open("account.txt","r")
lines=a.readlines()
username=lines[0]
password=lines[1]
a.close()

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.binary_location = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
driver_path: str = r'D:\Programs\BrowserDriver\chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
driver.get("https://www.mintos.com/de/login")
a=open("account.txt", "r")
lines=a.readlines()
username=lines[0]
password=lines[1]
inputElement_user = driver.find_element_by_id("login-username")
inputElement_user.send_keys(username)
inputElement_pw = driver.find_element_by_id("login-password")
inputElement_pw.send_keys(password)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/div[3]/button/span').click()
time.sleep(5)
kontostand= driver.find_element_by_xpath('//*[@id="mintos-boxes"]/li[1]').text
Rendite= driver.find_element_by_xpath('//*[@id="mintos-boxes"]/li[2]').text
Invest= driver.find_element_by_xpath('//*[@id="mintos-boxes"]/li[3]').text
driver.close()
with codecs.open('C:/Users/fabia/PycharmProjects/Mint.txt', 'w', "utf-8-sig") as f:
    # Uhrzeit und Liste in Txt speichern
    f.write(kontostand+'\n')
    f.write(Rendite+'\n')
    f.write(Invest+'\n')
    print(kontostand + '\n' + Rendite + '\n' + Invest)
    f.close()
    a.close()
    f.open("C:/Users/fabia/PycharmProjects/Mint.txt")
