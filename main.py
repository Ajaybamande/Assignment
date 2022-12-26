"""1:--  Using a loop, determine whether a given value is an integer or not.
A= [None, 2, 3, 4, 'Sureshs', 'XYZ', 1]"""
A= [None, 2, 3, 4, 'Sureshs', 'XYZ', 1]

for item in A:
    if type(item) == None:
        print('This is the str type ', item)
    elif type(item) == int:
        print("This is the integer type", item)
    else:
        print("this is not str type", item)


"""2 :-Find out whether given strings are anagrams or not. 
 dad, add >> Yes
 Sankar, Sanker >> No"""

def chack_anagrams(string1, string2):
    if sorted(string1) == sorted(string2):
        print('Strings are nagrams')
    else:
        print('Strings are not nagrams')


chack_anagrams('dad', 'add')

"""3. Input: [a, b, c], [1, 2, 3, 4, 5] and output
should be
Output: [a, 1, b, 2, c, 3, 4, 5]"""

import itertools

Input = ['a', 'b', 'c'], [1, 2, 3, 4, 5]
alphabets, numbers = Input
result = []
for alphabet, number in itertools.zip_longest(alphabets, numbers):
    result.append(alphabet)
    result.append(number)
out_put = []
for item in result:
    if item == None:
        continue
    else:
        out_put.append(item)
print(out_put)

"""4. Remove all even elements of a given list and multiple odd numbers with 5"""

A = list(range(100))

result = []
for element in A:
    if element % 2 != 0:
        result.append(element * 5)
print(result)

"""5. Find out occurrences of each element on a given list without using any built - in functions.
A = [1, 11, 22, 44, 1, 11, 5, 6, 7, 8, 9, 10]
O / p: 1: 2, 11: 2, 22: 1
"""
A = [1, 11, 22, 44, 1, 11, 5, 6, 7, 8, 9, 10]

result = {}
for items in A:
    result[items] = A.count(items)

for key, value in result.items():
    print("% d : % d" % (key, value), end=" ")

"""6. Define one class with two methods, where one method is used to set the passed value to data and another method is used to remove elements(passed list) from data.
Class
A:
obj = A()
obj.set_value(23)
obj.remove_elements([12, 34, 45])
"""

class A:
    list = [24, 35, 58, 39, 20, 30]

    def set_value(self, element):
        A.list.append(element)
        print(A.list)

    def remove_elements(self, lst):
        for item in lst:
            A.list.remove(item)
        print(A.list)


obj = A()
obj.set_value(12)
obj.remove_elements([24, 58, 35])




