import random  # import the library for getting random numbers


even_sum = 0  # declare a variable
even_count = 0  # declare a variable
odd_sum = 0  # declare a variable
odd_count = 0  # declare a variable

random_list = []  # declare a variable for our list
number_of_elements_in_list = 100  # number of elements in our list

# adding elements to our list in 'for' loop, number of elements depends on variable that was declared above
for i in range(number_of_elements_in_list):
    random_list.append(random.randint(0, 1000))  # append method for adding element to the end of the list


def sorting_list(some_list):  # function for sorting elements in the list without using sort method
    new_list = []  # a variable for new list that will be in the right order
    for unsorted_x in some_list:  # check each element in the list that need to be sorted
        if not new_list:  # if our new list is empty
            new_list.append(unsorted_x)  # then just add the element to the new list
        else:  # if our new list is not empty

            # then we need to compare the element from the random list with each element in our new list
            for sorted_x in new_list:

                # if element from the random list is smaller then the element from the new list then we just need to
                # add the element to the new list before the current element
                if unsorted_x <= sorted_x:
                    # for inserting in the needed position we use insert method to the position where current element
                    # is located
                    new_list.insert(new_list.index(sorted_x), unsorted_x)
                    break  # and we need to stop checking with other elements
                # but if we compare with all the elements in the new list and all of them are smaller
                # then we need just add the current element to the end of the list
                elif new_list.index(sorted_x) + 1 == len(new_list):
                    new_list.append(unsorted_x)  # again append method is optimal
                    break  # and we need to stop checking with other elements
    return new_list  # and as a result of the function we want to return the new list with sorted values


sorted_list = sorting_list(random_list)  # here we use our function that was described below

for elem in random_list:  # here we go through all the elements in the list
    if elem % 2 == 0:  # checking if the number is even and if yes...
        even_sum += elem  # we add the value to the even sum
        even_count += 1  # we increase the count of the even numbers
    else:  # otherwise
        odd_sum += elem  # we add the value to the odd sum
        odd_count += 1  # we increase the count of the odd numbers

try:  # try block to avoid dividing by zero error
    even_average = round(even_sum / even_count, 2)  # if it is OK we receive an average value
except ZeroDivisionError:  # if we get an error
    even_average = False  # we mark the variable as False

try:  # try block to avoid dividing by zero error
    odd_average = round(odd_sum / odd_count, 2)  # if it is OK we receive an average value
except ZeroDivisionError:  # if we get an error
    odd_average = False  # we mark the variable as False


if even_average:  # check if the variable is not False
    print(f"Even average equals {even_average}")  # then print the average value
else:  # otherwise
    print("No even numbers in the list")  # print message that we do not have even numbers


if odd_average:  # check if the variable is not False
    print(f"Odd average equals {odd_average}")  # then print the average value
else:  # otherwise
    print("No odd numbers in the list")  # print message that we do not have odd numbers

# print the lists just to show that the new list is sorted as expected
print(random_list)
print(sorted_list)
