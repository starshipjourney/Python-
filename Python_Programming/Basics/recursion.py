"""RECURSION"""

# def fact(x):
#     if x == 1: #base case
#         return x
#     else:
#         return x * fact(x-1)

# print(fact(4)) #factorial of number

# arr = [8,2,5,6,4,5]
# def sum(x):
#     if x >= 0: 
#         return arr[x]+sum(x-1)
#     else:
#         return 0
# print(sum(len(arr)-1)) #sum of numbers in list

arr =[3,4,7,1]
def count(arr):
    if arr == []:
        return 0
    else:
        return 1+count(arr[1:])

print(count(arr)) #count number of elements in list


# arr=[2,19,34,3,7]
# def sum(arr):
#     if arr == []:
#         return 0
#     else:
#         return arr[0] + sum(arr[1:])
# print(sum(arr))