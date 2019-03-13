import yaml
from appium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from read_data import test_readdata
import pytest
import sys, os
sys.path.append(os.getcwd())


def readdatas():
    user_list = []
    user_data = test_readdata().get("User")
    for i in user_data.keys():
        user_list.append(
            (i, user_data.get(i).get('name'), user_data.get(i).get('phone'), user_data.get(i).get('expect')))
    return user_list
class TongxunluClass:
        def setup_class(self):
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '7.0'
            desired_caps['deviceName'] = 'TEX9K17904908260'
            desired_caps['appPackage'] = 'com.android.contacts'
            desired_caps['appActivity'] = '.activities.PeopleActivity'
            desired_caps['noReset'] = 'true'
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True

            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.newlianxirenbtn=(By.ID,"com.android.contacts:id/menu_add_contact")
            self.selectzhanghu=(By.XPATH,"//*[contains(@text,'手机')]")
            self.name=(By.XPATH,"//*[contains(@text,'姓名')]")
            self.phone=(By.XPATH,"//*[contains(@text,'电话号码')]")
            self.queren=(By.ID,"android:id/icon2")ls
            self.backbtn=(By.ID,"com.android.contacts:id/backImg")
            self.usertext=(By.CLASS_NAME,"android.widget.TextView")
            self.search_btn=(By.ID,"com.android.contacts:id/search_view")
            self.clickimagebtn=(By.ID,"com.android.contacts:id/frame_pressed")
            self.fromtufu=(By.XPATH,"//*[contains(@text,'从图库中选择')]")
        def position_ele(self,elem):
            return  WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
                    lambda x: x.find_element(*elem)
            )

        def position_ele_list(self,elem):
            return WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
                lambda x: x.find_elements(*elem)
            )

        def click_ele(self,elem):
           ele=self.position_ele(elem)
           ele.click()

        def input_text(self,elem,text):
            el_text = self.position_ele(elem)
            el_text.clear()
            el_text.send_keys(text)

        # def test_get_user_list(self):
        #     self.driver.swipe(350, 1200, 350, 300,2000)
        #     # user_list=[]
        #     # users=self.position_ele_list(self.usertext)
        #     #
        #     # for i in users:
        #     #
        #     #     user_list.append(i.text)
        #     #
        #     # return user_list
        #     # print(user_list)
        # def if_disp(self,elem):
        #     try:
        #         self.position_ele(self.newlianxirenbtn,self.search_btn)
        #         return True
        #     except Exception as e:
        #         return False
        @pytest.mark.parametrize("num,username,userphone,expect",readdatas())
        def test_clicknewlianxiren(self,num,username,userphone,expect):

            self.click_ele(self.newlianxirenbtn)
            # self.click_ele(self.selectzhanghu)
            print(num)
            self.input_text(self.name, username)
            self.input_text(self.phone,userphone)
            self.click_ele(self.clickimagebtn)
            self.click_ele(self.fromtufu)
            self.click_ele(self.queren)

            self.click_ele(self.backbtn)


        def teardown_class(self):

            self.driver.quit()



