from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import TimeoutException
import pandas
import time


option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)
#------------NAVIGATION 01-----------------------------------------------------------------------------------------------------------------------------------------------
driver.get('https://www.quickerala.com/')
print("\n Page Title is : " + driver.title)
driver.find_element_by_xpath('/html/body/section[2]/div/div/div[15]/a/div[2]').click() #click on a category
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-lead-form"]/div/div/div/a')))
element.click() #to close ad that pops up
qk=pandas.DataFrame(columns=['name','phone','address','rating','description','main_tag','sub_tag'])
#------------DATA COLLECTION---------------------------------------------------------------------------------------------------------------------------------------------
def get_data():
    driver.refresh()
    for i in range(4):
        scroll_point = driver.find_element_by_class_name('pagination')
        desired_y = (scroll_point.size['height'] / 2) + scroll_point.location['y']
        current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
        scroll_y_by = desired_y - current_y
        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    main_block = driver.find_elements_by_class_name('listItem')
    for sub_block in main_block:
        name = sub_block.find_element_by_class_name('listHeading')
        location = sub_block.find_element_by_class_name('listLocation')
        rating = sub_block.find_element_by_class_name('ratingVot')
        contact = sub_block.find_element_by_class_name('listContacts')
        description = sub_block.find_element_by_class_name('desc')
        main_tag = sub_block.find_element_by_class_name('listedsec')
        sub_tag = sub_block.find_element_by_class_name('clearfix')
        qk.loc[len(qk)] = [name.text,contact.text,location.text,rating.text,description.text,main_tag.text,sub_tag.text]
        qk.to_csv('out.csv')
        # print("name = " + name.text + "phone : " + contact.text )
        # print("location = " + location.text + "rating : " + rating.text )
        # print("description = " + description.text + "tags : " + main_tag.text )
        # print(sub_tag.text+"\n")
        # print("-------------------------------------------------------------------------------------------------------------------------------------------")
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
i=0
while i==0:
    try:
        driver.find_element_by_class_name('listItem')
    except NoSuchElementException:
        print("-------COMPLETED---------")
        break
        driver.quit()
    else: 
        get_data()
        driver.find_element_by_css_selector('body > section.grey-bg.padtop-15.padbottom-30 > div > div > div > div.col-lg-9.col-md-9.col-sm-12.col-xs-12.pull-right > div.listingWrap > div.pagination.text-center > ul > li:nth-child(12) > a').click() #click on next button
        #element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-lead-form"]/div/div/div/a')))
        try:   
            element1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-lead-form"]/div/div/div/a')))
            element1.click() #to close ad that pops up
        except TimeoutException:
            get_data()

        

