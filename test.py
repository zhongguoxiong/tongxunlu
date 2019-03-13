from appium import  webdriver
import  time

from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'TEX9K17904908260'
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = '.activities.PeopleActivity'
desired_caps['noReset'] = 'true'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# #print(driver.device_time)
#
# # for i in range(10):
# #     # driver.keyevent(25)
# #     driver.swipe(350, 1020, 350, 930, 100)
# driver.open_notifications()
# time.sleep(3)
# driver.find_element(By.XPATH,"//*[contains(@text,'蓝牙')]").click()
# # miguship=driver.find_element(By.XPATH,"//*[contains(@text,'咪咕视频')]")
# # miguship.click()
#
# print(driver.network_connection)
# driver.set_network_connection(2)
# print(driver.network_connection)
# driver.get_screenshot_as_file("./network.png")
#driver.swipe(100,1196,100,1020,100)
time.sleep(1)
# fjthk=driver.find_element(By.XPATH,"//*[contains(@text,'陈丹丹')]")
# wo=driver.find_element(By.XPATH,"//*[contains(@text,'我')]")
# #driver.scroll(fjthk,wo)
# driver.drag_and_drop(fjthk,wo)
# text_list=driver.find_elements(By.CLASS_NAME,"android.widget.TextView")
# texts=[]
# for i in text_list:
#     for j in range(text_list.__len__()):
#         texts.append(i.text)
#         driver.swipe(350, 1020, 350, 930, 100)

# fjthk=driver.find_element(By.XPATH,"//*[contains(@text,'陈丹丹')]")
print(driver.current_package)
print(driver.current_activity)
# print(fjthk.location)
# driver.background_app(10)

time.sleep(3)
driver.quit()