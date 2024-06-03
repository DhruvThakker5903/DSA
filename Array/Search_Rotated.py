'''
LeetCode Q33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
'''

def Search(arr , target):

    low = 0
    high = len(arr)-1

    while low <= high :

        mid = (low + high) // 2

        if target == arr[mid]:
            return mid
        
        if arr[low] <= arr[mid]:

            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:

            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

arr = [4,5,6,7,0,1,2]
target = 0

arr1 = [4,5,6,7,0,1,2]
target1 = 3

arr2 = [1]
target2 = 0

print(Search(arr,target))
print(Search(arr1,target1))
print(Search(arr2,target2))

