def right_rotate(word,d):
    updated_word=word[-d:]+word[0:-d]
    return updated_word
    
word=input()
d=int(input())
print(right_rotate(word,d))
