'''from selenium.webdriver import Chrome
from Library import readdata
def startbrowser():
    global driver
    path="C:/Users/User/PycharmProjects/practice21/drivers1/chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.maximize_window()
    driver.get(readdata.readdata1('info', 'Application_url'))
    return driver

def close():
    driver.close()'''

from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import readdata
def startbrowser():
    global driver
    if((readdata.configdata('info', 'Browser'))=='Chrome'):

        path="C:/Users/User/PycharmProjects/practice21/drivers1/chromedriver.exe"
        driver=Chrome(executable_path=path)
    else:
        path="C:/Users/User/PycharmProjects/practice21/drivers1/geckodriver-v0.26.0-win64 (1)/geckodriver.exe"
        driver=Firefox(executable_path=path)
    driver.maximize_window()
    driver.get(readdata.configdata('info', 'Application_url'))
    return driver

def closebrowser():
    driver.close()


