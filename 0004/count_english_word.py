"""the ' (I'm)
some article is using unicode character
the current solution is not handling that"""
import re
import operator

def program_start():
    # 1 retrieve file into a string object
    file_name = "sample_article.txt"
    file_string_object = open(file_name).read()

    # 2 substitute non English letter into space
    patter_object_digits = re.compile('[0-9]+')
    file_string_object, no_replacement = \
        patter_object_digits.subn("", file_string_object)
    #print file_string_object  # test
    patter_object_nonEnglish = re.compile("[^a-zA-Z'\s]+")
    file_string_object = patter_object_nonEnglish.sub(" ", file_string_object)
    #print file_string_object  # test
    file_string_object_list = file_string_object.split()
    #print file_string_object_list  # test

    # 3 store list into set
    a_dict = dict()
    for item in file_string_object_list:
        if a_dict.has_key(item):
            a_dict[item] = a_dict[item] + 1
        else:
            a_dict[item] = 1

    #print a_dict  # test

    # 4 sort a represetation of a python dictionary
    sorted_a_dict = sorted(a_dict.items(), key=operator.itemgetter(1))
    for item_tuple in sorted_a_dict:
        print item_tuple




program_start()