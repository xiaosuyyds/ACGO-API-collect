# Access-Token
> 由于逆向登录的跨站token(Csrf-Token)过于复杂，我们另辟蹊径，模拟浏览器操作，获取登陆的cookie

### 代码
```python
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def refresh_cookie(number, password):
    print('正在启动浏览器')
    if sys.platform == 'linux':
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
    elif sys.platform == 'win32' or sys.platform == 'cygwin':
        driver = webdriver.Chrome()
    else:
        print("未知系统，可能会遇到问题，请自行解决")
        driver = webdriver.Chrome()

    driver.delete_all_cookies()

    print('正在打开网页')
    driver.get("https://www.acgo.cn/discuss")

    driver.implicitly_wait(0.5)
    
    print('正在点击发起讨论')

    elements = driver.find_elements(by=By.TAG_NAME, value="button")
    for element in elements:
        if element.text == "发起讨论":
            element.click()
            break

    driver.implicitly_wait(3)
    print('正在登录')
    # 登录界面
    login = driver.find_element(by=By.CLASS_NAME, value="login-form")
    inputs = login.find_element(by=By.CLASS_NAME, value="form_wrap")
    print('正在输入账号密码')
    # 输账号&密码
    element = inputs.find_element(by=By.ID, value="username")
    element.send_keys(number)
    driver.implicitly_wait(0.5)
    element = inputs.find_element(by=By.ID, value="pwd")
    element.send_keys(password)
    driver.implicitly_wait(2)
    # 点同意协议
    print('正在同意用户协议')
    element = login.find_element(by=By.CLASS_NAME, value="xmloginant-checkbox-input")
    element.click()
    driver.implicitly_wait(2)
    print('正在点击登录按钮')
    # 登录！
    element = login.find_element(by=By.ID, value="login")
    element.click()

    driver.implicitly_wait(3)
    time.sleep(1.5)

    cookie = driver.get_cookie('user_token')

    driver.quit()

    if cookie:
        print(f'登录成功 cookie: {cookie.get("value")}')
        return cookie.get('value')
    else:
        print('登录失败')
        return None


if __name__ == '__main__':
    number, password = input("请输入账号: "), input("请输入密码: ")
    refresh_cookie(number, password)
```

### 依赖库
```text
selenium
```

### 注意事项
1. 如果系统中没有Chrome浏览器，请自行安装，[传送门](https://developer.chrome.com/docs/chromedriver/downloads?hl=zh-cn)
2. 如果运行时报错，请根据[selenium文档](https://www.selenium.dev/zh-cn/documentation)与错误信息自行解决
3. ***⚠️此代码仅供学习交流，请勿用于非法用途，否则后果自负⚠️***