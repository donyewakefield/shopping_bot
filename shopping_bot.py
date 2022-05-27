#Description: A program that collects data from websites
from selenium import webdriver #webdriver is used to interact with the browswer
from selenium.webdriver.common.keys import Keys #Keys are the phyisical key commands on the keyboard
from selenium.webdriver.support.ui import Select #This imports a module that helps select actual items on the page

def main():
    # Have user enter its credentials
    email = input("Please enter your email:")
    password = input("Please enter your password: ")

    # Have user enter what they want to search for
    search = input("Please enter what you want to search for on Amazon: ")
    while search == "": #Until user enters something, keep asking
        print(" ")
        print("You have not entered anything.")
        print(" ")
        search = input("Please enter what you want to search for on Amazon: ")

    # Construct driver
    PATH = r"C:\Users\DonyeWakefield\Desktop\Coding\drivers\chromedriver.exe" #Find out where our chromedriver is located (We do this after we installed it)
    driver = webdriver.Chrome(PATH) #webdriver objct and use Chrome method, which contains an argument PATH. Therefore I create Chrome webdriver and store in driver
    driver.implicitly_wait(300) #tell the driver to wait for 2 minutes before closing the interactive connection with the browser

    # Access a website and search
    amazon = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Dmarvel%2Bselect%2Bcarnage%26crid%3D1D72ZRB8ZYYB0%26sprefix%3Dmarvel%2Bselect%2Bcarna%252Caps%252C311%26ref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"

    driver.get(amazon) #use access member function get(string) on driver and this will allow us to access the website

    # insert credentials
    elem = driver.find_element_by_id("ap_email")
    elem.clear()
    elem.send_keys(email) #enter these keys
    elem.send_keys(Keys.RETURN) #Then hit enter to do the search

    elem = driver.find_element_by_id("ap_password")
    elem.clear()
    elem.send_keys(password) #enter these keys
    elem.send_keys(Keys.RETURN) #Then hit enter to do the search

    # insert what user wants to search for
    elem = driver.find_element_by_id("twotabsearchtextbox") #We found the input field
    elem.clear() #clear out the input field
    elem.send_keys(search) #enter these keys
    elem.send_keys(Keys.RETURN) #Then hit enter to do the search

    # Select a item
    # Example of a product (this will have to be generalized for any product)
    elem = driver.find_element_by_link_text('Dynasty Warriors 9 Empires - PlayStation 4')
    elem.click()

    # Buy the item
    #elem = driver.find_element_by_id("buy-now-button")
    #elem.click()
    #elem = find_element_by_name('placeYourOrder1')
    #elem.click()

    # wait and then sleep
    driver.sleep(300)
    driver.close()


    #try:
        #driver.get(yahoo_finance)
        #text_bar = driver.find_element_by_id('yfin-usr-qry')
        #text_bar
    #except:
        #print("oops")

main()
