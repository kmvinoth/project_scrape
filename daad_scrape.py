import requests
from bs4 import BeautifulSoup

url = "https://www.daad.de/deutschland/studienangebote/studiengang/en/?a=result&q=&degree=&courselanguage=&locations=&admissionsemester=&sort=name&page=1"

first_page = requests.get(url)

first_page_soup = BeautifulSoup(first_page.text, 'html.parser')

hit = first_page_soup.find('p', class_='loading')

# course_name = hit.h3.a.text

print(hit.ul)



