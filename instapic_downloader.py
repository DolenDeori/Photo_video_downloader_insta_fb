from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import webbrowser
import pip
try:
    import matplotlib
except:
    pip.main(['install' , "matplotlib"])

url = 'https://www.instagram.com/p/CRY9PR7nBDo/?utm_source=ig_web_copy_link'

chrome_options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
chrome_options.headless = True
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)

soup = BeautifulSoup(driver.page_source , features="html5lib")

image = soup.find('meta' , property = 'og:video')
image = soup.find('meta' , property = 'og:image')

image_url = image['content']
webbrowser.open(image_url , new=0 , autoraise=True)