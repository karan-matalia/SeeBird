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
from src.controllers import Controllers

if __name__ == '__main__':
    controllers = Controllers()
    while True:
        choice = int(input("\nPress 1 for Life list press\n\t  2 for location based details for lifers\n\t"
                           "  3 for summarising checklists\n\t  4 for comparing hotspots \n\t  5 for region list\n\t"
                           "  6 for year list comparision\n\t  7 for possible lifers in a hotspot\n\t"
                           "  8 possible lifers in a trip (multiple hotspots)\n\t  9 for needs list for a district\n\t"
                           "  Anything else to exit\n"))
        if choice == 1:
            controllers.print_life_list()
        elif choice == 2:
            controllers.print_location_based_lifers()
        elif choice == 3:
            controllers.print_checklist_summary()
        elif choice == 4:
            controllers.print_hotspots_comparision()
        elif choice == 5:
            controllers.print_region_list()
        elif choice == 6:
            controllers.print_year_list_comparision()
        elif choice == 7:
            controllers.print_possible_lifers_in_a_hotspot()
        elif choice == 8:
            controllers.print_possible_lifers_in_a_trip()
        elif choice == 9:
            controllers.print_needs_list()
        else:
            exit(0)
