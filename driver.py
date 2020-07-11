from utils.utils import calculate_time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    @calculate_time
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--headless")

    def prepare(self, driver_path):
        return webdriver.Chrome(options=self.chrome_options,
                                executable_path=driver_path)
    