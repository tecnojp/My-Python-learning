# Playing with strings and operators
first_name = 'JP'
last_name = 'Oliveira'
print (first_name + last_name)
print (first_name + ' ' + last_name)

# Playing with strings and functions
sentence = "The Dog is named Sammy"
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

first_name = input('What is yuour fist name? ')
last_name = input('What is your last name?' )
print ('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())
output = 'Hello, {} {}'.format(first_name,last_name)
print(output)
output = 'Hello, {0} {1}'.format(first_name,last_name)
print(output)
# Only available in Python 3
output = f'Hello, {first_name} {last_name}'
print(output)