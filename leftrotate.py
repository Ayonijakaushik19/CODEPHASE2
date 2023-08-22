'''Given a string of size n, write functions to perform the following operations on a string-

Left (Or anticlockwise) rotate the given string by d elements (where d <= n)

Right (Or clockwise) rotate the given string by d elements (where d <= n).
Examples: 

Input : s = "GeeksforGeeks"
        d = 2
Output : Left Rotation  : "eksforGeeksGe" 
         Right Rotation : "ksGeeksforGee"  '''
         
def left_rotate(str1,d):
    updated_str=str1[d:]+str1[0:d]
    return updated_str
str1=input()
d=int(input())
print(left_rotate(str1,d))
