import requests
from bs4 import BeautifulSoup

# url = "https://www.daad.de/deutschland/studienangebote/studiengang/en/?a=result&q=&degree=&courselanguage=&locations=&admissionsemester=&sort=name&page=1"

# First 100 results
# https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/search/1/studtyp/3.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100

# Deatiled information about each course (Learn More button)
# https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/detail/all/search/1/studtyp/3.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100


# Next rsults follows same pattern replace 1.html by increasing numbers say from 1 to 18
# https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/search/1/studtyp/3/pn/1.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100

url = "https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/search/1/studtyp/3.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100"

first_page = requests.get(url)

first_page_soup = BeautifulSoup(first_page.text, 'html.parser')

print(first_page_soup.prettify())

# hit = first_page_soup.find('p', class_='loading')

# course_name = hit.h3.a.text

# print(hit.ul)



