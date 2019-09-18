import unittest
import time
import os
from appium import webdriver
from time import sleep


class Android_ATP_WTA(unittest.TestCase):
            "Class to run tests against the ATP WTA app"

            def setUp(self):
                "Setup for the test"
                desired_caps = {}
                desired_caps['platformName'] = 'Android'
                desired_caps['platformVersion'] = '8.1.0'
                desired_caps['deviceName'] = '$ Your device name'
                # Since the app is already installed launching it using package and activity name
                desired_caps['appPackage'] = 'in.hipbar.hipbar_pay_app'
                desired_caps['appActivity'] = '.ui.activities.SplashScreenActivity'
                # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
        #        desired_caps['appWaitActivity'] = '.ui.activities.*'
                self.driver = webdriver.Remote(
                    'http://0.0.0.0:4723/wd/hub', desired_caps)

            def tearDown(self):
                "Tear down the test"
                self.driver.quit()

            def test_atp_wta(self):
                "Testing the ATP WTA app "
                self.driver.implicitly_wait(5)
                # click on Navigation Bar MainMenu by finding element by xpath
                menubar = self.driver.find_element_by_xpath(
                    "//android.widget.Button[@resource-id='in.hipbar.hipbar_pay_app:id/btn_agree_contine']")
                menubar.click()
                time.sleep(5)

                # From list of options available click on Rankings by finding element using uiautomator
        #        rankings = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Rankings")')
        #        rankings.click()

                # click on ATP Singles by finding element using id
                singles = self.driver.find_element_by_xpath(
                    "//android.widget.Button[@resource-id='in.hipbar.hipbar_pay_app:id/btn_gold_next']")
                singles.click()
                time.sleep(5)
                # Assert that Novak Djokovic is the top listed player
         #       elmnt = self.driver.find_element_by_id('atpwta.live:id/Player1TV')
         #       self.assertEqual('Novak Djokovic', elmnt.get_attribute('text'))
         #       print elmnt.get_attribute('text')
