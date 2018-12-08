import requests
import time
import json
from bs4 import BeautifulSoup

# First 100 results
# https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/search/1/studtyp/3.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100

# Deatiled information about each course (Learn More button)
# https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/detail/all/search/1/studtyp/3.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100

# first_page_url = "https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/search/1/studtyp/3.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100"

# remaining_pages_url = "https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/search/1/studtyp/3/pn/1.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100"


page_num_list = list(range(1, 199))

url_list_second_page_to_last_page = []

url_list_first_page = ["https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/search/1/studtyp/3.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100"]

""" Construct a list of urls for all the 199 pages """
for num in page_num_list:

    url = "https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/search/1/studtyp/3/pn/"+str(num)+".html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100"

    url_list_second_page_to_last_page.append(url)

url_list = url_list_first_page + url_list_second_page_to_last_page

# url = "https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/search/1/studtyp/3.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100"

only_learn_more_links = []

main_dict = {}

counter = 0

small_url = [url_list[0], url_list[1], url_list[2]]

for url in small_url:

    page_data = requests.get(url)

    page_soup = BeautifulSoup(page_data.text, 'html.parser')

    # find all the Learn More links in the page
    links = page_soup.find_all('a', {'class': 'btn-info btn'})

    for link in links:
        if 'Learn More' in link.text:
            print(link['href'])
            only_learn_more_links.append(link['href'])  # Save href only

    for ul_tag in page_soup.find_all('section', {'class': 'result-box'}):
        counter = counter + 1
        results = {}
        print("Course name = ", ul_tag.h2.text)
        results["Course_Name"] = ul_tag.h2.text

        # counter -1, because list index starts from 0
        print("COUNTER = ", counter)
        dum_var = counter-1
        print("DUM_VAR = ", dum_var)
        results["Learn_more_url"] = "https://www.hochschulkompass.de" + only_learn_more_links[dum_var]

        for li_tag in ul_tag.find_all('ul', {'class': 'info list-inline'}):

            for span_tag in li_tag.find_all('li'):
                field = span_tag.find('span', {'class': 'title'}).text
                value = span_tag.find('span', {'class': 'status'}).text
                print("field = ", field)
                print("value = ", value)
                field = field.replace(" ", "_")
                results[field] = value
            main_dict[counter] = results

cols = list(main_dict.keys())

with open("first_page_res.json", "w") as f:
    json.dump(main_dict, f, ensure_ascii=False, indent=4)



#
# main_dict = {}
#
# for url in url_list:
#
#     page_data = requests.get(url)
#
#     page_soup = BeautifulSoup(page_data.text, 'html.parser')
#
#     counter = 0
#
#     for ul_tag in page_soup.find_all('section', {'class': 'result-box'}):
#         counter = counter + 1
#         results = {}
#         print("Course name = ", ul_tag.h2.text)
#         results["Course_Name"] = ul_tag.h2.text
#
#         for li_tag in ul_tag.find_all('ul', {'class': 'info list-inline'}):
#
#             for span_tag in li_tag.find_all('li'):
#
#                 field = span_tag.find('span', {'class': 'title'}).text
#                 value = span_tag.find('span', {'class': 'status'}).text
#                 print("field = ", field)
#                 print("value = ", value)
#                 field = field.replace(" ", "_")
#                 results[field] = value
#             main_dict[counter] = results
#
# cols = list(main_dict.keys())
#
# with open("first_page_res.json", "w") as f:
#     json.dump(main_dict, f, ensure_ascii=False, indent=4)




# print(url_list)

# print(len(url_list))

# https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/search/1/studtyp/3/pn/2.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100

#
# for result in first_page_results:
#     if len(result.attrs) == 2:
#         print("RESULTS")
#         print("*************************************************")
#         print(result)
#         print("COURSE NAME")
#         print("*************************************************")
#         print(result.h2)
#         break






