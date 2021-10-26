import re
import os
import csv


class WorkingWithResults:

    def __init__(self, file_name='result_file.txt'):
        self.file_name = file_name
        self.list_of_words = []
        self.count_words_dictionary = {}
        self.count_letters_dictionary = {}
        self.file_name_for_words_count = 'statistic_files\\word_count.csv'
        self.file_name_for_letters_count = 'statistic_files\\letter_count.csv'

    def get_list_of_words_from_txt_file(self, directory=None):
        if not directory:  # if directory was not given then use current directory
            directory = os.getcwd()
            # and then create full path to the file with results
            path_full = os.path.join(directory, 'files_with_results', self.file_name)
        else:
            # if the directory was given we use it plus file_name
            path_full = os.path.join(directory, self.file_name)

        if not os.path.isfile(path_full):  # check if the file exists
            raise FileNotFoundError(f"You want to update file that does not exist. Path {path_full} is incorrect")

        with open(path_full, 'r') as file:  # read lines from file
            all_lines = file.readlines()

        string_full = ''
        for line in all_lines:  # exclude rows with the topic of publication and last rows of publications with * only
            if '*' not in line:
                string_full = string_full + line

        replacement_list = ['It is not actual already, it was actual until:', 'Actual until:', 'is winner! Congrats!',
                            'No winner revealed, draw', ' days left']

        for strings in replacement_list:
            string_full = string_full.replace(strings, '')

        words = string_full.split()  # split the string into words

        for word in words:
            if not re.match(r'\d', word):  # looking through the words without numbers
                clear_word = re.sub(r"[^\w\s]", "", word)  # saving only letters without punctuation marks
                if len(clear_word) != 0:
                    self.list_of_words.append(clear_word)  # create list of words

        return self.list_of_words

    # function for counting words in the list of words
    def count_words_in_lower_case(self):
        for word in self.list_of_words:
            lower_word = word.lower()
            if lower_word not in self.count_words_dictionary:
                self.count_words_dictionary[lower_word] = 1
            else:
                self.count_words_dictionary[lower_word] += 1

        return self.count_words_dictionary

    # function for counting letters in the list of words
    def count_letters_in_the_text(self):
        for word in self.list_of_words:
            for symbol in word:
                # all the letters will be stored in lower
                if symbol.lower() not in self.count_letters_dictionary:
                    # if the letter does not exist in the dictionary we add it with default value
                    self.count_letters_dictionary[symbol.lower()] = {'count_all': 1, 'count_uppercase': 0}
                else:  # if the letter exists we just increase count_all value
                    self.count_letters_dictionary[symbol.lower()]['count_all'] += 1
                # also we need to check if this letter in lower case and if not we need to increase count_uppercase
                if symbol.lower() != symbol:
                    self.count_letters_dictionary[symbol.lower()]['count_uppercase'] += 1

        # finally we have dictionary with letter as key and value is the next dictionary with count results
        return self.count_letters_dictionary

    def write_count_of_words_result_to_csv(self):
        # firstly we need to check if the directory exists, and create it if not
        full_path = os.path.join(os.getcwd(), self.file_name_for_words_count)
        path_without_file_name = os.path.split(full_path)[0]
        if not os.path.isdir(path_without_file_name):
            os.mkdir(path_without_file_name)

        # write results using cycle FOR and csv.writer()
        with open(full_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for word, counter in self.count_words_dictionary.items():
                csv_writer.writerow([word, counter])

        print('File with words and their count was updated')

    def write_count_of_letters_with_headers(self):
        # firstly we need to check if the directory exists, and create it if not
        full_path = os.path.join(os.getcwd(), self.file_name_for_letters_count)
        path_without_file_name = os.path.split(full_path)[0]
        if not os.path.isdir(path_without_file_name):
            os.mkdir(path_without_file_name)

        # write results using cycle FOR and csv.DictWriter()
        with open(self.file_name_for_letters_count, 'w', newline='') as file:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            csv_dict_writer = csv.DictWriter(file, fieldnames=headers)
            csv_dict_writer.writeheader()

            for letter, values in self.count_letters_dictionary.items():
                # here we need to create final dictionary to write it and calculate percentage
                new_dict = {
                    'letter': letter,
                    'percentage': round(values['count_uppercase']/values['count_all']*100, 2)
                }

                full_dict = dict(new_dict, **values)  # use this for union of two dictionaries
                csv_dict_writer.writerow(full_dict)  # and then write it to file

        print('File with letters and their count was updated')




