from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('enviroment/chromedriver', options=chrome_options)
driver.get('https://www.baidu.com')

print(driver.title)

driver.quit()
