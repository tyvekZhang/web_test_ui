from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from base.base_page import BasePage


class Design(BasePage):
    url = 'http://10.101.4.25/'
    def query_target_result(self):
        cas = (By.XPATH,'//*[@id="root"]/div/section/div[2]/main/div/div/div/div/form/div[1]/div[2]/div/div/div/div')
        self.click(cas)
        cas_option = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]')
        self.wait(0.5)
        self.click(cas_option)
        taxPk = (By.ID, 'taxPk')
        self.click(taxPk)
        self.wait(0.5)
        tax_ancestor_fir_pos = (By.XPATH, '/html/body/div[3]/div/div/div/div/ul[1]/li[1]/div[1]')
        tax_ancestor_fir = self.locator(tax_ancestor_fir_pos)
        action = ActionChains(self.driver)
        action.move_to_element(tax_ancestor_fir)
        action.perform()
        self.wait(0.5)
        tax_ancestor_sec_pos = (By.XPATH, '/html/body/div[3]/div/div/div/div/ul[2]/li[1]/div[1]')
        tax_ancestor_sec = self.locator(tax_ancestor_sec_pos)
        action.move_to_element(tax_ancestor_sec)
        action.perform()
        self.wait(0.5)
        tax_ancestor_third_pos = (By.XPATH, '/html/body/div[3]/div/div/div/div/ul[3]/li[1]/div')
        self.click(tax_ancestor_third_pos)
        query_button = (By.XPATH, '//*[@id="root"]/div/section/div[2]/main/div/div/div/div/form/div[4]/div/div/div/button/span')
        self.click(query_button)
        self.wait(10)
        self.driver.close()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    indexScreen = Design(driver)
    indexScreen.open()
    driver.maximize_window()
    indexScreen.query_target_result()
