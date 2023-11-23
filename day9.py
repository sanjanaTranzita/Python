age = int(input("Enter your age:"))
if age>18:
    print('You are old enough to learn to drive.')
else:
    print('You need 3 more years to learn to drive.')
    
#2
your_age = int(input("Enter your age: "))
my_age = 22 
if my_age < your_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")
elif my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_diff} years older than you.")
else:
    print("We are the same age.")
    
#3
a = int(input('Enter any number:'))
b = int(input('Enter any number:'))
if a>b:
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")

#4
score= int(input('Enter any score:'))
if score>80 and score<100:
    print('Grade:','A')
elif score>70 and score<89:
    print('Grade:','B')
elif score>60 and score<69:
    print('Grade:','C')
elif score>50 and score<59:
    print('Grade:','D')
    

#5
season = input("Enter any season:")
if season == 'September' or season=='October' or season== 'November':
    print('Season is Autumn')
elif season == 'December' or season== 'January' or season =='February':
    print('Season is Winter')
elif season == 'March' or season== 'April' or season=='May':
    print('Season is Spring')
elif season == 'June' or season== 'July' or season== 'August':
    print('Season is Summer')
    
#6
fruits = ['banana', 'orange', 'mango', 'lemon']
if 'banana' in fruits:
    print('That fruit already exist in the list')
elif 'apple' not in fruits:
    fruits.append('apple')
    print(fruits)

#7
