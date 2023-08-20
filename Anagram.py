#Write a program to  check whether two strings are anagram to each other
#race--'care'---These two are anagrams of each other
#--carr

def check_anagram(s1,s2):
    s1="".join(sorted(s1))
    s2="".join(sorted(s2))
    
    if s1==s2:
        print ("True")
    else:
        print ("False")
s1=input()
s2=input()
check_anagram(s1,s2)


    
