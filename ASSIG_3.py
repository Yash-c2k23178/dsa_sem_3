"""Write a Python program to compute following computation on matrix:
    a) Addition of two matrices
    b) Subtraction of two matrices
    c) Multiplication of two matrices
    d) Transpose of a matrix """

r1 = int(input("Enter number of rows in First Matrix: "))
c1 = int(input("Enter number of columns in First Matrix: "))

m1 = []
for i in range(0,r1):
    my_list = []
    for j in range(0,c1):
        temp = int(input(f"Enter {j+1} element in {i+1} row of Matrix: "))
        my_list.append(temp)
    m1.append(my_list)

r2 = int(input("\nEnter number of rows in Second Matrix: "))
c2 = int(input("Enter number of columns in Second Matrix: "))

m2 = []
for i in range(0,r2):
    my_list = []
    for j in range(0,c2):
        temp = int(input(f"Enter {j+1} element in {i+1} row of Matrix: "))
        my_list.append(temp)
    m2.append(my_list)

print("\nFirst Matrix is ")
for i in m1:
    print(i)
print("Second Matrix is ")
for i in m2:
    print(i)
print()
#a) Addition of two matrices
def add():
    m3 = []
    if c1 != c2 or r1 != r2:
        print("For addition of two Matrices their order should be Same")
    else:
        for i in range(0, r1):
            temp_list = []
            for j in range(0, c1):
                temp_list.append(m1[i][j] + m2[i][j])
            m3.append(temp_list)
            temp_list = []
        i = 0
        print("Addition of two Matrices is:")
        for i in m3:
            print(i)

def sub():
    m4 = []
    if c1 != c2 or r1 != r2:
        print("For Subtraction of two Matrices their order should be Same")
    else:
        for i in range(0, r1):
            temp_list = []
            for j in range(0, c1):
                temp_list.append(m1[i][j] - m2[i][j])
            m4.append(temp_list)
            temp_list = []
        i = 0
        print("Subtraction of two Matrices is:")
        for i in m4:
            print(i)

def transpose(m0):
    r = len(m0)
    c = len(m0[0])
    m_new = [[0 for _ in range(len(m0))] for _ in range(len(m0[0]))]
    for i in range(0, r):
        for j in range(0, c):
            m_new[j][i] = m0[i][j]
    return m_new

def mul_add():
    r_ = []
    for i in range(0,r1):
        sum_of_mul = 0
        for j in m1[i]:
            sum_of_mul = sum_of_mul + m1[i][j]*m2t[i][j]
        r_.append(sum_of_mul)
    return r_

def mul():
    if c1 == r2:
        C = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    C[i][j] += m1[i][k] * m2[k][j]
        return C
    else:
        print("For Multiplication of two Matrices column of first matrix should be equal to rows of second matrix")


for i in range(0,5):
    choice = int(input("""Press 1 ~ Addition of two matrices
Press 2 ~ Subtraction of two matrices
Press 3 ~ Multiplication of two matrices
Press 4 ~ Transpose of matrices
Enter anything except 1 to 4 to exit"""))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        new_ = mul()
        print("\nMultiplication of two matrices is:")
        for i in new_:
            print(i)
    elif choice == 4:
        print("Transpose of first matrix is:")
        m1t = transpose(m1)
        for i in m1t:
            print(i)
        print("\nTranspose of second matrix is:")
        m2t = transpose(m2)
        for i in m2t:
            print(i)
    else:
        break
    i = choice

