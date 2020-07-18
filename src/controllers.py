"""
a program to perform all ebird actions.
"""
import time

from src.utils import year_list_comparision, checklist_summariser, hotspot_comparision, \
    location_for_lifers, possible_lifers_in_a_hotspot, get_needs_list, life_list

ebird_url = 'https://ebird.org/india/'


def get_life_list():
    """

    :return:
    """
    from src.utils import life_list, login
    selenium_browser = login()
    selenium_browser.get(ebird_url + r'MyEBird?cmd=list&rtype=custom&r=world&time=life&sortKey=obs_dt&o=asc')
    page = str(selenium_browser.page_source)
    life_species_list = life_list(page)
    counter = 1
    print("Your lifers sorted by date are : \n")
    for item in life_species_list:
        print(counter, " ", item)
        counter += 1


def get_location_based_lifers():
    """
            Get location Based lifers.
    """
    from src.utils import login
    selenium_browser = login()
    selenium_browser.get(ebird_url + r'MyEBird?cmd=list&rtype=custom&r=world&time=life&sortKey=obs_dt&o=asc')
    page = str(selenium_browser.page_source)
    sorted_location_frequency, data_list = location_for_lifers(page)
    print("Your lifers sorted by location are:")
    for item in sorted_location_frequency:
        print("\nYour lifers in ", item[0], " are : \n")
        count = 1
        for items in data_list:
            if items[1] == item[0]:
                print(count, ". ", items[0], " first seen on ", items[2])
                count += 1


def summarise_checklists():
    """
            Api to summarise checklists.
    """
    import requests
    checklist_links = []
    web_pages = []
    print("\nEnter the link of the checklists.Enter done to quit.")
    while True:
        list_of_checklists = input()
        if list_of_checklists.casefold() == "done".casefold():
            break
        else:
            checklist_links.append(list_of_checklists)
    for link_curr in checklist_links:
        web_pages.append(requests.get(link_curr))
    species = checklist_summariser(web_pages)
    count = 1
    for item in species:
        print(count, " ", item)
        count += 1


def compare_hotspots():
    """
            Api to compare 2 hotspots.
    """
    import requests
    print("Enter hotspot links")
    hotspot_link1 = input("Enter link 1 : ").strip()
    hotspot_link2 = input("Enter link 2 : ").strip()
    web_page1 = requests.get(hotspot_link1).text
    web_page2 = requests.get(hotspot_link2).text
    unique_in_hotspot1, unique_in_hotspot2, hotspot1_name, hotspot2_name = hotspot_comparision(web_page1, web_page2)
    print("Unique species in " + hotspot1_name)
    for index, val in enumerate(unique_in_hotspot1):
        print(index + 1, ". ", val)

    print("Unique species in " + hotspot2_name)
    for index, val in enumerate(unique_in_hotspot2):
        print(index + 1, ". ", val)


def get_region_list():
    """
        Api to compare district list.
    """
    from src.utils import login
    print("Enter exact region name: ")
    search_district = input()
    list_type = input("Which list id required: All time, year, month or day?")
    selenium_browser = login()
    selenium_browser.get(ebird_url + 'myebird')
    time.sleep(5)
    selenium_browser.find_element_by_xpath("//div[@class='SectionHeading-link']/a").click()
    selenium_browser.find_element_by_xpath("//div[@class='Suggest-inputContainer']/input").send_keys(search_district)
    time.sleep(5)
    selenium_browser.find_element_by_class_name("Suggestion-text").click()
    time.sleep(5)
    selenium_browser.find_element_by_xpath("//ul[@class='StatsToolbar StatsToolbar--fiveAcross']/li").click()
    time.sleep(5)
    selenium_browser.find_element_by_xpath(
        "//a[@class='Toolbar-item-button Toolbar-item-button--hasDropdown Toolbar-item-button--labelNoWrap']").click()
    time.sleep(5)
    if list_type.casefold() == "all time".casefold():
        selenium_browser.find_element_by_xpath("//ul[@class='SectionMenu-section-list']/li[1]/a").click()
    elif list_type.casefold() == "year".casefold():
        selenium_browser.find_element_by_xpath("//ul[@class='SectionMenu-section-list']/li[2]/a").click()
    elif list_type.casefold() == "month".casefold():
        selenium_browser.find_element_by_xpath("//ul[@class='SectionMenu-section-list']/li[3]/a").click()
    elif list_type.casefold() == "day".casefold():
        selenium_browser.find_element_by_xpath("//ul[@class='SectionMenu-section-list']/li[4]/a").click()
    time.sleep(5)
    page = str(selenium_browser.page_source)
    district_species_list = life_list(page)
    counter = 1
    for item in district_species_list:
        print(counter, " ", item)
        counter += 1
    return district_species_list


def compare_year_list():
    """
        Api to compare the year list.
    """
    from src.utils import login
    selenium_browser = login()
    input_year1 = input("Enter a year : ")
    input_year2 = input("Enter another year : ")
    selenium_browser.get(ebird_url + r'MyEBird?cmd=lifeList&listType=IN&listCategory=country&time=year&year='
                         + input_year1 + r'&sortKey=obs_dt&o=asc')
    year_list_page1 = str(selenium_browser.page_source)
    selenium_browser.get(ebird_url + r'MyEBird?cmd=lifeList&listType=IN&listCategory=country&time=year&year='
                         + input_year2 + r'&sortKey=obs_dt&o=asc')
    year_list_page2 = str(selenium_browser.page_source)
    unique_in_year1, unique_in_year2 = year_list_comparision(year_list_page1, year_list_page2)
    print("unique species in " + input_year1)
    for index, val in enumerate(unique_in_year1):
        print(index + 1, ". ", val)
    print("unique species in " + input_year2)
    for index, val in enumerate(unique_in_year2):
        print(index + 1, ". ", val)

def get_possible_lifers_in_a_hotspot():
    """
            Api to get lifers possible in a hotspot.
    """
    from src.utils import life_list, login
    hotspot_link = input("Enter hotspot link : ").strip()
    selenium_browser = login()
    selenium_browser.get(ebird_url + r'MyEBird?cmd=list&rtype=custom&r=world&time=life&sortKey=obs_dt&o=asc')
    page = str(selenium_browser.page_source)
    selenium_browser.get(hotspot_link)
    web_page = str(selenium_browser.page_source)
    life_list = life_list(page)
    lifers_in_hotspot, hotspot_name = possible_lifers_in_a_hotspot(web_page, life_list)
    print("Possible lifers in " + hotspot_name)
    for index, val in enumerate(lifers_in_hotspot):
        print(index + 1, ". ", val)


def get_possible_lifers_in_a_trip():
    """
        possible lifers in a trip.
    """
    from src.utils import life_list, login
    hotspot_links = []
    lifers_possible = {}
    print("Enter the hotspot links. Enter done to quit.")
    while True:
        hotspot_link = input().strip()
        if hotspot_link.casefold() == "done".casefold():
            break
        else:
            hotspot_links.append(hotspot_link)
    selenium_browser = login()
    selenium_browser.get(ebird_url + r'MyEBird?cmd=list&rtype=custom&r=world&time=life&sortKey=obs_dt&o=asc')
    page = str(selenium_browser.page_source)
    life_list = life_list(page)
    for link in hotspot_links:
        selenium_browser.get(link)
        web_page = str(selenium_browser.page_source)
        lifers_in_hotspot, hotspot_name = possible_lifers_in_a_hotspot(web_page, life_list)
        for item in lifers_in_hotspot:
            if item in lifers_possible:
                locations = lifers_possible[item]
                locations.append(hotspot_name)
                lifers_possible[item] = locations
            else:
                lifers_possible[item] = [hotspot_name]

    print("Possible lifers are ")
    for index, val in enumerate(lifers_possible):
        print(index + 1, ". ", val, " can be seen in: ", lifers_possible[val])


def needs_list():
    """
            Get the summarised needs list for a district.
    """
    district_name = input("Enter district name for needs list:\n")
    current_year_required = input("Current year only? y /n ")
    needs_map = get_needs_list(district_name, current_year_required)
    for index, val in enumerate(needs_map):
        print(index + 1, ". ", val, " can be seen in: ", needs_map[val])
