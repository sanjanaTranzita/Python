#evel-1
it_companies = {'Facebook', 'Google', 'Microsoft','Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update('Tranzita','Jaro Education','Alobha Technologies')
print(it_companies)

it_companies.remove('Google')
print(it_companies)

#Level-2
C = A.union(B)
print(C)

D =A.intersection(B)
print(D)

E = A.issubset(B)
print(E)

F = A.union(B)
G = B.union(A)
print(F)
print(G)

H= A.isdisjoint(B)
print(H)

I = A.symmetric_difference(B)
print(I)

str = set('I am a teacher and I love to inspire and teach people')
print(str)






