import unittest
from typing import Tuple

import self
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAlerts(unittest.TestCase):
    ALERT_SELECTOR = (By.XPATH, '//button [@onclick="jsAlert()"]')
    RESULT_SELECTOR = (By.ID, 'result')
    CONFIRM_SELECTOR = (By.CSS_SELECTOR, 'button[onclick="jsConfirm()"]')
    PROMPT_SELECTOR = (By.CSS_SELECTOR, 'button[onclick="jsPrompt()"]')

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
        expected_text = 'You successfully clicked an alert'
        self.assertEqual(result_text, expected_text, "Result not matched")

    def testJsConfirmCancel(self):
        self.driver.find_element(*self.CONFIRM_SELECTOR).click()
        js_alert = self.driver.switch_to.alert
        js_alert.dismiss()
        result_text = self.driver.find_element(*self.RESULT_SELECTOR).text
        expected_text = 'You clicked: Cancel'
        self.assertEqual(result_text, expected_text, "Result not matched")

    def testJsPrompt(self):
        sent_text = 'TestTest'
        self.driver.find_element(*self.PROMPT_SELECTOR).click()
        js_alert = self.driver.switch_to.alert
        js_alert.send_keys(sent_text)
        js_alert.accept()
        result_text = self.driver.find_element(*self.RESULT_SELECTOR).text
        expected_text = f'You entered: {sent_text}'
        self.assertEqual(result_text, expected_text, "Result not matched")




