"""
A file for util functions.
"""
from bs4 import BeautifulSoup

ebird_url = 'https://ebird.org/india/'


def login():
    """
    a function that does the login into the selenium browser.
    :return:
    """
    from selenium import webdriver
    login_url = r'https://secure.birds.cornell.edu/cassso/login?service=https%3A%2F%2Febird.org%2Flogin%2Fcas%3F' \
                'portal%3Dindia&locale=en_US'
    selenium_browser_object = webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver.exe")
    selenium_browser_object.minimize_window()
    # login_id = input("enter login id for ebird\n")
    # password = input("enter password\n")
    selenium_browser_object.get(login_url)
    selenium_browser_object.find_element_by_name("username").send_keys("")
    selenium_browser_object.find_element_by_name("password").send_keys("")
    selenium_browser_object.find_element_by_id("form-submit").click()
    return selenium_browser_object


def life_list(web_page):
    """

    :param web_page:
    """
    soup_obj = BeautifulSoup(web_page, 'html.parser')
    table_list = soup_obj.find_all('li',
                                   class_='Observation Observation--flushInPageSection Observation--sightingsList')
    species_list = []
    for item in table_list:
        bird_name = item.find_all('div')[1].find('a').find_all('span')[0].contents[0].strip()
        species_list.append(bird_name)
    return species_list


def location_for_lifers(web_page):
    """

    :param web_page:
    """
    bs4_object = BeautifulSoup(web_page, 'html.parser')
    table_list = bs4_object.find_all('li',
                                     class_='Observation Observation--flushInPageSection Observation--sightingsList')
    data_list = []
    for item in table_list:
        bird_name = item.find_all('div')[1].find('a').find_all('span')[0].contents[0].strip()
        location = item.find_all('div')[2].find_all('div')[1].find_all('a')[0].contents[0].strip()
        date = item.find_all('div')[2].find_all('div')[0].find('a').contents[0].strip()
        data_list.append([bird_name, location, date])
    location_frequency = dict()
    for item in range(len(data_list)):
        if data_list[item][1] in location_frequency.keys():
            location_frequency[data_list[item][1]] += 1
        else:
            location_frequency[data_list[item][1]] = 1
    sorted_location_frequency = sorted(location_frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_location_frequency, data_list


def checklist_summariser(web_pages):
    """
        a function that summarises all checklists.
    """
    species = set()
    for web_page_curr in web_pages:
        soup = BeautifulSoup(web_page_curr.text, 'html.parser')
        bird_list_li = soup.find('ol', class_="u-stack-md")
        bird_list_a = bird_list_li.find_all('span', class_='Heading-main')
        for bird in bird_list_a:
            names = bird.contents[0]
            species.add(names)
    return sorted(species)


def get_hotspot_details(web_page):
    """

    :param web_page:
    """
    hotspot_list = []
    bs4_object_hotspot1 = BeautifulSoup(web_page, 'html.parser')
    hotspot_name = bs4_object_hotspot1.find(class_='hotspot--name').contents[0].strip()
    bird_name_list1_species = bs4_object_hotspot1.find_all(class_='species-name')
    for item in bird_name_list1_species:
        bird_name_list_items1 = item.find_all('a')
        for bird_name in bird_name_list_items1:
            hotspot_list.append(bird_name.contents[0].strip())
    return hotspot_name, hotspot_list


def hotspot_comparision(web_page1, web_page2):
    """
        a function that compares 2 hotspots and gives the unique species list.
    """
    hotspot1_name, hotspot1_list = get_hotspot_details(web_page1)
    hotspot2_name, hotspot2_list = get_hotspot_details(web_page2)
    unique_in_hotspot1 = sorted(set(hotspot1_list) - set(hotspot2_list))
    unique_in_hotspot2 = sorted(set(hotspot2_list) - set(hotspot1_list))
    return unique_in_hotspot1, unique_in_hotspot2, hotspot1_name, hotspot2_name


def get_district_list_page(selenium_browser, data_cells, iterator, offset):
    """
    :param selenium_browser:
    :param data_cells:
    :param iterator:
    :param offset:
    :return:
    """
    url_all_time = str(data_cells[iterator + offset])
    bs4_all_time = BeautifulSoup(url_all_time, 'html.parser')
    link_tag = bs4_all_time.find('a', href=True)
    all_time_link = link_tag['href']
    selenium_browser.get(ebird_url + all_time_link)
    return selenium_browser.page_source


def year_list_comparision(year_list_page_1, year_list_page_2):
    """
    :param year_list_page_1:
    :param year_list_page_2:
    """
    year1_list = life_list(year_list_page_1)
    year2_list = life_list(year_list_page_2)
    unique_in_year1 = set(year1_list) - set(year2_list)
    unique_in_year2 = set(year2_list) - set(year1_list)
    return unique_in_year1, unique_in_year2


def possible_lifers_in_a_hotspot(web_page, life_species_list):
    """
        a function to find the lifers possible in a hotspot.
    """
    hotspot_name, hotspot_list = get_hotspot_details(web_page)
    lifers_in_hotspot = hotspot_list.copy()
    for life_list_item in life_species_list:
        for hotspot_item in lifers_in_hotspot:
            if hotspot_item in life_list_item:
                lifers_in_hotspot.remove(hotspot_item)
    return lifers_in_hotspot, hotspot_name


def get_needs_list(district_name, current_year_required):
    """
    :param district_name:
    :param current_year_required:
    :return:
    """
    import time
    needs_map = dict()
    selenium_browser = login()
    selenium_browser.get(ebird_url + "alerts")
    selenium_browser.find_element_by_name("needs").send_keys(district_name)
    time.sleep(5)
    selenium_browser.find_element_by_class_name("Suggestion-text").click()
    if current_year_required.lower() == 'y':
        selenium_browser.find_element_by_name("t2").click()
    selenium_browser.find_element_by_id("needs-view-btn").click()
    soup = BeautifulSoup(str(selenium_browser.page_source), 'html.parser')
    need_objects = soup.find_all('div', class_="Observation")
    for item in need_objects:
        bird_name = item.find('span', class_='Heading-main').contents[0]
        location = item.find('a', {'rel': 'noopener'}).contents[0]
        index = location.index(",")
        location = location[:index]
        if bird_name in needs_map:
            locations = needs_map[bird_name]
            locations.add(location)
            needs_map[bird_name] = locations
        else:
            locations = set()
            locations.add(location)
            needs_map[bird_name] = locations
    return needs_map
