# needed imports
import re
import datetime
import os
import sys
import json
# import functions from previous homeworks
from files_for_use.homework_4_3_yahor_kazadoi import case_modifying


# parent class
# it includes all the variables and methods that we need in child classes
class Publication:
    def __init__(self):
        self.result_list = []
        self.publication_type = ""
        self.number_of_publications = 0
        self.folder_for_files_with_publications = 'files_for_publications'
        self.path_to_file_with_result = os.path.join(os.getcwd(), 'files_with_results', 'result_file.txt')

    # a method for checking if additional arguments come to us and we need to use them as path, or not
    def creating_path_to_file(self):
        if len(sys.argv) > 1:
            path_for_searching_files = sys.argv[1]
            # if the path does not exist we raise an error
            if not os.path.exists(sys.argv[1]):
                raise ValueError(f"Your path {sys.argv[1]} does not exist")
        else:  # if we do not have additional arguments we use default path (current dir + folder_for_publications)
            folder_for_publications = self.folder_for_files_with_publications
            path_for_searching_files = os.path.join(os.getcwd(), folder_for_publications)
        return path_for_searching_files

    def creating_first_string(self):
        str1 = self.publication_type.title() + " "
        full_string_1 = f"{str1.ljust(30, '*')}"
        return full_string_1

    # it was decided to split method into two steps
    def input_information(self):
        pass  # empty method that should be overridden in the child classes

    def adding_to_list(self):
        pass  # empty method that should be overridden in the child classes

    def fulfil_the_content(self):
        self.input_information()
        self.adding_to_list()

    # method that can be used in different classes
    def enter_the_text(self):
        text = input(f"What is the text of the {self.publication_type}? \n")
        return text

    # method that is common for all the child classes
    # all that we need to have a list with the same structure (list with strings inside)
    def insert_strings_into_file(self, list_with_strings):
        with open(self.path_to_file_with_result, 'a', encoding='utf-8') as file:
            for elem in list_with_strings:
                file.write(f"{case_modifying(elem)}\n")
            file.write(f"{''.ljust(30, '*')}\n\n\n")

    def print_result(self):
        if len(self.result_list) == 0:
            print('No new files for publication')
        else:  # otherwise we going through lists in the result_list
            # checking if the directory exist and creating it if not
            if not os.path.exists(os.path.split(self.path_to_file_with_result)[0]):
                os.mkdir(os.path.split(self.path_to_file_with_result)[0])
            for result in self.result_list:
                self.insert_strings_into_file(result)
        return len(self.result_list)


# child class for news
class News(Publication):
    def __init__(self):
        super().__init__()
        self.publication_type = "news"
        self.text = ''
        self.city = ''

    def input_information(self):
        self.text = self.enter_the_text()
        self.city = input("City? \n")

    def adding_to_list(self):
        # getting current date and convert it to sting with the needed format
        current_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')

        self.result_list.append([])
        self.result_list[self.number_of_publications].append(self.creating_first_string())
        self.result_list[self.number_of_publications].append(self.text)
        self.result_list[self.number_of_publications].append(self.city)
        self.result_list[self.number_of_publications].append(current_date)


# child class for ad
class PrivateAd(Publication):
    def __init__(self):
        super().__init__()
        self.publication_type = "private ad"
        self.text = ''
        self.expiration_date_str = ''

    def input_information(self):
        self.text = self.enter_the_text()
        self.expiration_date_str = input("When is the expiration date? \nInsert the date in the next format "
                                         "yyyy-mm-dd\n")

    def adding_to_list(self):
        # checking if the date correct
        check_date_format = re.match(r"(20[0-9]\d)-([\d]{2})-([\d]{2})", self.expiration_date_str)
        if not bool(check_date_format):
            raise ValueError("The date format is incorrect")

        # converting string to date format
        expiration_date = datetime.datetime.strptime(self.expiration_date_str, '%Y-%m-%d').date()
        # calculating days difference
        days_left = (expiration_date - datetime.date.today()).days

        # checking if difference positive or not, message depends on this result
        if days_left >= 0:
            second_string = f"Actual until: {expiration_date}, {days_left} days left"
        else:
            second_string = f"It is not actual already, it was actual until: {expiration_date}"

        self.result_list.append([])
        self.result_list[self.number_of_publications].append(self.creating_first_string())
        self.result_list[self.number_of_publications].append(self.text)
        self.result_list[self.number_of_publications].append(second_string)


# child class for sport result
class SportResult(Publication):
    def __init__(self):
        super().__init__()
        self.publication_type = "sport result"
        self.game_result = ''
        self.kind_of_sport = ''
        self.participant1 = ''
        self.participant2 = ''

    def input_information(self):
        self.kind_of_sport = input("Enter the sport (only sports with two participants fit)\n")
        self.participant1 = input("Enter the first participant\n")
        self.participant2 = input("Enter the second participant\n")
        self.game_result = input("Enter the result in the next format '1-0','56-88' etc.\n")

    def adding_to_list(self):
        participants = [self.participant1, self.participant2]
        # checking that result is in correct format
        check_result_format = re.match(r"[\d]+-[\d]", self.game_result)
        if not bool(check_result_format):
            raise ValueError("The format of the result is inappropriate")

        string1 = f"{self.kind_of_sport.title()}"
        string2 = f"{self.participant1}:{self.participant2}, result {self.game_result}"
        # using function to determine the winner using the class method
        result = self.determining_the_winner()

        # creating the row in dependency of the previous result
        if result == 3:
            string3 = "No winner revealed, draw"
        else:
            string3 = f"{participants[result]} is WINNER! Congrats!"

        self.result_list.append([])
        self.result_list[self.number_of_publications].append(self.creating_first_string())
        self.result_list[self.number_of_publications].append(string1)
        self.result_list[self.number_of_publications].append(string2)
        self.result_list[self.number_of_publications].append(string3)

    def determining_the_winner(self):
        res1 = self.game_result.split('-')[0]
        res2 = self.game_result.split('-')[1]
        if res1 > res2:
            return 0
        elif res2 > res1:
            return 1
        else:
            return 3


# child class for publications from txt files
class FillingFromText(Publication):
    def __init__(self):
        super().__init__()
        self.publication_type = "Text information"

    def fulfil_the_content(self):
        path_for_searching_files = self.creating_path_to_file()

        counter = 0
        # going through the folder, searching for the txt files
        for one_file in os.listdir(path_for_searching_files):  # we expect that one file = one publication
            if one_file.endswith('.txt'):  # if true - read file row by row, and then remove
                self.result_list.append([])
                file_path = os.path.join(path_for_searching_files, one_file)
                self.result_list[counter].append(self.creating_first_string())
                with open(file_path, 'r') as f:
                    for line in f:
                        self.result_list[counter].append(line.replace('\n', ''))
                counter += 1
                os.remove(file_path)


# it was decided to create class with multiple inheritance
class JsonPublication(News, PrivateAd, SportResult):
    def __init__(self):
        super(JsonPublication, self).__init__()
        self.json_data = {}

    # describe methods adding_to_list from all the parent classes
    def adding_to_list_news(self):
        News.adding_to_list(self)

    def adding_to_list_ad(self):
        PrivateAd.adding_to_list(self)

    def adding_to_list_sport(self):
        SportResult.adding_to_list(self)

    # override the method fulfil_the_content for json files
    def fulfil_the_content(self):
        # create local variable for the list with all the results
        # we will add information here only all the file was proceed correctly
        full_result = []

        path_for_searching_files = self.creating_path_to_file()

        # directory_local = os.getcwd()
        # full_path_local = os.path.join(directory_local, 'files_for_publications', 'test_json.json')

        # going through the directory and searching for the json files
        for one_file in os.listdir(path_for_searching_files):
            if one_file.endswith('.json'):
                # if the json file was found redefine two self variables to the start values
                self.result_list = []
                self.number_of_publications = 0

                # delete file has default value 1, it should be switched tp 0 if something goes wrong with the file
                delete_flag = 1

                file_path = os.path.join(path_for_searching_files, one_file)

                with open(file_path, 'r') as f:
                    json_data = json.loads(f.read())

                # if something goes wrong try helps us to avoid the crash of the program
                try:
                    for key, value in json_data.items():
                        if value['publication_type'] == 'news':
                            self.publication_type = 'News'
                            self.text = value['text']
                            self.city = value['city']
                            self.adding_to_list_news()
                            self.number_of_publications += 1
                        elif value['publication_type'] == 'ad':
                            self.publication_type = 'Private ad'
                            self.text = value['text']
                            self.expiration_date_str = value['date']
                            self.adding_to_list_ad()
                            self.number_of_publications += 1
                        elif value['publication_type'] == 'sport_result':
                            self.publication_type = 'sport result'
                            self.game_result = value['game_result']
                            self.kind_of_sport = value['kind_of_sport']
                            self.participant1 = value['participant1']
                            self.participant2 = value['participant2']
                            self.adding_to_list_sport()
                            self.number_of_publications += 1
                        else:
                            delete_flag = 0
                except KeyError:
                    delete_flag = 0
                except ValueError:
                    delete_flag = 0

                # if the delete_flag was not overwritten we can remove the file and add the results to the local
                # variable full_result
                if delete_flag == 1:
                    for included_list in self.result_list:
                        full_result.append(included_list)
                    os.remove(file_path)
                else:  # otherwise this file shouldn't be removed and
                    # the results from this file should not be added to the final result file
                    print(f"File {one_file} has incorrect structure, data from the file were not added to the result "
                          f"file")

        # after all the files will be checked redefine self.result_list variable from local variable full_result
        self.result_list = full_result
