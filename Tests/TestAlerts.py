import unittest
from typing import Tuple

import self
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAlerts(unittest.TestCase):
    ALERT_SELECTOR = (By.XPATH, '//button [@onclick="jsAlert()"]')
    RESULT_SELECTOR = (By.ID, 'result')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def testAlertOk(self):
        self.driver.find_element(*self.ALERT_SELECTOR).click()
        js_alert = self.driver.switch_to.alert
        js_alert.accept()
        result_text = self.driver.find_element(*self.RESULT_SELECTOR).text
        print(result_text)
        expected_text = 'You successfully clicked an alert'
        self.assertEqual(result_text, expected_text, "Result not matched")
