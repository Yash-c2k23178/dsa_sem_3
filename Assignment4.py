'''class search:
    def __init__(self)'''
def length(A):
    len = 0
    for i in A:
        len = len +1
    return len 

def linear(A):
    key=int(input("Enter the key to be searched: "))
    i=0
    n = length(A)
    while(i<n):
        if(A[i]== key):
            print(i)
        i=i+1
    return -1

def sentinel(A):
    key=int(input("Enter the element to be searched: "))
    i=0
    A.append(key)
    n = length(A)
    while(A[i]!= key):
        i = i +1
    if(i<n):
        print("Found at index ",i)
    else:
        print("Not found")

def binary_search(A):
    key=int(input("Enter the element to be searched: "))
    start = 0
    end = length(A)-1
    while(end>=start):
        mid = start + (end - start)/2
        if (key == A[mid]):
            print("The element found at position ",mid)
        elif(key>A[mid]):
            start = mid +1
        else:
            end = mid -1
    return -1

def fibonacci_search(A):
    key = int(input("Enter the key to be searchd: "))
    n = length(A)
    fibm2 = 0
    fibm1 = 1
    fibm = fibm2 + fibm1
    while(fibm < n):
        fibm2 = fibm1
        fibm1 = fibm
        fibm = fibm2 + fibm1
    offset = -1
    while(fibm > 1):
        i = min((offset + fibm2),n-1)
        if (A[i]<key):
            fibm = fibm1
            fibm1 = fibm2
            fibm2= fibm - fibm1
            offset = i
        elif(A[i]>key):
            fibm = fibm2
            fibm1 = fibm1-fibm2
            fibm2= fibm - fibm1
        else:
            return i
    if(fibm1 and A[offset +1]== key):
        return (offset + 1)
    return -1

def make(): 
    A=[]
    s= int(input("Enter the number of elements in the array: "))
    print("\n Enter the array in the sorted form")
    for i in range(s):
        a = int(input("Enter element "))
        A.append(a)
    return A
    
def menu():
    while(True):
        i = int(input("Enter the search method you have to perform (Enter the corresponding number)\n1.Linear Search\n2.Sentinel Search\n 3.Binary Search \n4.Fibonacci Search"))  
        if(i == 1):
            arr=make(),
            linear(arr)
        elif(i == 1):
            arr=make()
            sentinel(arr)
        elif(i == 1):
            arr=make()
            binary_search(arr)
        elif(i == 1):
            arr=make()
            index=fibonacci_search(arr)
            if (index>=0):
                print("Key is present at index ",index)
            else:
                print("Key not found")
        else:
            print("Invalid Input.Enter a value input ")
        

