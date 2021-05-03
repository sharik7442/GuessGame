# PYTHON PROBLEM 9

import random

'''
AUTHOR : SHARIK ANSARI
PROGRAME : JUMBLE WORDS 
DATE : 25-04-2021

'''


def jumble_words(first_name, last_name, number):
    for i in range(0, number):
        joumbled_name = first_name[i] + " " + last_name[random.randint(0, number - 1)]
        print(joumbled_name)


if __name__ == "__main__":
    number = int(input("Enter the number of names\n"))
    namelist = []
    first_name = []
    last_name = []

    for i in range(1, number + 1):
        name = input("Enter the name\n")
        namelist.append(name)

        split_name = ele.split(" ")
        first_name.append(split_name[0])
        last_name.append(split_name[1])

    jumble_words(first_name, last_name, number)
