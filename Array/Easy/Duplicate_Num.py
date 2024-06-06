#Leetcode Q217
#Given an integer array, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Using HashSet

def Duplicate(arr):
    hashset = set()
    for n in arr:
        if n in hashset:
            return True
        hashset.add(n)
    return False

Num = [1,2,3,1]
print(Duplicate(Num))


#Brute Force

def Duplicate2(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

print(Duplicate2(Num))


#Using Sort Method

def Duplicate3(arr):
    arr.sort()
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    return False

print(Duplicate3(Num))