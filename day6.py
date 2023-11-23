
#create an empty tuple
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
#Join brothers and sisters tuples and assign it to siblings
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members

sisters =('Muskan','Shivangi','Soni')
brothers =('Ananya','Sonu','Srijan','Anshul')
siblings =sisters+brothers
print(siblings)
print(len(siblings))
family_members = ("Father", "Mother") + siblings
print(family_members)

#unpacking the tuple
family_members = ("Father", "Mother") + siblings
father, mother, *rest_of_family = family_members
print("Father:", father)
print("Mother:", mother)
print("Siblings:", rest_of_family)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits =('mango','apple','banana','orange','kiwi')
vegetables=('potato','onion','tomato','carrot')
animal_products=('dog','cat','lion','monkey')
food_stuff_tp =fruits+vegetables+animal_products
print(food_stuff_tp)

#converting tuple to list
lst = list(food_stuff_tp)
print(lst)

#Slice out the first three items and the last three items from food_staff_lt list
first = food_stuff_tp[:4]
last = food_stuff_tp[-4:-1]
print(first)
print(last)

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print('not a nordiac country')
elif 'Iceland' in nordic_countries:
    print('a nordiac country')
