""" Write a Python program to compute following operations on String: 
a) To display the length of the string 
b) To determines the frequency of occurrence of particular character in the string 
c) To check whether given string is palindrome or not 
d) To display index of first appearance of the substring 
e) To count the occurrences of each word in a given string"""

def length(A):
    len = 0
    for i in A:
        len = len +1
    return len

def char_frequency(A):
    s = str(input("Enter the character to be checked : "))
    count = 0
    for i in range(len(A)):
        if A[i] == s:
            count = count +1
        i = i+1
    return count

def palindrome(A):
    t=""
    for i in A:
        t = i + t
    if(A == t):
        print("The string is an palindrome")
    else:
        print("The string is not an palindrome")
        
def first(self, substring):
    len_sub = len(substring)
    len_str = len(self.input_string)
    for i in range(0, len_str - len_sub + 1):
        j = 0
        while j < len_sub:
            if self.input_string[i + j] != substring[j]:
                break
            j += 1
        if j == len_sub:
            return i
    return -1
    
def count_word_occurrences(self):
        words = []
        curr = ""
        word_count = {}
        
        for char in self.input_string:
            if char == ' ':
                if curr:
                    words.append(curr)
                    if curr in word_count:
                        word_count[curr] += 1
                    else:
                        word_count[curr] = 1
                    curr = ""
            else:
                curr += char
        
        if curr:
            words.append(curr)
            if curr in word_count:
                word_count[curr] += 1
            else:
                word_count[curr] = 1
        
        return word_count                                                  


s = str(input("Enter the string "))
l =length(s)
print("The length of the string is ",l)
c =char_frequency(s)
print (c)
f = palindrome(s)
