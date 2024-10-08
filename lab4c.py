#!/usr/bin/env python3
# Author ID- isingh176

def create_dictionary(keys, values):
    # Accepts two lists as arguments and combines them into a dictionary
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary

def shared_values(dict1, dict2):
    # Accepts two dictionaries as arguments and finds all values shared by both
    return set(dict1.values()).intersection(set(dict2.values()))

if __name__ == '__main__':
    dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
    dict_newham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J1G5'}
    
    list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
    list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']
    
    york = create_dictionary(list_keys, list_values)
    print('York:', york)
    
    common = shared_values(dict_york, dict_newham)
    print('Shared Values:', common)

