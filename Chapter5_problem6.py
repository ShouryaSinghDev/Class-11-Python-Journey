#this program is for 4 friends to enter their name or language as value and key.

d = {} #show an empty dict 
name = input("Enter your name ")
lang = input(" Enter your language ")
d.update({name : lang})#we use this .update function like .append function to insert in the dict 

name = input("Enter your name ")
lang = input(" Enter your language ")
d.update({name : lang})#always remember not use quote in this for update in dict

name = input("Enter your name ")
lang = input(" Enter your language ")
d.update({name : lang})
name = input("Enter your name ")
lang = input(" Enter your language ")
d.update({name : lang})
print(d)#at last print (d)