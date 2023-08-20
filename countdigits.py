#Write a progarm to count the digits in a given number
#9050--4

def count_digits(s):
    count=0 
    for i in s:
        if i.isnumeric()==True:
            count+=1
    print(count)
    
s=input()
count_digits(s)
