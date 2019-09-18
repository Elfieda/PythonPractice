import unittest, time, os
from appium import webdriver
from time import sleep

class Android_ATP_WTA(unittest.TestCase):
    "Class to run tests against the ATP WTA app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '$ Your device name'
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'in.hipbar.hipbar_pay_app'
        desired_caps['appActivity'] = '.ui.activities.SplashScreenActivity'
        # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
#        desired_caps['appWaitActivity'] = '.ui.activities.*'
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_atp_wta(self):
        "Testing the ATP WTA app "
        self.driver.implicitly_wait(5)
        
        menubar = self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='in.hipbar.hipbar_pay_app:id/btn_agree_contine']")
        menubar.click()
        time.sleep(1)

    
        singles = self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='in.hipbar.hipbar_pay_app:id/btn_gold_next']")
        singles.click()
        time.sleep(1)


        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView").click()
        time.sleep(2)

        #Entering the mobile number and cliking next
        self.driver.find_element_by_id("in.hipbar.hipbar_pay_app:id/et_enter_number").send_keys("9789702255")
        self.driver.find_element_by_id("in.hipbar.hipbar_pay_app:id/btn_next").click()
        time.sleep(2)

        #Clicking on Onboarding Screen
        self.driver.find_element_by_id("in.hipbar.hipbar_pay_app:id/tv_on_boarding").click()
        time.sleep(3)

        #Clicking on more tabs
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc="MORE"]/android.widget.ImageView").click()






#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_ATP_WTA)
    unittest.TextTestRunner(verbosity=2).run(suite)

