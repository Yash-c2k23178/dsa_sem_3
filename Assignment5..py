'''Write a python program to store second year percentage of
students in array. Write function for sorting array of floatingpoint numbers in ascending order using a) Insertion sort
b) Shell Sort and display top five scores'''

def length(A):
    len = 0
    for i in A:
        len = len +1
    return len

def make():
    A=[]
    s= int(input("Enter the number of elements in the array: "))
    for i in range(s):
        a = int(input("Enter element "))
        A.append(a)
    return A

def bubble_sort(A):
    n = length(A)
    for i in range(n-1):
        swap = 0
        for j in range (n-i-1):
            if(A[j] > A[j+1]):
               temp = A[j]
               A[j]=A[j+1]
               A[j+1]=temp
               swap = 1
        print("Pass",i+1,A)
        if swap==0:
            break
    print("Sorted array is ",A)

def insertion_sort(A):
    B=[]
    B.append(A[0])
    n = length(A)
    if n<= 1:
        return 
    for i in range(1, n):
        B.append(A[i])
        key = B[i]
        j = i-1
        swap = 0
        while j>=0 and key<B[j]:
            temp = B[j+1]
            B[j+1] = B[j]
            B[j] = temp
            j = j -1
            key = B[j+1]
            swap =1
            counter = counter + 1
            print("Pass:",i,B)
            if (swap == 0):
                break

def shell_sort(arr):
    n = length(arr)
    gap = int(n/2)
    while(gap>0):
        i = 0
        j = gap
        counter = 0
        while(j<n):
            if (arr[i]>arr[j]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                counter = counter + 1
                print("Pass :",counter,arr)
            i = i +1
            j = j +1
        gap = int(gap/2)
    bubble_sort(arr)
    
        
def menu():
    n = int(input("Enter the sort you have to perform \n (Write the respective number)\n 1.Bubble Sort \n 2.Insertion Sort \n 3.Shell Sort"))
    A = make()
    if(n == 1):
        bubble_sort(A)
    elif(n == 2):
        insertion_sort(A)
    elif(n == 3):
        shell_sort(A)
    else:
        print("Invalid Input \n Enter valid input")

