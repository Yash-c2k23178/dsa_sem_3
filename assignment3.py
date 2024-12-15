''' Write a python program to perform following operations on a matrix:
1.Addition of matrices
2.Subtraction of matrices
3.Multiplication of matrices
4.Transpose of a matrix '''

result=[[0,0,0],
 [0,0,0],
 [0,0,0]]
class matrix:
    def __init__(self,A,B):
        self.A=A
        self.B=B
    def length(self,A):
        len = 0
        for i in A:
            len = len +1
        return len 

    def addition(self,A,B):
        length_A=self.length(A)
        length_A_row=self.length(A[0])
        for i in range(length_A):
            for j in range (length_A_row):
                result[i][j] = A[i][j] + B[i][j]
        
        for r in result:
            print (r)

    def subtraction(self,A,B):
        length_A=self.length(A)
        length_A_row=self.length(A[0])
        for i in range(length_A):
            for j in range (length_A_row):
                result[i][j] = A[i][j] - B[i][j]
        
        for r in result:
            print (r)     

    def multiplication(self,A,B):
        row1=self.length(A)
        column2=self.length(B[0])
        column1=self.length(A[0])
        for i in range(row1):
            for j in range(column2):
                for k in range(column1):
                    result[i][j] += A[i][k] *B[k][j]
        for r in result :
            print(r)

    def transpose(self,A):
        row1=self.length(A)
        column1=self.length(A[0])
        for i in range (row1):
            for j in range (column1):
                result[j][i] = A[i][j]
        for r in result:
            print(r)

def create_matrix(R,C):
    matrix = []
    print("Enter the entries row-wise:")
    for i in range(R):
        a=[]
        for j in range (C):
            a.append(int(input()))
        matrix.append(a)
    return matrix

def menu():
    operation = int(input("Enter the operation to be performed \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Transpose \nEnter the respective number\n"))
    if(operation ==  1):
        r1=int(input("Enter the no of rows of 1st matrix "))
        c1=int(input("Enter the no of columns of 1st matrix "))
        r2=int(input("Enter the no of rows 2nd matrix "))
        c2=int(input("Enter the no of rows of 2nd matrix "))
        if(r1==r2 & c1==c2):
            R1=create_matrix(r1,c1)
            R2=create_matrix(r2,c2)
            obj1=matrix(R1,R2)
            obj1.addition
    elif(operation ==  2):
        r1=int(input("Enter the no of rows of 1st matrix "))
        c1=int(input("Enter the no of columns of 1st matrix "))
        r2=int(input("Enter the no of rows of 2nd matrix "))
        c2=int(input("Enter the no of rows of 2nd matrix "))
        if(r1==r2 & c1==c2):
            R1=create_matrix(r1,c1)
            R2=create_matrix(r2,c2)
            obj1=matrix(R1,R2)
            obj1.subtraction
        else:
            print("Can't perform subtraction ")
    elif(operation ==  3):
        r1=int(input("Enter the no of rows of 1st matrix "))
        c1=int(input("Enter the no of columns of 1st matrix "))
        r2=int(input("Enter the no of rows of 2nd matrix "))
        c2=int(input("Enter the no of rows of 2nd matrix "))
        if(c1==r1):
            R1=create_matrix(r1,c1)
            R2=create_matrix(r2,c2)
            obj1=matrix(R1,R2)
            obj1.multiplication
        else:
            print("Can't perform multiplication ")
    elif(operation ==  4):
        r1=int(input("Enter the no of rows of matrix "))
        c1=int(input("Enter the no of columns of matrix "))
        R=create_matrix(r1,c1)
        obj1=matrix(R)
        obj1.transpose
    else:
        print("Invalid input for operations")

menu()