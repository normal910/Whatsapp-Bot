path = 'C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver.exe' #Path to the ChromeDriver executable

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(path)
driver.get("https://web.whatsapp.com/")

input("Press anything after QR scan")
#you can set a sleep if requierd
time.sleep(5)


names = ["Admin"] #Your Chat goes there <-

for name in names:

    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    person.click()

    for i in range(1,3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    msg_got = driver.find_elements_by_class_name('_3ExzF')                                        #msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
    msg = [message.text for message in msg_got]
    
   
try:

     if msg[0] == "Hello!":
   
      xpath = './/div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
      reply = driver.find_element_by_xpath(xpath)
      
      reply.send_keys("Hello! message recieved correctly") 
      reply.send_keys(Keys.RETURN)
      reply.clear()


              
     
     if msg[0] == "Test":
             xpath = './/div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
             reply = driver.find_element_by_xpath(xpath)
             reply.send_keys("Hello! message recieved correctly") 
             reply.send_keys(Keys.RETURN)
             reply.clear()


     
     else:

         xpath = './/div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
         reply = driver.find_element_by_xpath(xpath)
         reply.send_keys("Your message could not be read correctly")
         reply.send_keys(Keys.RETURN)
         reply.clear()



except IndexError:
     xpath = './/div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
     print("IndexError")
     reply = driver.find_element_by_xpath(xpath)
     reply.clear()
     reply.send_keys("The script ran into a IndexError!")
     reply.send_keys(Keys.RETURN)

      

#finally:
 #  reply = driver.find_element_by_name('.//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]')
  # reply.clear()
   #reply.send_keys("This message will be sent anyway!")
   #reply.send_keys(Keys.RETURN)