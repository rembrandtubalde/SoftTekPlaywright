import time
import string
import random
from playwright.sync_api import Page

class User_Functions:
    def __init__(self, page: Page):
        self.page = page

    def login(self, username: str, password: str):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.page.fill('//input[@name="username"]', username)
        self.page.fill('//input[@name="password"]', password)
        self.page.click('//button[@type="submit"]')

    def fill_user_details(self, first_name: str, middle_name: str, last_name: str, username: str, password: str, confirm_pass: str):
        self.page.click('//a[@class="oxd-main-menu-item"][contains(.,"PIM")]')
        self.page.click('//button[@type="button"][contains(., "Add")]')
        self.page.fill('//input[@name="firstName"]', first_name)
        self.page.fill('//input[@name="middleName"]', middle_name)
        self.page.fill('//input[@name="lastName"]', last_name)
        self.page.click('//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]')
        self.page.fill('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input', username)
        self.page.fill('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input', password)
        self.page.fill('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input', confirm_pass)
        iduser = self.page.input_value('(//input[contains(@class,"oxd-input oxd-input--active")])[5]')
        self.page.click('//button[@type="submit"]')
        return iduser
    def verify_user_creation(self, xpath: str, timeout: int = 30):
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                if self.page.locator(xpath).is_visible():
                    return True
            except TimeoutError:
                pass
            time.sleep(1)
        raise TimeoutError(f"El texto no apareció en {timeout} segundos")

    def verify_employee_information(self, Employee_Id: str):
        self.page.click('//a[@href="/web/index.php/pim/viewPimModule"]')
        self.page.fill('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input', Employee_Id)
        self.page.click('//button[@type="submit"]')
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
    @staticmethod
    def generate_random_letter():
        return random.choice(string.ascii_letters)
