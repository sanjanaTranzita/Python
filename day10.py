for i in range(11):
    print(i)
    
i=0    
while i<11:
    print(i)
    i+=1
  
for i in range(10,-1):
    print(i)

i=11
while i>0:
    print(i)
    i-=1  
    
# print pattern
for i in range(1,8):
    print("#"*i)
    
#4
for _ in range(1,9):
    print("#"*8)
    
#5
for i in range(11):
    res = i * i
    print(f"{i} x {i} = {res}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
l =  ['Python', 'Numpy', 'Pandas','Django', 'Flask']
for i in l:
    print(i)

# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i%2==0:
        print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i%2!=0:
        print(i)
        
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum =0
for i in range(101):
    sum+= i
print('The sum of all numbers is',sum)
    
sum_even=0
sum_odd=0
for i in range(101):
    if i%2 == 0:
        sum_even+=i
    else:
        sum_odd+=i
print('The sum of all evens is',sum_even)
print('The sum of all odd numbers is',sum_odd)       
