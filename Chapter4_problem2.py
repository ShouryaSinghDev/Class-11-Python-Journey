marks = [ ]

f1 = int(input("Enter your marks here "))
# we use int function here. becuse if we not use this. ours list did not come in a sort manner.because pyhton think this is a string so we use int function
marks.append(f1)
#we use .append function so that f1 marks append in the list 
f2 = int(input("Enter your marks here "))
# same here 
marks.append(f2)
# same here 
f3 = int(input("Enter your marks here "))
# so on
marks.append(f3)
# so on
f4 = int(input("Enter your marks here "))

marks.append(f4)

f5 = int(input("Enter your marks here "))

marks.append(f5)

f6 = int(input("Enter your marks here "))

marks.append(f6)

marks.sort()# we use this function here because we want list in a sorted manner 

print(marks)