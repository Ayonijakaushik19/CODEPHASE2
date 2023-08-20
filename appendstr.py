'''Exercise 2: Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
Given:
s1 = "Ault"
s2 = "Kelly"
Expected Output:
"AuKellylt"
'''

'''s1="Ault"
s2="Kelly"
s3=s1[0:2]+s2+s1[2:]
print(s3)'''

s1=input()
s2=input()

n1=len(s1)
n2=len(s2)
s3=s1[:n1//2]+s2+s1[n1//2:]
print(s3)

