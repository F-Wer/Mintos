import codecs
import os
import smtplib
import ssl
import time

from selenium import webdriver

from secret import *


class scrape_Mintos(object):
    def Scrape(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        # Options for headless and to circumvent captchas
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.binary_location = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
        print('Opening Chrome')
        driver_path: str = r'D:\Python\webdriver\chromedriver.exe'
        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
        driver.get("https://www.mintos.com/de/login")
        inputElement_user = driver.find_element_by_id("login-username")
        inputElement_user.send_keys(username)
        inputElement_pw = driver.find_element_by_id("login-password")
        inputElement_pw.send_keys(password)
        print('login at Site')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/div[3]/button/span').click()
        time.sleep(5)
        kontostand = driver.find_element_by_xpath('//*[@id="mintos-boxes"]/li[1]').text
        Rendite = driver.find_element_by_xpath('//*[@id="mintos-boxes"]/li[2]').text
        Invest = driver.find_element_by_xpath('//*[@id="mintos-boxes"]/li[3]').text
        driver.close()
        s_loc = 'D:/Python/webdriver/Mint.txt'
        with codecs.open(s_loc, 'w', "utf-8-sig") as f:
            # Uhrzeit und Liste in Txt speichern
            f.write(kontostand + '\n')
            f.write(Rendite + '\n')
            f.write(Invest + '\n')
            #   print(kontostand + '\n' + Rendite + '\n' + Invest)
            f.close()
            # a.close()
            os.system(s_loc)

    def Send_Mail(self):
        port = 465  # For SSL
        # Create a secure SSL context
        context = ssl.create_default_context()
        # reading the file in binary mode. Because it is saved as a UTF-8 file and there is a error, if you try to convert it to ASCII
        r = open('D:/Python/webdriver/Mint.txt', "rb+")
        message = r.read()
        # print(message)
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, passwort_g)
            print("Login for E-Mail")
            server.sendmail(sender_email, receiver_email, message)
            print("Email send")


o = scrape_Mintos()
o.Scrape()
o.Send_Mail()
