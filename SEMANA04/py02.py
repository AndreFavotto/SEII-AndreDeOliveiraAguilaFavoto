''' Exercício referente ao vídeo 02 
 André de Oliveira Águila Favoto - 11811EAU013''' 

#common print
""" message = "Hello World"
 
print(message)
 """

# using ' 

""" message = "Bobby's World"
 
print(message)
 """
#multiple line print
''' message = """Bobby's World is
nothing but fake"""

print(message) '''

#len function and accessing individual characters/intervals
""" message = "Hello World"
 
print(len(message))
print(message[1])
print(message[:5])
 """

#useful string methods
""" message = "Hello World"

 
print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.count('Hello'))
print(message.find('World'))
aux_message = message.replace('World', 'Universe')
print(aux_message)
 """

#concatenating methods
greeting = "Hello"
name = "Michael"
message = greeting + ', ' + name + '!'
print(message)
print(f'{greeting}, {name}!')