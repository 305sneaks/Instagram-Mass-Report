from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random
import urllib2

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('Macintosh HD/Applications/Firefox.app')
driver = webdriver.Firefox(firefox_binary=binary, proxy=proxy)

# Read a random proxy from the 'proxy.txt' file
with open('proxy.txt', 'r') as f:
    lines = f.readlines()
    if not lines:
        print("proxy.txt file is empty or not found.")
    else:
        proxy_ip, proxy_port = random.choice(lines).strip().split(':')
        proxy = Proxy({
                      'proxyType': ProxyType.MANUAL,
                      'httpProxy': "{}:{}".format(proxy_ip, proxy_port),
                      'ftpProxy': "{}:{}".format(proxy_ip, proxy_port),
                      'sslProxy': "{}:{}".format(proxy_ip, proxy_port),
                      'noProxy': ''
                      })



# Select a random proxy from proxy.txt
with open('proxy.txt', 'r') as f:
    lines = f.readlines()
    if not lines:
        print("proxy.txt file is empty or not found.")
    else:
        proxy_ip, proxy_port = random.choice(lines).strip().split(':')

proxy = Proxy({
              'proxyType': ProxyType.MANUAL,
              'httpProxy': "{}:{}".format(proxy_ip, proxy_port),
              'ftpProxy': "{}:{}".format(proxy_ip, proxy_port),
              'sslProxy': "{}:{}".format(proxy_ip, proxy_port),
              'noProxy': ''
              })


# Open a web browser and navigate to Instagram's login page
driver = webdriver.Firefox(proxy=proxy)
driver.get('https://www.instagram.com/accounts/login/')

# Select a random account from acc.txt
with open('acc.txt', 'r') as f:
    lines = f.readlines()
    if not lines:
        print("acc.txt file is empty or not found.")
    else:
        account = random.choice(lines).strip()
        if ':' not in account:
            print("Line {} is not formatted correctly.".format(account))
        else:
            username, password = account.split(':')

# Find the input fields and fill them out
username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")
username_input.send_keys(username)
password_input.send_keys(password)

# Submit the form to log in
password_input.submit()

# Navigate to the page to report a profile
driver.get('https://help.instagram.com/contact/383679321740945')

# Fill out the form with the user's input
yesno_input = driver.find_element_by_name("yesno")
violation_location_input = driver.find_element_by_name("violation_location")
violation_type_input = driver.find_element_by_name("violation_type")
yesno_input.send_keys('no')
violation_location_input.send_keys('an entire profile')
violation_type_input.send_keys('Nudity or pornography')

username_to_report = input("Enter the username of the person you are reporting: ")
username_to_report_input = driver.find_element_by_name("username_to_report")
username_to_report_input.send_keys(username_to_report)
username_to_report_input
