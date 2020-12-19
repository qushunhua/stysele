from selenium import webdriver
import yaml
import time

def get_cookies():
    opt=webdriver.ChromeOptions()
    opt.debugger_address="127.0.0.1:9222"
    driver=webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    cookies=driver.get_cookies()
    return cookies
def set_cookies():
    cookies=get_cookies()
    with open("datas.yml",'w',encoding='UTF-8') as f:
        yaml.safe_dump(cookies,f)

class Test_wx():
    def loging(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("datas.yml",encoding="UTF-8") as f:
            datas=yaml.safe_load(f)
        for cookie in datas:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def test_addcon(self):
        self.loging()
        # // *[ @ id = "member_list"] / tr / td[1] / input
        # // *[ @ id = "menu_contacts"] / span
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('// *[ @ id = "member_list"] / tr / td[1] / input').click()
        time.sleep(2)
        # // *[ @ id = "member_list"] / tr / td[6] / div / a
        self.driver.find_element_by_xpath('// *[ @ id = "member_list"] / tr / td[6] / div / a').click()
        time.sleep(6)

        # // *[ @ id = "__dialog__MNDialog__"] / div / div[3] / a[1]
        self.driver.find_element_by_xpath('// *[ @ id = "__dialog__MNDialog__"] / div / div[3] / a[1]').click()
        assert self.driver.find_element_by_xpath('//*[@id="js_tips"]').text=='已发送邀请'
        time.sleep(3)



if __name__ == '__main__':
    set_cookies()

