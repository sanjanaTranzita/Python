# Get the first item, the middle item and the last item of the list
l=["Sanju",1,"Tanu",123,"orange","mango",789]
print(len(l))
print(l[0])
print(l[-1])
print(l[4])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types =["Sanjana",22,5.5,"unmarried","Lucknow"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(it_companies.count('Google'))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[-1])
print(it_companies[3])

#modifying the list
it_companies[3] ='Tranzita_Systems'
print(it_companies)

#adding an element in the list
print(it_companies.append('Tranzita_Systems'))

#adding element in the middle of the list
print(it_companies.insert(4,'Tranzita'))

# Change one of the it_companies names to uppercase (IBM excluded!)
list = [x.upper() for x in it_companies]
print(list)

# Join the it_companies with a string '#;  '
print('#;'.join(it_companies))

#sorting the list
print(it_companies.sort())

# Reverse the list in descending order
print(it_companies.sort(reverse=True))

# Slice out the last 3 companies from the list
print(it_companies[-4:-1])

# Remove the first IT company from the list
it_companies.remove('Facebook')
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
it_companies.clear()
print(it_companies)

#joining the two lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
print(front_end+back_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end+back_end
print(full_stack)
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

#The following is a list of 10 students ages:
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
#Find the median age (one middle item or two middle items divided by two)
#Find the average age (sum of all items divided by their number )
#Find the range of the ages (max minus min)
#Compare the value of (min - average) and (max - average), use abs() method

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(ages[-1])
print(ages[0])
avg = sum(ages)/10
print(avg)
print(len(ages))



