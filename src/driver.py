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
from src.controllers import get_life_list, get_location_based_lifers, get_region_list, compare_year_list, \
    summarise_checklists, compare_hotspots, get_possible_lifers_in_a_hotspot, get_possible_lifers_in_a_trip, \
    needs_list

if __name__ == '__main__':
    while True:
        choice = int(input(
            "\nPress 1 for Life list press\n\t  2 for location based details for lifers\n\t"
            "  3 for summarising checklists\n\t  4 for comparing hotspots \n\t  5 for region list\n\t"
            "  6 for year list comparision\n\t"
            "  8 for possible lifers in a hotspot\n\t  9 possible lifers in a trip (multiple hotspots)\n\t"
            "  10 for needs list for a district\n\t  Anything else to exit\n"))
        if choice == 1:
            get_life_list()
        elif choice == 2:
            get_location_based_lifers()
        elif choice == 3:
            summarise_checklists()
        elif choice == 4:
            compare_hotspots()
        elif choice == 5:
            get_region_list()
        elif choice == 6:
            compare_year_list()
        elif choice == 8:
            get_possible_lifers_in_a_hotspot()
        elif choice == 9:
            get_possible_lifers_in_a_trip()
        elif choice == 10:
            needs_list()
        else:
            exit(0)
