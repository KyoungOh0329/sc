from selenium import webdriver

driver = webdriver.Chrome('/Users/mazoola12/Documents')
driver.get('https://cvat.dyhs.kr/tasks/37/jobs/11')
driver.implicitly_wait(time_to_wait=5)
element = driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[13]').text
### driver.quit()