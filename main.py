from Utils.browser import CreateDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
if __name__ == '__main__':
    drive=CreateDriver(0)
    print(drive.get('https://search.brave.com/search?q=software+development+consultant&source=desktop'))

