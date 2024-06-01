#Leetcode Q53
#Given an integer array, find the subarray with the largest sum, and return its sum.

def maxSubArr(arr):
    max_count = arr[0]
    current_count = 0
    for num in arr:
        if current_count < 0:
            current_count=0
        current_count += num
        max_count = max(current_count , max_count)
    return max_count        

a = [-1]
b = [-2,-1]
c = [-3,5,3,-2,3,8,-5,4]
print(maxSubArr(a))
print(maxSubArr(b))
print(maxSubArr(c))

