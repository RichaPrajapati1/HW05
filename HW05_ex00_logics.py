#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    num_input = raw_input("Enter a number: ")
    try:
        num = int(num_input)
    except:
        print("Enter a valid number!")
    else:
        if num%2 == 0:
            print("The number is even")
        else:
            print("The number is odd")


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    num = 1
    for row in range(10):
        for column in range(10):
            if num <= 10:
                print str(num) +' ',
            else:
                print num,
            num += 1
        print ('')



def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    sum_num = 0
    count = 0
    num_input = raw_input("Enter a number: ")
    while num_input != 'done':
        sum_num += int(num_input)
        count += 1
        num_input = raw_input("Enter another number: ")
    if count != 0:
        avg = float(sum_num)/count
    else:
        avg = 0
    print ("Average is: %.2f") % (avg)




##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    # even_odd()
    # ten_by_ten()
    find_average()

if __name__ == '__main__':
    main()
