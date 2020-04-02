from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

save_path = 'D:\\project\\python\\test\\file\\'
class Hue():
    def __init__(self, url, user, password, path):
        self.url = url
        self.user = user
        self.password = password
        self.path = path
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': save_path}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(executable_path=self.path, chrome_options=options)

    def login(self):

        self.driver.get(self.url)
        self.driver.find_element_by_id("id_username").send_keys(self.user)
        self.driver.find_element_by_id("id_password").send_keys(self.password)
        self.driver.find_element_by_class_name("btn.btn-primary").click()

    def sql_query(self, sql):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div[2]/div[2]/div[4]/div[1]/span/span/div[5]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/textarea')))
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[4]/div[1]/span/span/div[5]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/textarea') \
            .send_keys(sql)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[4]/div[1]/span/span/div[5]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/textarea') \
            .send_keys(Keys.CONTROL, Keys.ENTER)
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                              'inactive-action.dropdown-toggle.pointer.snippet-side-btn')))
        time.sleep(5)

    def download(self):

        self.driver.find_element_by_class_name("inactive-action.dropdown-toggle.pointer.snippet-side-btn").click()

        time.sleep(5)
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                              'download')))
        self.driver.find_element_by_class_name(
            'download').click()


if __name__ == '__main__':
    hue = Hue('hue path',
              'user_name',
              'password',
              'D:\\******\\chromedriver.exe')
    print(hue.url, hue.user, hue.password)
    hue.login()
    hue.sql_query("********")
    hue.download()
    # 显示所有列
    pd.set_option('display.max_columns', None)

    file_name = os.listdir(save_path)[0]
    file_path = save_path+file_name
    data = pd.read_csv(file_path)

    print(data)

