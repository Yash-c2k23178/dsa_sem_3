"""In second year, computer engineering class, group A student’s play cricket, group B students play badminton and group C students play football. Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, do not use SET built-in functions)"""

def set_intersection(A,B):
   intersection=[]
   for i in A:
       for x in B:
           if i==x:
               intersection.append(i)
   return intersection

def set_union(A,B):
   union = list(A)
   for i in B:
       found = False
       for x in union:
           if x == i:
               found = True
               break
       if not found:
           union.append(i)
   return union

def set_difference(A,B):
   difference = []
   for i in A:
       found = False
       for x in B:
           if i == x:
               found = True
               break
       if not found:
           difference.append(i)
   return difference

students = []
cricket=[]
badminton=[]
football=[]
s=int(input("Enter the number of students in the class "))
for i in range(s):
    i=input("Name: ")
    students.append(i)
a=str(input("Enter the number of students who play cricket "))
for i in range(a):
    i=input("Name: ")
    cricket.append(i)
b=str(input("Enter the number of students who play badminton "))
for i in range(b):
    i=input("Name: ")
    badminton.append(i)
c=str(input("Enter the number of students who play football "))
for i in range(c):
    i=input("Name: ")
    football.append(i)
 
cricket_badminton_both= set_intersection(cricket,badminton)
print("The students playing cricket and badminton are ",cricket_badminton_both)

either_cricket_or_badminton_not_both= set_difference(cricket,badminton)+set_difference(badminton,cricket)
print("The students playing cricket or badminton but not both are ",either_cricket_or_badminton_not_both)

cricket_badminton=set_union(cricket,badminton)
neither_cricket_nor_badminton= set_difference(students,cricket_badminton)
print("The number of students playing neither cricket nor badminton is ",len(neither_cricket_nor_badminton))

cricket_football_both=set_intersection(cricket,football)
not_badminton= set_difference(cricket_football_both,badminton)
print("The number of students who play cricket and football but not badminton is ",len(not_badminton))