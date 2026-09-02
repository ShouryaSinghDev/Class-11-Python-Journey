#this program is built for that user who want an option to look which word he want to know it translation 

words = { 
"Kursi" : "Chair",
"Tum"  :  "You" ,
"Dost"  :  "Friend" ,  # Don't forget to use this (,) because it show error if you not use this(,)
}


word = input("Enter your word that you want to looked its translation ") # we use input function here because for the user who want an option to look which word he want to know its translation 

print(words[word]) # we do this (words[word])
#because we want translation of word from the dict. of words 