from selenium import webdriver
from bs4 import BeautifulSoup

# Workplan
#
# step1 : Get all the original links
#
# step2 : Click the learnmore button in the client
#
# step3 : Handover the pagesource to BeautifulSoup
#
# step4 : Click the Field of study (span=icon)  in the client
#
# step 5: Again handover the page source to the client
#
# Step 6 : repeat step 4 and 5 for other javascript fields


driver = webdriver.Firefox()
url = "https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/detail/all/search/1/studtyp/3.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100"
driver.get(url)
# link = driver.find_element_by_class_name('icon')
# link_click = link.click()
#
# page_soup = BeautifulSoup(driver.page_source, 'lxml')
#
# print(page_soup.prettify())
# find all the Learn More links in the page
# span_icon = page_soup.find_all('span', {'class': 'icon'})

# print(span_icon)

# for link in links:

# driver.quit()
# fos_icon = driver.find_element_by_class_name("icon")
# content = fos_icon.click()
# soup_level1 = BeautifulSoup(driver.page_source, 'lxml')
# print(content)
# print(soup_level1)
# driver.find_element_by_id("search_button_homepage").click()
# print(driver.current_url)
