from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

#---------------------------------------------------------GENERAL SETTINGS--------------------------------------------------------------------
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--incognito")
option.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(),options=option) 

def scrap(pages):
    #-----------------------------------------------------------MAIN PAGE----------------------------------------------------------------------
    driver.get(f'https://www.4icu.org/reviews/index{pages}.htm')
    print("\n Page Title is : " + driver.title)
    data = pd.DataFrame(columns=['University','World rank','Address','Telephone','Gender','International admission','Selection type','Control type','Entity type','affiliations','Departments','Features'])
    #------------------------------------------------------------SCRAPPING----------------------------------------------------------------------
    main_list = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/table/tbody")
    links = [link.get_attribute('href') for link in main_list.find_elements_by_tag_name("a")]
    for each in links:
        driver.get(each)
        #Basic details
        university_name = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[2]/h1")
        world_rank = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[3]/table/tbody/tr[2]")
        address = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td")
        telephone = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td/span")
        gender = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr[1]/td")
        international_admission = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr[2]/td")
        selection_type = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr[3]/td")
        control_type = driver.find_element_by_xpath("/html/body/div[3]/div[8]/div[2]/div/div[1]/table/tbody/tr[3]/td")
        entity_type = driver.find_element_by_xpath("/html/body/div[3]/div[8]/div[2]/div/div[1]/table/tbody/tr[4]/td")
        try:
            affiliations = driver.find_element_by_xpath("/html/body/div[3]/div[11]/div[2]/ul")
            affiliations_text = affiliations.text
        except NoSuchElementException:
            affiliations_text = "no-data"
            pass
        try:
            departments = driver.find_element_by_xpath("/html/body/div[3]/div[12]/div[2]")
            departments_text = departments.text
        except NoSuchElementException:
            departments_text = "no-data"
            pass
        #facilities and features
        facilities = []
        fac_library = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[2]/div/div[1]/table/tbody/tr[1]/td")
        if fac_library.text == "Yes":
            facilities.append("library")
        fac_housing = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[2]/div/div[1]/table/tbody/tr[2]/td")
        if fac_housing.text == "Yes":
            facilities.append("housing")
        fac_sports = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[2]/div/div[1]/table/tbody/tr[3]/td")
        if fac_sports.text == "Yes":
            facilities.append("sports facilities")
        fac_financial_aid = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[2]/div/div[1]/table/tbody/tr[4]/td")
        if fac_financial_aid.text == "Yes":
            facilities.append("financial aid")
        fac_distance_learning = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[2]/div/div[2]/table/tbody/tr[2]/td")
        if fac_distance_learning.text == "Yes":
            facilities.append("distant learning")
        try:
            fac_career_service = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[2]/div/div[2]/table/tbody/tr[4]/td")
            if fac_career_service.text == "Yes":
                facilities.append("career services")
        except NoSuchElementException:
            career_service = "no-data"
            pass
        if not facilities:
            facilities.append("Not reported")
        data.loc[len(data)] = [university_name.text,world_rank.text,address.text,telephone.text,gender.text,international_admission.text,selection_type.text,
        control_type.text,entity_type.text,affiliations_text,departments_text,facilities]
        data.to_csv(f"page{pages}.csv")
        driver.back()
    
    print("csv data RELEASED")
    return f"page : {pages} done"
#------------------------------------------------MAIN OPERATION-------------------------------------------------------------------------
a_z = [i for i in range(23,28)]
out = list(map(scrap,a_z))
print(out)