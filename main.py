from selenium import webdriver
import time

# wifi Auto login
if __name__ == '__main__':

    username = open("username", "r").read().replace('\n', '')  # Enter Your Wifi Username
    password = open("password", "r").read().replace('\n', '')  # Enter Your Wifi password

    url = 'http://192.168.20.254:1000/login?'  # Wifi Login URL

    # for Safari
    driver = webdriver.Safari()
    # driver = webdriver.Chrome('your_path')

    # URL with token examples
    # http://192.168.20.254:1000/keepalive?0f0d0d060f2b8310
    # http://192.168.20.254:1000/login?01674a0b0f9b0ef5
    # http://192.168.20.254:1000/keepalive?f5fdf2f9fef0fcf6
    # http://192.168.20.254:1000/login?0068450a96e49fa4
    # http://192.168.20.254:1000/logout?f0fcf4fef9f5f9f7

    driver.get(url)
    time.sleep(0.2)
    try:
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr[4]/td/input[2]').click()
    except:
        driver.refresh()
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr[4]/td/input[2]').click()

    print("Login Succeed")

