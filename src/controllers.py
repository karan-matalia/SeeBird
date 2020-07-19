"""
MIT License

Copyright (c) 2020 Karan Matalia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import time

import requests
from selenium import webdriver

from src.utils import get_checklists_summary, get_hotspot_details, get_location_based_lifers, get_needs_list, \
    get_species_list


class Controllers:
    def __init__(self):
        self.ebird_url = 'https://ebird.org/india/'
        self.life_list_url = r'https://ebird.org/india/MyEBird?cmd=list&rtype=custom&r=world&time=life&sortKey=obs_dt' \
                             r'&o=asc'
        self.login_url = r'https://secure.birds.cornell.edu/cassso/login?service=https%3A%2F%2Febird.org%2Flogin%2F' \
                         r'cas%3Fportal%3Dindia&locale=en_US'
        self.selenium_browser = None
        self.life_species_list = None

    def login(self):
        """
            A function that does the login into the selenium browser.
        """
        self.selenium_browser = webdriver.Chrome(r'C:\Users\admin\Downloads\chromedriver.exe')
        self.selenium_browser.minimize_window()
        self.selenium_browser.get(self.login_url)
        self.selenium_browser.find_element_by_name('username').send_keys('your-username')
        self.selenium_browser.find_element_by_name('password').send_keys('your-password')
        self.selenium_browser.find_element_by_id('form-submit').click()

    def print_life_list(self):
        """
            A method that prints the life list.
        """
        if self.selenium_browser is None:
            self.login()
        self.selenium_browser.get(self.life_list_url)
        life_list_page = str(self.selenium_browser.page_source)
        self.life_species_list = get_species_list(life_list_page)
        print('Your lifers sorted by date are : \n')
        for index, species_name in enumerate(self.life_species_list):
            print(index + 1, '. ', species_name)

    def print_location_based_lifers(self):
        """
            Get location Based lifers.
        """
        if self.selenium_browser is None:
            self.login()
        self.selenium_browser.get(self.life_list_url)
        life_list_page = str(self.selenium_browser.page_source)
        sorted_location_frequency, lifer_data_list = get_location_based_lifers(life_list_page)
        print('Your lifers sorted by location are:\n')
        for item in sorted_location_frequency:
            print('\nYour lifers in ', item[0], ' are : \n')
            count = 1
            for lifer_details in lifer_data_list:
                if lifer_details[1] == item[0]:
                    print(count, '. ', lifer_details[0], ' first seen on ', lifer_details[2])
                    count += 1

    def print_checklist_summary(self):
        """
            Create a summary of a list of checklists.
        """
        checklist_links = []
        web_pages = []
        print('\nEnter the link of the checklists.Enter done to quit. \n')
        while True:
            list_of_checklists = input()
            if list_of_checklists.casefold() == 'done'.casefold():
                break
            else:
                checklist_links.append(list_of_checklists)
        for link_curr in checklist_links:
            web_pages.append(requests.get(link_curr))
        species_list = get_checklists_summary(web_pages)
        for index, species_name in enumerate(species_list):
            print(index + 1, '. ', species_name)

    def print_hotspots_comparision(self):
        """
            Method to compare 2 hotspots.
        """
        print('Enter hotspot links')
        hotspot_link1 = input('Enter link 1 : ').strip()
        hotspot_link2 = input('Enter link 2 : ').strip()
        web_page1 = requests.get(hotspot_link1).text
        web_page2 = requests.get(hotspot_link2).text
        hotspot1_name, hotspot1_list = get_hotspot_details(web_page1)
        hotspot2_name, hotspot2_list = get_hotspot_details(web_page2)
        unique_in_hotspot1 = sorted(set(hotspot1_list) - set(hotspot2_list))
        unique_in_hotspot2 = sorted(set(hotspot2_list) - set(hotspot1_list))
        print('Unique species in ' + hotspot1_name)
        for index, val in enumerate(unique_in_hotspot1):
            print(index + 1, '. ', val)

        print('Unique species in ' + hotspot2_name)
        for index, val in enumerate(unique_in_hotspot2):
            print(index + 1, '. ', val)

    def print_region_list(self):
        """
            Api to compare district list.
        """
        print('Enter exact region name: ')
        search_district = input()
        list_type = input('Which list id required: All time, year, month or day?')
        if self.selenium_browser is None:
            self.login()
        self.selenium_browser.get(self.ebird_url + 'myebird')
        time.sleep(5)
        self.selenium_browser.find_element_by_xpath("//div[@class='SectionHeading-link']/a").click()
        self.selenium_browser.find_element_by_xpath("//div[@class='Suggest-inputContainer']/input").send_keys(
            search_district)
        time.sleep(5)
        self.selenium_browser.find_element_by_class_name("Suggestion-text").click()
        time.sleep(5)
        self.selenium_browser.find_element_by_xpath("//ul[@class='StatsToolbar StatsToolbar--fiveAcross']/li").click()
        time.sleep(5)
        self.selenium_browser.find_element_by_xpath(
            "//a[@class='Toolbar-item-button Toolbar-item-button--hasDropdown Toolbar-item-button--labelNoWrap']").click()
        time.sleep(5)
        if list_type.casefold() == "year".casefold():
            self.selenium_browser.find_element_by_xpath("//ul[@class='SectionMenu-section-list']/li[2]/a").click()
        elif list_type.casefold() == "month".casefold():
            self.selenium_browser.find_element_by_xpath("//ul[@class='SectionMenu-section-list']/li[3]/a").click()
        elif list_type.casefold() == "day".casefold():
            self.selenium_browser.find_element_by_xpath("//ul[@class='SectionMenu-section-list']/li[4]/a").click()
        time.sleep(5)
        self.selenium_browser.find_element_by_xpath("//a[@class='RadioGroup--toggler u-inset-sm u-prn']").click()
        self.selenium_browser.find_element_by_xpath("//span[text()='Date: Oldest First']").click()
        page = str(self.selenium_browser.page_source)
        district_species_list = get_species_list(page)
        for index, species_name in enumerate(district_species_list):
            print(index + 1, ', ', species_name)

    def print_year_list_comparision(self):
        """
            Api to compare the year list.
        """
        input_year1 = input('Enter a year : ')
        input_year2 = input('Enter another year : ')
        if self.selenium_browser is None:
            self.login()
        self.selenium_browser.get(
            self.ebird_url + r'MyEBird?cmd=lifeList&listType=IN&listCategory=country&time=year&year='
            + input_year1 + r'&sortKey=obs_dt&o=asc')
        year_list_page1 = str(self.selenium_browser.page_source)
        self.selenium_browser.get(
            self.ebird_url + r'MyEBird?cmd=lifeList&listType=IN&listCategory=country&time=year&year='
            + input_year2 + r'&sortKey=obs_dt&o=asc')
        year_list_page2 = str(self.selenium_browser.page_source)
        year1_list = get_species_list(year_list_page1)
        year2_list = get_species_list(year_list_page2)
        unique_in_year1 = set(year1_list) - set(year2_list)
        unique_in_year2 = set(year2_list) - set(year1_list)
        print('unique species in ' + input_year1)
        for index, val in enumerate(unique_in_year1):
            print(index + 1, '. ', val)
        print('unique species in ' + input_year2)
        for index, val in enumerate(unique_in_year2):
            print(index + 1, '. ', val)

    def get_possible_lifers_in_a_hotspot(self, hotspot_web_page, life_list_species, life_list_web_page=None):
        """
            a function to find the lifers possible in a hotspot.
        """
        if life_list_species is None:
            life_list_species = get_species_list(life_list_web_page)
        hotspot_name, hotspot_list = get_hotspot_details(hotspot_web_page)
        lifers_in_hotspot = set(hotspot_list) - set(life_list_species)
        return lifers_in_hotspot, hotspot_name

    def print_possible_lifers_in_a_hotspot(self):
        """
            Method to get lifers possible in a hotspot.
        """
        life_list_page = None
        hotspot_link = input('Enter hotspot link : ').strip()
        if self.selenium_browser is None:
            self.login()
        if self.life_species_list is None:
            self.selenium_browser.get(self.life_list_url)
            life_list_page = str(self.selenium_browser.page_source)
        self.selenium_browser.get(hotspot_link)
        hotspot_list_web_page = str(self.selenium_browser.page_source)
        lifers_in_hotspot, hotspot_name = self.get_possible_lifers_in_a_hotspot(hotspot_list_web_page,
                                                                                self.life_species_list, life_list_page)
        print('Possible lifers in ' + hotspot_name)
        for index, val in enumerate(lifers_in_hotspot):
            print(index + 1, '. ', val)

    def print_possible_lifers_in_a_trip(self):
        """
            Possible lifers in a trip.
        """
        hotspot_links = []
        lifers_possible = {}
        life_list_page = None
        print('Enter the hotspot links. Enter done to quit.')
        while True:
            hotspot_link = input().strip()
            if hotspot_link.casefold() == 'done'.casefold():
                break
            else:
                hotspot_links.append(hotspot_link)
        if self.selenium_browser is None:
            self.login()
        if self.life_species_list is None:
            self.selenium_browser.get(self.life_list_url)
            life_list_page = str(self.selenium_browser.page_source)
        for link in hotspot_links:
            self.selenium_browser.get(link)
            hotspot_web_page = str(self.selenium_browser.page_source)
            lifers_in_hotspot, hotspot_name = self.get_possible_lifers_in_a_hotspot(hotspot_web_page,
                                                                                    self.life_species_list,
                                                                                    life_list_page)
            for bird_species in lifers_in_hotspot:
                if bird_species in lifers_possible:
                    locations = lifers_possible[bird_species]
                    locations.append(hotspot_name)
                    lifers_possible[bird_species] = locations
                else:
                    lifers_possible[bird_species] = [hotspot_name]

        print('Possible lifers are ')
        for index, val in enumerate(lifers_possible):
            print(index + 1, '. ', val, ' can be seen in: ', lifers_possible[val])

    def print_needs_list(self):
        """
            Get the summarised needs list for a district.
        """
        district_name = input('Enter district name for needs list:\n')
        current_year_required = input('Current year only? y /n ')
        if self.selenium_browser is None:
            self.login()
        self.selenium_browser.get(self.ebird_url + 'alerts')
        self.selenium_browser.find_element_by_name('needs').send_keys(district_name)
        time.sleep(5)
        self.selenium_browser.find_element_by_class_name('Suggestion-text').click()
        if current_year_required.lower() == 'y':
            self.selenium_browser.find_element_by_name('t2').click()
        self.selenium_browser.find_element_by_id('needs-view-btn').click()
        needs_map = get_needs_list(str(self.selenium_browser.page_source))
        for index, val in enumerate(needs_map):
            print(index + 1, '. ', val, ' can be seen in: ', needs_map[val])
