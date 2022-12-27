"""Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

Example 1:
N = 5
A[] = {1,2,3,5}"""

def MissingNo(arr):
    n = len(arr)
    total = (n + 1)*(n + 2)//2
    arr_sum = sum(arr)
    return total - arr_sum
print(MissingNo({1,2,3,5}))

"""Example 2:
Input:
N = 10
A[] = {6,1,2,8,3,4,7,10,5}"""

def MissingNo(arr):
    n = len(arr)
    total = (n + 1)*(n + 2)//2
    arr_sum = sum(arr)
    return total - arr_sum
print(MissingNo({6,1,2,8,3,4,7,10,5}))


"""1. Convert two lists into a dictionary"""

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = { i:j  for i , j in zip(keys, values)}
print(result)

"""3. Print the value of key 'history' from the below dict"""

sampleDict = {"class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])

"""4 Create a dictionary by extracting the keys from a given"""
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
result = {}
for i in keys:
    result.update({i :sample_dict[i]})
print(result)


"""Delete a list of keys from a dictionary"""
keys = ["name", "salary"]

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

for i in keys:
    sample_dict.pop(i)
print(sample_dict)