#this program to find the length of (s)
s = set() 
s.add(20)
s.add(20.0)
s.add('20') 

print(len(s))# use this to finding the length

print(s)
#output 20 ,'20' 
#because python compare both values which is 20 or 20.0 after comparing the answer is simple both are same so that the length is coming out is 2 because in output we have two values 
