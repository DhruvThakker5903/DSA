'''
DSA Q5/Q375
Chocolate Distribution Problem
Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that:
    I) Each student gets one packet.
    II)The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum 
'''

def chocolate(arr,m):
    arr.sort()
    print(arr)
    diff = arr[m-1] - arr[0]       # =2 ,
    for i in range(0 , len(arr)-(m-1)):
        check = arr[(m-1)]-arr[i]
        # print("check ", i ,"=", check)
        if check < diff:
           diff = check
        m = m+1
    return diff

#Ex 1
arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
print("minimum difference is = " , chocolate(arr,m))
#Ex 2
arr1 = [3, 4, 1, 9, 56, 7, 9, 12]
m1 = 5
print("minimum difference is = " , chocolate(arr1,m1))
#Ex 3
arr2 = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m2 = 7
print("minimum difference is = " , chocolate(arr2,m2))