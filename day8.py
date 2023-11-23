dog = {
    'name': 'Shih Tzu',
    'color': 'brown',
    'breed': 'Siberian Huskey',
    'legs': 4,
    'age': 10,
}

student = {
    'first_name': 'Sanjana',
    'last_name': 'Agrawal',
    'age': 22,
    'gender':'Female',
    'country': 'India',
    'marital_status': False,
    'skills': ['JavaScript', 'Angular', 'Node', 'SQL', 'Python','Typescript'],
    'address': {
        'street': 'Rajendra Nagar',
        'zipcode': '273015'
    }
}
print(len(student))

value = student.get("skills")
skills = type(value)
print(value)
print(skills)

keys = student.keys()
print(keys)

values = student.values()
print(values)

student['first_name'] = 'Sanju'
student['age'] = 24
print(student)

del student['marital_status']
print(student)

print(student.items())

del student

