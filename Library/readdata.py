''''mport configparser


def readdata1(section, key):
    config=configparser.ConfigParser()
    config.read("C:/Users/User/PycharmProjects/practice21/Configuration/config.cfg")
    return config.get(section, key)
#print(readdata1('info', 'Application_url'))

def readdata2(section,key):
    config=configparser.ConfigParser()
    config.read("C:/Users/User/PycharmProjects/practice21/Configuration/elements.cfg")
    return config.get(section,key)'''



import configparser
def configdata(section, key):
    config=configparser.ConfigParser()
    config.read("C:/Users/User/PycharmProjects/practice21/Configuration/config.cfg")
    return config.get(section, key)
#print(configdata('info', 'Application_url'))

def configdata1(section, key):
    config=configparser.ConfigParser()
    config.read("C:/Users/User/PycharmProjects/practice21/Configuration/elements.cfg")
    return config.get(section,key)
#print(configdata1('Elementsdata','username'))
