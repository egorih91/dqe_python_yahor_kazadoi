# assumptions:
# we need to calculate whitespaces before adding the sentence with the last words

import string


text_variable = """
homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
# print(text_variable.lower())


last_sentence = ""
previous_symbol = '.'
whitespaces_counter = 0

string_list = list(text_variable)

for symbol_number in range(0, len(string_list)):
    current_letter = string_list[symbol_number]

    if current_letter.lower() == 'z' \
            and string_list[symbol_number - 1].lower() == 'i' \
            and string_list[symbol_number - 2].lower() in [' ', string.punctuation, string.whitespace, '\n'] \
            and ((symbol_number + 1 < len(string_list)
                  and string_list[symbol_number + 1].lower() in [' ', string.punctuation])
                 or (symbol_number + 1 == len(string_list))
    ):
        current_letter = 's'

    if current_letter in string.ascii_letters and previous_symbol in [':', '.']:
        string_list[symbol_number] = current_letter.upper()
    elif current_letter in string.ascii_letters:
        string_list[symbol_number] = current_letter.lower()

    if current_letter not in string.whitespace:
        previous_symbol = string_list[symbol_number]
    else:
        previous_space_index = symbol_number
        whitespaces_counter += 1

    if current_letter == '.':
        if len(last_sentence) == 0:
            last_sentence = "".join(string_list[previous_space_index + 1:previous_space_index + 2]).upper() + \
                            "".join(string_list[previous_space_index + 2:symbol_number]) + " "
        else:
            last_sentence = last_sentence + "".join(string_list[previous_space_index + 1:symbol_number]) + " "

new_string = "".join(str(x) for x in string_list)

new_string = new_string + "  " + last_sentence[:-1] + "."
# print(type(string_list))


print(new_string)
print(whitespaces_counter)


