"""QUCIK SORT"""
arr = [6,3,1,45,12,16,9]
def qs(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i >= pivot]
        return qs(lesser) + [pivot] + qs(greater)
print(qs(arr))