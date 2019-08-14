import unittest
from appium import webdriver
from visual_elements import VisualElements
import os
directory = os.getcwd()

DESIRED_CAPS = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'Pixel',
    'app': directory+'/content/Saavn.apk'
}


class AppiumTestCase(unittest.TestCase):

    def setUp(self):
        if DESIRED_CAPS is None or len(DESIRED_CAPS) == 0:
            raise Exception('desired_caps has not been defined')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', DESIRED_CAPS)
        print(self.driver.desired_capabilities)
        self.visualElements = VisualElements(self.driver)

    def tearDown(self):
        self.driver.quit()
