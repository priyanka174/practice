from Library import readdata
class readdata2:
    def __init__(self, obj):
        global driver
        driver=obj

    def username(self,username):
        driver.find_element_by_name(readdata.configdata1('Elementsdata', 'username')).send_keys("priya")

    def email(self,email):
        driver.find_element_by_name(readdata.configdata1('Elementsdata', 'email')).send_keys("priya@gmail.com")

    def password(self,password):
        driver.find_element_by_name(readdata.readdata2('Elementsdata', 'password')).send_keys("12344566")
    def cpassword(self,cpassword):
        driver.find_element_by_name(readdata.readdata2('Elementsdata', 'cpassword')).send_keys("12345678")