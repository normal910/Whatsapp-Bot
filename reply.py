from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("https://web.whatsapp.com/")

input("Press anything after QR scan")
time.sleep(5)


names = ["ContactName"] #Your Chat goes there <-

for name in names:

    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    person.click()

    for i in range(1,3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
    msg = [message.text for message in msg_got]

   
    if msg[0] == "Hello!":
   
      xpath = './/div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
      reply = driver.find_element_by_xpath(xpath)
      #("_2S1VP.copyable-text.selectable-text")reply.clear()
      reply.send_keys("Hello! message recieved correctly") 
      reply.send_keys(Keys.RETURN)


except IndexError:
 print("IndexError")
 reply = driver.find_element_by_xpath(xpath)
 reply.clear()
 reply.send_keys("The script ran into a IndexError!")
 reply.send_keys(Keys.RETURN)




       else:
       reply = driver.find_element_by_xpath(xpath)
       reply.clear()
       reply.send_keys("your message could not be read correctly")
       reply.send_keys(Keys.RETURN)

finally:
   reply = driver.find_element_by_xpath(xpath)
   reply.clear()
   reply.send_keys("This message will be sent anyway!")
   reply.send_keys(Keys.RETURN)