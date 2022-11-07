print("**********************PROGRAMMED BY***********************")
print("***************Kevin Joseph G. Concepcion*****************")
print("***********************BSCOE 2-2**************************")

nos_list = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]

def menu_options():
    print("\n>>>>>>>> MENU <<<<<<<<")
    print("1 -> Add an Element")
    print("2 -> Insert an Element")
    print("3 -> Modify an Element")
    print("4 -> Delete an Element")
    print("5 -> Arrange in Ascending Order")
    print("6 -> Arrange in Descending Order")
    print("7 -> Find the Smallest Number")
    print("8 -> Find the Biggest Number")
    print("9 -> Find the Sum of all the Elements")
    print("10 -> Count how many times an element appeared")
    print("11 -> Count how many elements in the list")
    print("12 -> Pop an element")
    print("13 -> Exit")

while True:
    menu_options()
    print("\nThese are the random numbers:",nos_list)

    user_input = int(input("\nPlease input the command that you would like to execute: "))
    if user_input == 1:
        add_number = int(input("Enter the element that you wish to add to the list: "))
        nos_list.append(add_number)
        print("\nThis is the number that you have added to the list:", add_number)
        print("This is the new list that you have created: ", nos_list)

    elif user_input == 2:
        ins_number = int(input("Enter the element that you wish to insert in the list: "))
        ins_index = int(input("Enter the index location that you wish to insert the element: "))
        if ins_index <= 9:
            nos_list.insert(ins_index, ins_number)
            print("\nThis is the new list that you have created: ", nos_list)
            print("Thank you for giving this program a chance.")

        else:
            print("\nI am sorry, the index that you entered is invalid")
            print("Thank you for giving this program a chance.")
            break

    elif user_input == 3:
        mod_number = int(input("Enter your number of choice to replace the element: "))
        ins_index = int(input("Enter the index location that you wish to insert the element: "))
        if ins_index <= 9:
            nos_list[ins_index] = mod_number
            print("\nThis is the new list that you have created: ", nos_list)

        else:
            print("\nI am sorry, the index that you entered is invalid.")
            print("Thank you for giving this program a chance.")
            break

    elif user_input == 4:
        rem_number = int(input("Enter the element you wish to remove from the list: "))
        for x in range(len(nos_list)):
            if nos_list[x] == rem_number:
                user_mistake = str("none")
                break

            else:
                user_mistake = str("100%")

        if user_mistake == "none":
            nos_list.remove(rem_number)
            print("\nThis is the new list that you have created:",nos_list)

        else:
            print("\nI am sorry, the number you entered is not in the list.")
            print("Thank you for giving this program a chance.")
            break

    elif user_input == 5:
        nos_list.sort()
        print("\nThis is the new list that you have created:",nos_list)

    elif user_input == 6:
        nos_list.sort()
        nos_list.reverse()
        print("\nThis is the new list that you have created:",nos_list)

    elif user_input == 7:
        smallest_num = min(nos_list)
        print("\nThis is the smallest number in the list:",smallest_num)

    elif user_input == 8:
        biggest_num = max(nos_list)
        print("\nThis is the biggest number in the list:",biggest_num)

    elif user_input == 9:
        sum_list = sum(nos_list)
        print("\nThis is the total sum of all the elements in the list:",sum_list)

    elif user_input == 10:
        count_num = int(input("Enter the element you wish to count(only within the list): "))
        count_list = nos_list.count(count_num)
        print("The number of time/s that", count_num, "appeared in the list is", count_list)

    elif user_input == 11:
        length_list = len(nos_list)
        print("The number of elements in the list is",length_list)

    elif user_input == 12:
        pop_index = int(input("Enter the index location of the element that you wish to pop: "))
        if pop_index <= 9:
            nos_list.pop(pop_index)
            print("This is the new list that you have created:",nos_list)

        else:
            print("\nI am sorry, the index that you entered is invalid.")
            print("Thank you for giving this program a chance.")
            break

    elif user_input == 13:
        print("\nThank you for giving this program a chance.")
        break

    else:
        print("\nInvalid command.")
        break

    add_question = input("\nWould you like to try again?(Y/N): ")
    ans = add_question.capitalize()
    if ans == "Y":
        continue
    else:
        print("\nThank you for giving this program a chance.")
        break