# needed imports
import re
import datetime
import os
import sys
# import functions from previous homeworks
from files_for_use.homework_4_3_yahor_kazadoi import case_modifying
from files_for_use.class_for_csv_tasks import WorkingWithResults


# parent class
# it includes all the variables and methods that we need in child classes
class Publication:
    def __init__(self):
        self.result_list = []
        self.publication_type = ""

    def fulfil_the_content(self):
        pass  # empty method that should be overridden in the child classes

    # method that can be used in different classes
    def enter_the_text(self):
        text = input(f"What is the text of the {self.publication_type}? \n")
        return text

    # method that is common for all the child classes
    # all that we need to have a list with the same structure (list with strings inside)
    def insert_strings_into_file(self, list_with_strings):
        with open('result_file.txt', 'a', encoding='utf-8') as file:
            str1 = self.publication_type.title() + " "

            file.write(f"{str1.ljust(30, '*')}\n")
            for elem in list_with_strings:
                file.write(f"{case_modifying(elem)}\n")
            file.write(f"{''.ljust(30, '*')}\n\n\n")

    def print_result(self):
        if len(self.result_list) == 0:
            print('No new files for publication')
        elif isinstance(self.result_list[0], str):  # if our list contains only strings we insert them to the final file
            self.insert_strings_into_file(self.result_list)
        else:  # otherwise we going through lists in the result_list
            for result in self.result_list:
                self.insert_strings_into_file(result)
        return len(self.result_list)


# child class for news
class News(Publication):
    def __init__(self):
        super().__init__()
        self.publication_type = "news"

    def fulfil_the_content(self):
        self.result_list.append(self.enter_the_text())
        self.result_list.append(input("City? \n"))
        # getting current date and convert it to sting with the needed format
        current_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')
        self.result_list.append(current_date)


# child class for ad
class PrivateAd(Publication):
    def __init__(self):
        super().__init__()
        self.publication_type = "private ad"

    def fulfil_the_content(self):
        text = self.enter_the_text()

        expiration_date_str = input("When is the expiration date? \nInsert the date in the next format yyyy-mm-dd\n")

        # checking if the date correct
        check_date_format = re.match(r"(20[0-9]\d)-([\d]{2})-([\d]{2})", expiration_date_str)
        if not bool(check_date_format):
            raise ValueError("The date format is incorrect")

        # converting string to date format
        expiration_date = datetime.datetime.strptime(expiration_date_str, '%Y-%m-%d').date()
        # calculating days difference
        days_left = (expiration_date - datetime.date.today()).days

        # checking if difference positive or not, message depends on this result
        if days_left >= 0:
            second_string = f"Actual until: {expiration_date}, {days_left} days left"
        else:
            second_string = f"It is not actual already, it was actual until: {expiration_date}"

        self.result_list.append(text)
        self.result_list.append(second_string)


# child class for sport result
class SportResult(Publication):
    def __init__(self):
        super().__init__()
        self.publication_type = "sport result"
        self.game_result = ''

    def fulfil_the_content(self):
        kind_of_sport = input("Enter the sport (only sports with two participants fit)\n")
        participant1 = input("Enter the first participant\n")
        participant2 = input("Enter the second participant\n")
        participants = [participant1, participant2]
        self.game_result = input("Enter the result in the next format '1-0','56-88' etc.\n")
        # checking that result is in correct format
        check_result_format = re.match(r"[\d]+-[\d]", self.game_result)
        if not bool(check_result_format):
            raise ValueError("The format of the result is inappropriate")

        string1 = f"{kind_of_sport.title()}"
        string2 = f"{participant1}:{participant2}, result {self.game_result}"
        # using function to determine the winner using the class method
        result = self.determining_the_winner()
        # creating the row in dependency of the previous result
        if result == 3:
            string3 = "No winner revealed, draw"
        else:
            string3 = f"{participants[result]} is WINNER! Congrats!"
        self.result_list.append(string1)
        self.result_list.append(string2)
        self.result_list.append(string3)

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
        # if we get some argument we try to use it as a path
        if len(sys.argv) > 1:
            path_for_searching_files = sys.argv[1]
            # if the path does not exist we raise an error
            if not os.path.exists(sys.argv[1]):
                raise ValueError(f"Your path {sys.argv[1]} does not exist")
        else:  # if we do not have additional arguments we use default path (current dir + folder_for_publications)
            folder_for_publications = 'files_for_publications'
            path_for_searching_files = os.path.join(os.getcwd(), folder_for_publications)

        counter = 0
        # going through the folder, searching for the txt files
        for one_file in os.listdir(path_for_searching_files):  # we expect that one file = one publication
            if one_file.endswith('.txt'):  # if true - read file row by row, and then remove
                self.result_list.append([])
                file_path = os.path.join(path_for_searching_files, one_file)
                with open(file_path, 'r') as f:
                    for line in f:
                        self.result_list[counter].append(line.replace('\n', ''))
                counter += 1
                os.remove(file_path)







if __name__ == '__main__':
    type_of_publication = input("""
Print the category number of the publication
1 - news
2 - private ad
3 - sport result
4 - information from text file \n""")

    if type_of_publication == '1':
        new_publication = News()
    elif type_of_publication == '2':
        new_publication = PrivateAd()
    elif type_of_publication == '3':
        new_publication = SportResult()
    elif type_of_publication == '4':
        new_publication = FillingFromText()
    else:
        raise ValueError("We don't have information about this category of the publication")

    new_publication.fulfil_the_content()
    results = new_publication.print_result()

    if results != 0:  # check if some rows were added to the result file
        result_work = WorkingWithResults()  # create object for working with the results
        result_work.get_list_of_words_from_txt_file()  # get list of words from the text

        result_work.count_words_in_lower_case()  # count words
        result_work.count_letters_in_the_text()  # count letters

        result_work.write_count_of_words_result_to_csv()  # write result of words counting
        result_work.write_count_of_letters_with_headers()  # write result of letters counting
    else:
        print('Content of files with publications were not updated')











