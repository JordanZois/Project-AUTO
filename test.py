from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Edge driver path
PATH = "D:\CodingSoftware\msedgedriver.exe"


#User desired website (for now, just https://www.footlocker.ca will be used)
website = input("Enter desired website: ")
#Launch calendar url extension
launchCalendar = "/en/release-dates"


#User input to decide if they want the bot to go for a launch calendar product
#or for it to auto check out/check stock on an already launched product
answer = str(input("Would you like to proceed to the Launch Calendar? Enter Y for yes or N for no: "))
proceed="y" or "Y" 


#If statement for users decision
if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:


#Setting up launch calendar url
    website = website+launchCalendar
#User input for desired launch product
    lp = input("Enter desired launch product: ")
#Code to launch microsoft edge, maximize window, and go to specified url
    driver = webdriver.Edge(executable_path = PATH)
    driver.maximize_window()
    driver.get(website)


#Looking for the product specified by user
    launchProducts = driver.find_elements_by_class_name("ProductName")
    

#Initialization of some variables
    t = 0
    count = 0
    numHref = 0
    i = 0


#Finding the index of the user desired product for later use
#FIX t VAL IN HERE
    for c in launchProducts:
       if c.text == lp:
           t = count
           print(lp)
           print(c.text)
       count += 1


#Printing the index
    print(t)


#Code to print out all href urls that are found under the tag a
    continue_link = driver.find_element_by_tag_name('a')
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:


#Printing out each href url, and checking if it is a launch product url or not
        print(elem.get_attribute("href"))
        FS = elem.get_attribute("href")
        SS = "https://www.footlocker.ca/en/release-dates/"


#If statement to let user know if the url is a launch product url 
#or not and storing the amoun of launch urls in numHref for later use
#(exclude all elements not containing https://www.footlocker.ca/en/release-dates/)
        if SS in FS:
            print("Product Found")
            numHref += 1
        else:
            print("Unusable Link")

    print(numHref)


#Setting a list to store all launch product urls
    LaunchURLs = [None] * numHref
    print(LaunchURLs)
    continue_link = driver.find_element_by_tag_name('a')
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        FS = elem.get_attribute("href")
        SS = "https://www.footlocker.ca/en/release-dates/"
        if SS in FS:
            LaunchURLs[i] = FS
            i += 1
    print(LaunchURLs)
    print(count)
    
    #Redirect user to desired launch product page
    print(LaunchURLs[t])
    driver.get(LaunchURLs[t])




#Bring user to desired product to be monitored or purchased
else:
    product = input("Enter desired product: ")
    time.sleep(2)


#Code to open desired website
    driver = webdriver.Edge(executable_path = PATH)
    driver.maximize_window()
    driver.get(website)


#Required code to be able to search for an item on footlocker.com
    search = driver.find_element_by_id("HeaderSearch_search_query")
    search.send_keys(product)
    search.send_keys(Keys.RETURN)


#Code to refine search by gender
    gender = str(input("which category is the product in? (Mens, Womens, Boys, Girls, Kids, etc): "))

    if gender in ['mens', 'Mens']:
        mens = driver.find_element_by_id("gender1")
        mens.click()
    else:
        if gender in ['womens', 'Womens']:
            womens = driver.find_element_by_id("gender1")
            womens.click()
        else:
            if gender in ['boys', 'Boys']:
                boys = driver.find_element_by_id("gender1")
                boys.click()
            else:
                if gender in ['girls', 'Girls']:
                    girls = driver.find_element_by_id("gender1")
                    girls.click()
                else:
                    if gender in ['kids', 'Kids']:
                        kids = driver.find_element_by_id("gender1")
                        kids.click()

#Code needed to go to desired product



#Code to add any/a specific size of product to cart



#Code to go to cart
