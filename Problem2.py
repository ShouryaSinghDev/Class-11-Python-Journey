letter = """
                Dear <|name|>
                You are selected 
                <|date|>                                                                                                         """
letter = letter.replace("<|name|>", "Alex")
#we use str.replace fuction in it so that name can be replace by Alex 

letter =letter.replace("<|date|>" , "26 August 2030")
# Same we use str.replace function here so that date can be replace by 26 august 2030

print(letter)

#when we print this the output come is                       look like this 
# Dear Alex
# You are selected 
# 26 august 2026                                                                                           