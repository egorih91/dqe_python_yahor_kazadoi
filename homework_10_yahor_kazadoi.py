from files_for_use.class_for_csv_tasks import WorkingWithResults
from files_for_use.publication_classes import News, PrivateAd, SportResult, FillingFromText, JsonPublication, \
    XmlPublication
from files_for_use.working_with_db_class import WorkingWithDb

if __name__ == '__main__':
    type_of_publication = input("""
Print the category number of the publication
1 - news
2 - private ad
3 - sport result
4 - information from text file 
5 - load from json
6 - load data from xml\n""")

    if type_of_publication == '1':
        new_publication = News()
    elif type_of_publication == '2':
        new_publication = PrivateAd()
    elif type_of_publication == '3':
        new_publication = SportResult()
    elif type_of_publication == '4':
        new_publication = FillingFromText()
    elif type_of_publication == '5':
        new_publication = JsonPublication()
    elif type_of_publication == '6':
        new_publication = XmlPublication()
    else:
        raise ValueError("We don't have information about this category of the publication")

    new_publication.fulfil_the_content()
    results_len, result_list_for_db = new_publication.print_result()

    if results_len != 0:  # check if some rows were added to the result file
        # adding data to db using the class that was imported
        adding_to_db = WorkingWithDb(result_list_for_db)
        adding_to_db.adding_data_to_db()

        result_work = WorkingWithResults()  # create object for working with the results
        result_work.get_list_of_words_from_txt_file()  # get list of words from the text

        result_work.count_words_in_lower_case()  # count words
        result_work.count_letters_in_the_text()  # count letters

        result_work.write_count_of_words_result_to_csv()  # write result of words counting
        result_work.write_count_of_letters_with_headers()  # write result of letters counting
    else:
        print('Content of files with publications were not updated')
