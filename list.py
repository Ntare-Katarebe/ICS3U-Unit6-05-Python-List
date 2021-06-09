#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: June 2021
# This program uses a list


def avg_of_numbers(mark):
    # this function finds the averqge of elements in a 2D array

    sum_of_all_numbers = 0
    for loop_counter in mark:
        sum_of_all_numbers += loop_counter

    return sum_of_all_numbers // len(mark)


def main():
    # this function uses a list

    mark = []
    n = 0

    # input
    print("Please enter 1 word at a time. Enter -1 to end.")

    try:
        while(True):
            n = int(input("What is your mark? (as %): "))
            if (n == -1):
                break
            mark.append(n)

        print("The average is {0}%.".format(avg_of_numbers(mark)))

    except Exception:
        print("That was not a mark please try again")


if __name__ == "__main__":
    main()
