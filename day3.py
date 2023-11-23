base =20
height =10
print('Enter base:',base)
print('Enter height:',height)
print("The area of triangle is:", 0.5*base*height)

a =5
b =4
c =3
print('Enter side a:', a)
print('Enter side b:', b)
print('Enter side c:',c)
print('The perimeter of triangle is:',a+b+c)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print('Area:',length*width)
print('Perimeter:',2*(length+width))

radius = float(input("Enter the value of radius:"))
print('Area:', 3.14*radius*radius)
print('Circumference:', 2*3.14*radius)


import math
x1 = int(input('Enter first number:'))
x2 = int(input('Enter second number:'))
y1 = int(input('Enter y1 axis value:'))
y2 = int(input('Enter y2 axis value:'))
print('slope is m=:',y2-y1/x2-x1)
print('Eucledian distance between two points are:',(((y2-y1)**2)+(x2-x1)**2)**0.5)

print(len('python')==len('dragon'))


s1 = 'python'
s2 = 'dragon'
if 'on' in s1 and 'on' in s2:
    print("'on' is found in both 'python' and 'dragon'")
else:
    print("'on' is not found in both words")
    
    
s1 = 'I hope this course is not full of jargon'
if 'jargon' in s1:
    print('jargon is present in',s1)
    

s1 = 'python'
s2 = 'dragon'
if 'on' not in s1 and 'on' not in s2:
    print("'on' is found in both 'python' and 'dragon'")
else:
    print("'on' is not found in both words")

text ='python'
print(len(text))
print(float(text))
print(str(text))


print(type('10')==type(10))

print(int('9.8')==10)

hours = int(input('Enter hours:'))
rate = int(input('Enter rate per hour:'))
print('Your weekly earning is:',hours*rate)

year = int(input('Enter number of hours you have lived:'))
print('You have lived for',year*24*3600,'seconds')


rows = 5
print("N  N^2  N^3  N^4  N^5")
for n in range(1,rows + 1):
    print(f"{n} {n**2} {n**3} {n**4} {n**5}")
