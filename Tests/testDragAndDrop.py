import time
import unittest
from typing import Tuple

import self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class TestDragAndDrop(unittest.TestCase):
    DRAG_SELECTOR = (By.CSS_SELECTOR, '#column-a')
    DROP_SELECTOR = (By.CSS_SELECTOR, '#column-b')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def testDragAndDrop(self):
        action = ActionChains(self.driver)
        drag_element = self.driver.find_element(*self.DRAG_SELECTOR)
        drop_element = self.driver.find_element(*self.DROP_SELECTOR)
        action.drag_and_drop(drag_element, drop_element).perform()
        print(drag_element.text)
        print(drop_element.text)
        self.assertEqual(drag_element.text, 'B')
        time.sleep(5)



