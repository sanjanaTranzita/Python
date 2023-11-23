import math
import string
first = 'Thirty'
second = 'Days'
third = 'Of'
fourth = 'Python'
space =' '
print(first+space+second+space+third+space+fourth)

first = 'Coding'
second = 'For'
third = 'All'
space = ' '
concatenate = first+space+second+space+third
print(concatenate)

variable = concatenate
print(variable)
print(len(variable))
print(variable.upper())
print(variable.lower())
print(variable.capitalize())
print(variable.title())
print(variable.swapcase())
print(variable.split()[0])

print(variable.find('Coding'))
print(variable.replace('Coding For All','Python'))

str = 'Python for Everyone'
print(str)
print(str.replace('Python for Everyone','Python for All'))

print(variable.split(" "))

str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str.split(","))

str = 'Coding For All'
sub_str = 'All'
print(str.index(sub_str))

py = 'Python for Everyone'
cd = 'Coding For All'
print(cd.index('C'))
print(cd.index('F'))

str = 'Coding For All People'
print(str.rfind('l'))

str = 'You cannot end a sentence with because because because is a conjunction'
print(str.index('because'))
print(str.rindex('because'))

sent = 'You cannot end a sentence with because because because is a conjunction'
phrase = sent[31:57]
print("Sliced Phrase:", phrase)

str = 'Coding For All'
if str.startswith('Coding'):
    print('Yes')
else:
    print('No')

str = 'Coding For All'
if str.endswith('Coding'):
    print('Yes')
else:
    print('No')

str = '30DaysOfPython'
print(str.isidentifier())

str = 'thirty_days_of_python'
print(str.isidentifier())

l = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("_".join(l))

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

r= 10
area = 3.14 * r ** 2
result = 'The area of a circle with radius {} is {}'.format(r, area)
print(result)
