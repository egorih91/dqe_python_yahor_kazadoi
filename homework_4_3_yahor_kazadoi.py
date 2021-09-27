# assumptions:
# we need to calculate whitespaces before adding the sentence with the last words

# import libraries that we need
import re
import string

# declare string that is needed for the task
text_variable = """
homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


# function to fix the mistakes with "IZ" using re.sub
def fix_iz_mistake(some_string):
    fixed_string = re.sub(r'\siz\b', ' is', some_string, 0, re.IGNORECASE)
    return fixed_string


# function for modifying case of letters
def case_modifying(some_string):
    # to apply correct case I would prefer to split the string to the list
    string_list = list(some_string)
    # the previous symbol for the first letter just to have it in Upper case
    previous_symbol = '.'
    # analyze each symbol one by one using for and range to have an ability refer to a symbol by its index
    # the case depends on the last not-whitespace symbol
    for symbol_number in range(0, len(string_list)):
        current_letter = string_list[symbol_number]

        if current_letter in string.ascii_letters and previous_symbol in [':', '.']:
            string_list[symbol_number] = current_letter.upper()
        elif current_letter in string.ascii_letters:
            string_list[symbol_number] = current_letter.lower()

        if current_letter not in string.whitespace:
            previous_symbol = string_list[symbol_number]

    # then get back from the list to the sting using join method
    beautiful_string = "".join(str(x) for x in string_list)
    return beautiful_string


# function for creating sentence that consists of the last words from each sentence
def creating_sentence_from_last_words(some_string):
    last_sentence = []
    for word in some_string.split():
        if word.endswith('.'):
            last_sentence.append(word[:-1])
    last_sentence_string = ' '.join(last_sentence).capitalize()+'.'
    return last_sentence_string


# function for inserting string inside another text,
# and with the parameter after which we need to insert it, with default parameter
def inserting_sentence_where_needed(text, string_to_insert, place_to_insert='it to the end of this paragraph.'):
    index_to_insert = text_variable.find(place_to_insert) + len(place_to_insert)
    result_string = f"{text[:index_to_insert]} {string_to_insert} {text[index_to_insert:]}"
    return result_string


# fixing the mistakes with "IZ"
text_variable = fix_iz_mistake(text_variable)

# modifying case
nice_string = case_modifying(text_variable)

# count whitespaces (I thinks it is not needed to create a function for one row)
whitespaces_counter = len(re.findall(r'\s', nice_string))

# creating needed sentence
last_word_sentence = creating_sentence_from_last_words(nice_string)

# adding last_word_sentence, to the nice_string, place where to insert is used as default value
new_string_final = inserting_sentence_where_needed(nice_string, last_word_sentence)

# print the results
print(new_string_final)
print(whitespaces_counter)

