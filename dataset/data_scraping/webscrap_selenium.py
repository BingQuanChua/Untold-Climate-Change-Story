from selenium import webdriver  
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.action_chains import ActionChains
import time  

print("\nStarted web scraping\n")

# initiate chrome driver
driver = webdriver.Chrome(r"chromedriver.exe")  
print("\nInitiated chrome driver\n")

# maximize the window size  
# driver.maximize_window()  

# navigate to the url  
driver.get("https://climateknowledgeportal.worldbank.org/download-data")  
print("\nOpened website\n")
time.sleep(5)

# identify the timeseries tab 
download_form = driver.find_element_by_id("data-download-form-container")
print("\nFound #data-download-form-container\n")
time.sleep(2)
timeseries_tab = driver.find_element_by_xpath('//div[@id="data-download-form-container"]/div/ul/li[3]/a')
print("\nFound #timeseries-tab\n")
driver.execute_script("window.scrollTo(0, 475)") 
time.sleep(2)

ActionChains(driver).move_to_element(download_form).click(timeseries_tab).perform()  
print("\nNavigated to timeseries-tab\n")
time.sleep(2)

# fill the form 
print("\nFilling the form\n") 
select_collection = Select(driver.find_element_by_xpath('//form[@class="form_timeseries_tab"]/div/div/select[@id="collection"]'))
select_collection.select_by_value("cru")
time.sleep(2)
select_variable = Select(driver.find_element_by_xpath('//form[@class="form_timeseries_tab"]/div/div/select[@id="variable"]'))
select_variable.select_by_value("tas")
time.sleep(2)
select_aggregation = Select(driver.find_element_by_xpath('//form[@class="form_timeseries_tab"]/div/div/select[@id="aggregation"]'))
select_aggregation.select_by_value("annual") 
time.sleep(2)
select_area_type = Select(driver.find_element_by_xpath('//form[@class="form_timeseries_tab"]/div/div/select[@id="type"]'))
select_area_type.select_by_value("country") 

# ready to download
print("\nFilled form, download starts in 5 seconds\n")
time.sleep(5)
select_country = Select(driver.find_element_by_xpath('//form[@class="form_timeseries_tab"]/div/div/select[@id="country"]'))

# get all the dropdown options
opt = select_country.options
print("\nTotal number of country: "+str(len(opt))+"\n")

# start to download
print("\nStarting download...\n\n")
time.sleep(2)


# loop the download
for i in range (1,len(opt)):
    select_country.select_by_index(i)
    print("Selected country "+str(i) + ", " + str(opt[i].text))
    time.sleep(8)
    driver.implicitly_wait(7)
    print("Downloading...")
    driver.find_element_by_xpath('//form[@class="form_timeseries_tab"]/div/div/button[@id="submit"]').click()
    time.sleep(10)
    print("Downloaded "+str(i)+"\n")

# final waiting time for any unfinished downloads
time.sleep(10)
print("waited 10s")
time.sleep(10)
print("waited 20s\n")
print("\nready to exit\n")
time.sleep(2)

#close the browser  
driver.close()  
print("\n\nweb scraping successfully completed\n\n") 