from selenium import webdriver
from selenium_stealth import stealth
from Resource import PathResource as path
import os
from dotenv import load_dotenv
from Helpers.errorhandler import handle_error

load_dotenv()


class CreateDriver:
    def __new__(cls, flag: bool):
        try:
            PATH = path.resource_path(os.environ.get('DRIVERPATH') + "chromedriver.exe")
            print(PATH)
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/90.0.4430.212 Safari/537.36")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument("--user-data-dir=" + path.resource_path(os.environ.get('USER_DATA')))

            if not flag: options.add_argument('--headless')
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(PATH, options=options)
            stealth(driver,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="Win64",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                    )

            return driver

        except Exception as e:
            handle_error.update_error(e)
