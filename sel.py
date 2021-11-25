from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

log = 'andrey'
pas = 'qryuoixcnnmkds'


class TestCreateFolder:
    def test_sel(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')

        driver = webdriver.Chrome()
        driver.get('https://passport.yandex.ru/auth')
        el = driver.find_element(By.NAME, 'login')
        el.send_keys(log)
        time.sleep(2)
        el.send_keys(Keys.ENTER)
        time.sleep(2)

        el2 = driver.find_element(By.ID, 'passp-field-passwd')
        el2.send_keys(pas)
        time.sleep(2)
        el2.send_keys(Keys.ENTER)
        time.sleep(2)
        assert 'Неверный пароль' not in driver.page_source

        driver.close()
        driver.quit()



