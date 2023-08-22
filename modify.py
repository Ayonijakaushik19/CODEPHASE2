#string="ayonija"
#d1,d2--sub-index
#reverse the characters between d1 and d2 
def update_word(word,d1,d2):
    #output=aynoija
    new_word=word[:d1]+word[d2-1:d1-1:-1]+word[d2:]
    return new_word
    
word=input()
d1,d2=int(input()),int(input())
print(update_word(word,d1,d2))
