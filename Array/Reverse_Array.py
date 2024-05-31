#Array Reverse Using an Extra Array

def Rev_Arr(arr):

    sol = arr[::-1]
    return sol

num = [1,2,3,4,5,6,7]
print(Rev_Arr(num))


#Array Reverse Using a Loop

def Rev_l(arr,start,end):

    while start<end:
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
    return arr

alpha = ["A","B","C","D","E","F"]
print(Rev_l(alpha,0,5))


#Array Reverse using an Inbuilt Methods

count = [1,2,3,4,5,6,7]
rev_list = list(reversed(count))
print(rev_list)


#Array Reverse Using a Recursion

def rec_rev(arr,start,end):
    if start >= end:
        return
    arr[start] , arr[end] = arr[end] , arr[start]
    rec_rev(arr,start+1,end-1)

meow = ["M","E","O","W"]
rec_rev(meow,0,3)
print(meow)

