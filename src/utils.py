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
from bs4 import BeautifulSoup

ebird_url = 'https://ebird.org/india/'
html_parser = 'html.parser'
myebird_species_li_class = 'Observation Observation--flushInPageSection Observation--sightingsList'


def get_species_list(web_page):
    """
        Return a list of species in a myEbird page.
    """
    bs4_obj = BeautifulSoup(web_page, html_parser)
    table_list = bs4_obj.find_all('li', class_=myebird_species_li_class)
    species_list = []
    for item in table_list:
        bird_name = item.find_all('div')[1].find('a').find_all('span')[0].contents[0].strip()
        species_list.append(bird_name)
    return species_list


def get_location_based_lifers(web_page):
    """
    a method that takes in a web page and returns back location frequency for lifers and lifer details.
    """
    bs4_object = BeautifulSoup(web_page, html_parser)
    table_list = bs4_object.find_all('li', class_=myebird_species_li_class)
    lifer_data_list = []
    for item in table_list:
        bird_name = item.find_all('div')[1].find('a').find_all('span')[0].contents[0].strip()
        location = item.find_all('div')[2].find_all('div')[1].find_all('a')[0].contents[0].strip()
        date = item.find_all('div')[2].find_all('div')[0].find('a').contents[0].strip()
        lifer_data_list.append([bird_name, location, date])
    location_frequency = dict()
    for item in range(len(lifer_data_list)):
        if lifer_data_list[item][1] in location_frequency.keys():
            location_frequency[lifer_data_list[item][1]] += 1
        else:
            location_frequency[lifer_data_list[item][1]] = 1
    sorted_location_frequency = sorted(location_frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_location_frequency, lifer_data_list


def get_checklists_summary(web_pages):
    """
        a function that summarises all checklists.
    """
    species_list = set()
    for web_page_curr in web_pages:
        soup = BeautifulSoup(web_page_curr.text, html_parser)
        bird_list_ol = soup.find('ol', class_='u-stack-md')
        bird_list_span = bird_list_ol.find_all('span', class_='Heading-main')
        for bird in bird_list_span:
            names = bird.contents[0]
            species_list.add(names)
    return sorted(species_list)


def get_hotspot_details(web_page):
    """
        Return hotspot name and list of hotspot species.
    """
    hotspot_list = []
    bs4_object = BeautifulSoup(web_page, html_parser)
    hotspot_name = bs4_object.find(class_='Heading-main').contents[0].strip()
    bird_name_list = bs4_object.find_all(class_='Observation-species')
    for item in bird_name_list:
        bird_name_a = item.find('a')
        if bird_name_a is not None and bird_name_a.find(class_='Heading-main') is not None:
            hotspot_list.append(bird_name_a.find(class_='Heading-main').contents[0].strip())
    return hotspot_name, hotspot_list


def get_needs_list(web_page):
    """
        a function that returns a dict of needs species.
    """
    needs_map = dict()
    bs4_object = BeautifulSoup(web_page, html_parser)
    need_objects = bs4_object.find_all('div', class_='Observation')
    for item in need_objects:
        bird_name = item.find('span', class_='Heading-main').contents[0]
        location = item.find('a', {'rel': 'noopener'}).contents[0]
        index = location.index(',')
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
