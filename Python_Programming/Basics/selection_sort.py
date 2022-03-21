"""SELECTION SORT"""

my_list = [8,19,23,5,6,14,11,55,1]

def sorting(my_list):
    smallest = my_list[0]
    smallest_pos = 0
    for i in range (0,len(my_list)):
        if smallest > my_list[i]:
            smallest = my_list[i]
            smallest_pos = i
    return smallest_pos
print("original list :",my_list)
def sorted_list(my_list):
    new_array = []
    for i in range(len(my_list)):
        item = sorting(my_list)
        new_array.append(my_list.pop(item))
    return new_array
print("selection sorted list :",sorted_list(my_list))
