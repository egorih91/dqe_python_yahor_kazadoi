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


number_of_dictionaries = random.randint(2, 10)  # generate number of dictionaries that we will need to create
dict_counter=0  # counter for dictionaries
list_of_dictionaries = []  # declare variable for list of dictionaries
dictionary_for_analysis = {}  # create a dictionary for grouping all the dictionaries from the list into one
result_dictionary = {}  # create a dictionary for the result dictionary

# cycle for adding dictionaries to the list
for dict_counter in range(0, number_of_dictionaries):
    number_of_letters = random.randint(1, 26)  # randomize the number of letters in the dictionary
    key_counter = 0  # declare counter for the keys
    temp_dictionary = {}  # declare empty dictionary that will be added to the list

    # we use while cycle to add key-value values to the dictionary as much time as wee need (number_of_letters)
    while key_counter in range(0, number_of_letters):
        letter = random.choice(string.ascii_lowercase)  # randomize the letter for the key
        if letter not in temp_dictionary:  # check if we do not have this key already, and if not...
            temp_dictionary[letter] = random.randint(0, 100)  # then we add key-value (letter + random int 0-100)
            key_counter += 1  # increase the counter
    list_of_dictionaries.append(temp_dictionary)  # add the dictionary to the list
    dict_counter += 1  # increase the counter

for d in list_of_dictionaries:  # going through all the dictionaries
    for key, value in d.items():  # going through each key-value pair
        if key in dictionary_for_analysis.keys():  # if the key already exists...
            dictionary_for_analysis[key]['count'] = dictionary_for_analysis[key]['count'] + 1  # increase the count val
            if dictionary_for_analysis[key]['max_value'] < value:  # and check if the current value more than existing
                # if yes then update the dictionary_with_max_value
                dictionary_for_analysis[key]['dictionary_with_max_value'] = list_of_dictionaries.index(d) + 1
                dictionary_for_analysis[key]['max_value'] = value  # update the max value
        else:  # if the key doesn't exist...
            dictionary_for_analysis[key] = {'count': 1}  # add dictionary with the key = 'count' with value = 1
            # add number of the dictionary with the key = 'dictionary_with_max_value'
            dictionary_for_analysis[key]['dictionary_with_max_value'] = list_of_dictionaries.index(d)+1
            # add the value with the key 'max_value'
            dictionary_for_analysis[key]['max_value'] = value

# going through all the key-value pairs in the dictionary_for_analysis
for key, value in dictionary_for_analysis.items():
    if value['count'] == 1:  # if th count = 1...
        result_dictionary[key] = value['max_value']  # just add the key as is and value equal to the max_value
    else:  # if not
        # in this case we need to create the key from the key plus value from dictionary_with_max_value, value as above
        result_dictionary[f"{key}_{value['dictionary_with_max_value']}"] = value['max_value']

# print the list with the dictionaries and the result
print(list_of_dictionaries)
print(result_dictionary)
