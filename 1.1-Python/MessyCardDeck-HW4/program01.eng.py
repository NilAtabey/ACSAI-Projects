#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
The objective of the homework assignment is to design and implement a function
that reads some strings contained in a series of files and generates a new
string from all the strings read.
The strings to be read are contained in several files, linked together to
form a closed chain. The first string in each file is the name of another
file that belongs to the chain: starting from any file and following the
chain, you always return to the starting file.

Example: the first line of file "A.txt" is "B.txt," the first line of file
"B.txt" is "C.txt," and the first line of "C.txt" is "A.txt," forming the 
chain "A.txt"-"B.txt"-"C.txt".

In addition to the string with the name of the next file, each file also
contains other strings separated by spaces, tabs, or carriage return 
characters. The function must read all the strings in the files in the chain
and construct the string obtained by concatenating the characters with the
highest frequency in each position. That is, in the string to be constructed,
at position p, there will be the character with the highest frequency at 
position p of each string read from the files. In the case where there are
multiple characters with the same frequency, consider the alphabetical order.
The generated string has a length equal to the maximum length of the strings
read from the files.

Therefore, you must write a function that takes as input a string "filename"
representing the name of a file and returns a string.
The function must construct the string according to the directions outlined
above and return the constructed string.

Example: if the contents of the three files A.txt, B.txt, and C.txt in the
directory test01 are as follows


test01/A.txt          test01/B.txt         test01/C.txt                                                                 
-------------------------------------------------------------------------------
test01/B.txt          test01/C.txt         test01/A.txt
house                 home                 kite                                                                       
garden                park                 hello                                                                       
kitchen               affair               portrait                                                                     
balloon                                    angel                                                                                                                                               
                                           surfing                                                               

the function most_frequent_chars ("test01/A.txt") will return "hareennt".
'''

# def most_frequent_chars(filename: str) -> str:
#     return wordlist_to_count(files_to_wordlist(filename))

# def files_to_wordlist(filename):
#     content = ''
#     nxname = filename
#     while True:
#         with open(nxname, 'r', encoding="utf-8") as file:
#             nxname = file.readline().split()[0]
#             content += file.read()
#         if nxname == filename:
#             break
#     return content.split()

def wordlist_to_count(w_list):
    d = {}
    for word in w_list:
        d.setdefault(len(word), []).append(word) # set default sets the value if it doesnt exist, if it does, continues on
    
    for index in range(max(d.keys())):
        countDict = {}
        for keys in d:
            if keys not in countDict:
                countDict[index] = 1
            else:
                countDict[index] += 1
                
    return countDict ??????????????????

    # for count in counts:
    #     max_value = max(count.items(), key=lambda x: x[1])[1]
    #     key_list = [k for k, v in count.items() if v == max_value]
    #     final.append(min(key_list))
    # return ''.join(final)

# wordlist_to_count: 
    
# Then, we iterate through every index in the range of longest length; we create an empty dictionary, countDict; we loop through the keys of the dictionary of lengths we made, let's call it lenDict; we check if index is less than the key to make sure we don't get an index error; we add the characters of each word at that index in countDict, which has the characters as keys and the count as values. ???????????

# Out of these loops, but still inside the index loop, we add to an empty string defined at the begining of the function, finalString, the appropriate letter, which we find by using the max function with a lambda as a key on countDict.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print(wordlist_to_count(['house', 'garden', 'kitchen', 'balloon', 'home', 'park', 'affair', 'kite', 'hello', 'portrait', 'angel', 'surfing']))
# print(wordlist_to_count(['house', 'garden', 'kitchen', 'balloon', 'home', 'park', 'affair', 'kite', 'hello', 'portrait', 'angel', 'surfing'])) # hareennt