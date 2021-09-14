import random  # import the library for getting random numbers


random_list = []  # declare a variable for our list
new_list = []  # a variable for new list that will be in the right order
even_list = []  # list for even numbers
odd_list = []  # list for odd numbers
number_of_elements_in_list = 100  # number of elements in our list


random_list = random.sample(list(range(0, 1000)), number_of_elements_in_list)  # create list of values from range 0-1000


i = 0  # variable for counter in random_list
while i < number_of_elements_in_list:  # repeat all the actions until our counter will be equal to number of elements
    u = 0  # variable for elements in new_list
    if not new_list:  # if our new list is empty
        new_list.append(random_list[i])  # then just add the element to the new list
    else:  # if our new list is not empty
        # then we need to compare the element from the random list with each element in our new list
        while random_list[i] not in new_list:
            # if element from the random list is smaller then the element from the new list then we just need to
            # add the element to the new list before the current element
            if random_list[i] <= new_list[u]:
                # for inserting in the needed position we use insert method to the position where current element
                # is located
                new_list.insert(new_list.index(new_list[u]), random_list[i])
            # but if we compare with all the elements in the new list and all of them are smaller
            # then we need just add the current element to the end of the list
            elif new_list.index(new_list[u]) + 1 == len(new_list):
                new_list.append(random_list[i])  # again append method is optimal
            u += 1  # increase the counter for new list

    if random_list[i] % 2 == 0:  # checking if the number is even and if yes...
        even_list.append(random_list[i])  # add the element to the even list using append method
    else:  # otherwise
        odd_list.append(random_list[i])  # add the element to the odd list using append method

    i += 1  # increase the counter for random list

try:  # try block to avoid dividing by zero error
    even_average = round(sum(even_list) / len(even_list), 2)  # if it is OK we receive an average value
    print(f"Even average equals {even_average}")  # then print the average value
except ZeroDivisionError:  # if we get an error
    print("No even numbers in the list")  # print message that we do not have even numbers

try:  # try block to avoid dividing by zero error
    odd_average = round(sum(odd_list) / len(odd_list), 2)  # if it is OK we receive an average value
    print(f"Odd average equals {odd_average}")  # then print the average value
except ZeroDivisionError:  # if we get an error
    print("No odd numbers in the list")  # print message that we do not have odd numbers


# print the lists just to show that the new list is sorted as expected
print(random_list)
print(new_list)
