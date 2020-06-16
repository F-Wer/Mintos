import codecs
import smtplib
import ssl
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename

from selenium import webdriver

from secret import *


class ScrapeMintos(object):
    def scrape(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        # Options for headless and to circumvent captchas
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        print('Opening Chrome')
        driver = webdriver.Chrome(options=options,executable_path=r'D:\Python\webdriver\chromedriver.exe')
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
           # os.system(s_loc)

    def smail(self):
        print('Function Send_Mail')
        port = 465  # For SSL
        # Create a secure SSL context
        context = ssl.create_default_context()
        # reading the file in binary mode. Because it is saved as a UTF-8 file and there is a error, if you try to convert it to ASCII
        r = open('D:/Python/webdriver/Mint.txt',encoding='utf-8')
        files = ['D:/Python/webdriver/Mint.txt']
        msg = MIMEMultipart()
        message = MIMEText(r.read())
        msg.attach(message)
        for f in files:
            with open(f, "rb") as file:
                part = MIMEApplication(
                    file.read(),
                    Name=basename(f)
                )
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)
        msg['Subject'] = 'Mintos'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        # print(message)
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, passwort_g)
            print("Login for E-Mail")
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email send")


o = ScrapeMintos()
o.smail()
