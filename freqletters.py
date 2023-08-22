'''Given a string and a character, the task is to make a function which count occurrence of the given character in the string.

Examples:  

Input : str = "geeksforgeeks"
         c = 'e'
Output : 4
'e' appears four times in str.'''

def freq_char(str,c):
    count=0
    for i in str:
        if i==c:
            count+=1 
    return count
    
str=input()
c=input()
print (freq_char(str,c))
        
    
