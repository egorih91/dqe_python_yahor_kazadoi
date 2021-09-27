# assumptions
# 1. if we have more then one key with the same value we save the first of the values
# 2. we only use letters in the lowercase
""" 3. after we have number of letters that should be in the dictionary
we need to check if the random letter does not exist in the dictionary
and if it is already exists we need to use another letter
"""

# import libraries that is needed
import random  # for random values
import string  # for working with letters


# function for adding dictionaries to the list and list of dictionaries will be returned
def adding_dictionaries_to_list(dictionary_count):
    list_of_dictionaries_full = []  # declare variable for list of dictionaries
    dict_counter = 0  # counter for dictionaries
    while dict_counter < dictionary_count:
        number_of_letters = random.randint(1, 26)  # randomize the number of letters in the dictionary
        key_counter = 0  # declare counter for the keys
        temp_dictionary = {}  # declare empty dictionary that will be added to the list

        # we use while cycle to add key-value values to the dictionary as much time as wee need (number_of_letters)
        while key_counter in range(0, number_of_letters):
            letter = random.choice(string.ascii_lowercase)  # randomize the letter for the key
            if letter not in temp_dictionary:  # check if we do not have this key already, and if not...
                temp_dictionary[letter] = random.randint(0, 100)  # then we add key-value (letter + random int 0-100)
                key_counter += 1  # increase the counter
        list_of_dictionaries_full.append(temp_dictionary)  # add the dictionary to the list
        dict_counter += 1  # increase the counter
    return list_of_dictionaries_full


# function for going through the dictionary and creating dictionary with the full result (that will be returned)
# default value for dict_for_analysis is set for the first run when the dictionary does not exist
def creating_dictionary_with_all_values(dictionary, dict_for_analysis=None):
    # pep8 recommends not to use mutable object as default parameter but use it as None
    # and then declare empty dictionary if needed
    if dict_for_analysis is None:
        dict_for_analysis = {}
    for dict_key, val in dictionary.items():  # going through each key-value pair
        if dict_key in dict_for_analysis.keys():  # if the key already exists...
            dict_for_analysis[dict_key]['count'] = dict_for_analysis[dict_key]['count'] + 1  # increase the count val
            if dict_for_analysis[dict_key]['max_value'] < val:  # check if the current value more than existing
                # if yes then update the dictionary_with_max_value
                dict_for_analysis[dict_key]['dictionary_with_max_value'] = list_of_dictionaries.index(dictionary) + 1
                dict_for_analysis[dict_key]['max_value'] = val  # update the max value
        else:  # if the key doesn't exist...
            dict_for_analysis[dict_key] = {'count': 1}  # add dictionary with the key = 'count' with value = 1
            # add number of the dictionary with the key = 'dictionary_with_max_value'
            dict_for_analysis[dict_key]['dictionary_with_max_value'] = list_of_dictionaries.index(dictionary)+1
            # add the value with the key 'max_value'
            dict_for_analysis[dict_key]['max_value'] = val
    return dict_for_analysis


# going through all the key-value pairs in the dictionary_for_analysis
# and return the dictionary with the result
def creating_result_dictionary(dictionary_for_analysis):
    result_dictionary = {}  # create a dictionary for the result dictionary
    for key, value in dictionary_for_analysis.items():
        if value['count'] == 1:  # if th count = 1...
            result_dictionary[key] = value['max_value']  # just add the key as is and value equal to the max_value
        else:  # if not
            # in this case we need to create the key from the key plus value from dictionary_with_max_value
            result_dictionary[f"{key}_{value['dictionary_with_max_value']}"] = value['max_value']
    return result_dictionary


number_of_dictionaries = random.randint(2, 10)  # generate number of dictionaries that we will need to create

# here we use function for creating list of dictionaries (we have to know only how many dictionaries we need)
list_of_dictionaries = adding_dictionaries_to_list(number_of_dictionaries)

# going through all the dictionaries using the functions
for one_dict in list_of_dictionaries:
    if 'dictionary_for_analysis_full' in globals():  # if the variable already exists we run the function with it
        dictionary_for_analysis_full = creating_dictionary_with_all_values(one_dict, dictionary_for_analysis_full)
    else:  # otherwise we run with one parameter and then the variable will appear
        dictionary_for_analysis_full = creating_dictionary_with_all_values(one_dict)

# here we use function that analyse dictionary_for_analysis_full and create the final dictionary that we need
final_result_dictionary = creating_result_dictionary(dictionary_for_analysis_full)

# print the list with the dictionaries and the result
print(list_of_dictionaries)
print(final_result_dictionary)
