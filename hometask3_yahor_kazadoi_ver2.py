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

# correct the mistakes with "IZ" with re.sub, the word should start with whitespace and finish after z (word border /b)
text_variable = re.sub(r'\siz\b', ' is', text_variable, 0, re.IGNORECASE)

# find and index where we need to insert one more sentence
place_to_insert = 'it to the END OF this Paragraph.'
index_to_insert = text_variable.find(place_to_insert)+len(place_to_insert)

# to apply correct case I would prefer to split the string to the list
string_list = list(text_variable)

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
new_string = "".join(str(x) for x in string_list)

# to count whitespaces we can use regexp method findall ( \s - all kinds of whitespaces)
# and len of the list equals to the number of whitespaces that were found
whitespaces_counter = len(re.findall(r'\s', new_string))

# to create the sentence that consists of the last words of each sentence I used split method (with default parameter)
# and find all the words that end with dot, append the list with each this word, without last symbol - dot ([:-1]
# and the join the in the one string using space, and capitalize the sentence
last_sentence = []
for word in new_string.split():
    if word.endswith('.'):
        last_sentence.append(word[:-1])
last_sentence_string = ' '.join(last_sentence).capitalize()+'.'

# to get the final string we need to insert our last sentence in the correct place
# we can use this structure [:] to split the first string in the correct place
new_string_final = f"{new_string[:index_to_insert]} {last_sentence_string} {new_string[index_to_insert:]}"

# print the results
print(new_string_final)
print(whitespaces_counter)







