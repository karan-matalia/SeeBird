"""
a program to perform all ebird actions.
"""
from src.controllers import get_life_list, get_location_based_lifers, get_region_list, compare_year_list, \
    summarise_checklists, compare_hotspots, get_possible_lifers_in_a_hotspot, get_possible_lifers_in_a_trip, \
    needs_list, compare_district_year_list

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
