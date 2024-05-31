#DSA Q1 / Q375
#Maximum and minimum of an array using minimum number of comparisons

def min(list):
    mini = float('inf')
    for num in list:
        if num<mini:
            mini = num
    return mini

def max(list):
    max = float('-inf')
    for num in list:
        if num>max:
            max = num
    return max

if __name__ == "__main__":
    A = [5,9,0,3,1,14,21]
    print("minimum num is: " , min(A))
    print("maximum num is: " , max(A))