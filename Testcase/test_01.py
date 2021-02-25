'''from selenium.webdriver import Chrome
from Base import Base_01
from Library import readdata
from pages import pages1
def test_data1():
    driver=Base_01.startbrowser()
    register=pages1.readdata2(driver)
    register.username("priya")
    
    register.email("priya@gmail.com")

    driver=Base_01.startbrowser()

def test_data2():
    driver=Base_01.startbrowser()
    reg=pages1.readdata2(driver)
    reg.password("12345")
    reg.cpassword("12345")
    driver = Base_01.close()'''


from selenium.webdriver import Chrome

from Base import Base_01
from Library import readdata
from pages import pages1
def test_data01():

    driver = Base_01.startbrowser()
    reg=pages1.readdata2(driver)
    reg.username("priya")

def test_data02():
    driver = Base_01.startbrowser()

    reg=pages1.readdata2(driver)
    reg.email("priya@123")
    driver = Base_01.closebrowser()


