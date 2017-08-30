#改编了一下这里的20题如下：登陆中国联通网上营业厅 后选择「自助服务」-->「查询」-->「账户余额」，然后输出手机号码和可用额度。
# 参考 http://www.cnblogs.com/LanTianYou/p/6432953.html


from selenium import webdriver
import selenium.webdriver.support.ui as ui
def login_query_10010(username,pwd):
    print(username,pwd)
    driver=webdriver.PhantomJS()#需要安装PhantomJS，安装方法参考http://www.cnblogs.com/LanTianYou/p/5578621.html
    driver.get('http://iservice.10010.com/e4/')
    wait=ui.WebDriverWait(driver,30)
    login_frame=driver.find_element_by_xpath('html/body/div[5]/div[1]/iframe')
    driver.switch_to_frame(login_frame);
    wait.until(lambda dr:dr.find_element_by_id('userName').is_displayed())
    driver.find_element_by_id('userName').send_keys(username)
    driver.find_element_by_id('userPwd').send_keys(pwd)
    driver.find_element_by_id('login1').click()
    driver.switch_to_default_content()
    wait.until(lambda dr:dr.find_element_by_id('menu_query').is_displayed())
    driver.find_element_by_id('menu_query').click()
    wait.until(lambda dr:dr.find_element_by_id('000100010002').is_displayed())
    driver.find_element_by_id('000100010002').click()
    wait.until(lambda dr:dr.find_element_by_xpath(".//*[@id='loadPage']/iframe").is_displayed())
    account_info_frame=driver.find_element_by_xpath(".//*[@id='loadPage']/iframe")
    driver.switch_to_frame(account_info_frame)
    wait.until(lambda dr:dr.find_element_by_id('userInfoContent').is_displayed())
    wait.until(lambda dr:dr.find_element_by_xpath(".//*[@id='userInfoContent']/dl[3]/dd").is_displayed())
    pthone_number=driver.find_element_by_xpath(".//*[@id='userInfoContent']/dl[3]/dd").text
    print('电话号码：'+pthone_number)
    wait.until(lambda dr:dr.find_element_by_xpath(".//*[@id='userInfoContent']/dl[4]/dd").is_displayed())
    available_amount=driver.find_element_by_xpath(".//*[@id='userInfoContent']/dl[4]/dd").text
    print('可用余额为:'+available_amount)

if __name__=='__main__':
    login_query_10010('186********','********')
