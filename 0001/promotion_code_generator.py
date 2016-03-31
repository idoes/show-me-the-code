"""generate arbitray amount of promotion code"""

import random
import sys

def create_promotion_code(promotion_code):
    choices = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(16):
        promotion_code.append(random.choice(choices))

def write_to_file(nth, promotion_code):
    fileObject = open("result.txt", "ab")
    fileObject.write(nth)
    for item in promotion_code:
        fileObject.write(item)
    fileObject.write("\n")
    fileObject.close()

def start():
    for i in range(int(sys.argv[1])):
        promotion_code = []
        create_promotion_code(promotion_code)

        nth = str(i + 1) + '\n'
        write_to_file(nth, promotion_code)


start()