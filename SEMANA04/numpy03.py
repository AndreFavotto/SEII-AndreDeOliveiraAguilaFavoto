import numpy as np

a1 = np.array([2,4,6,8,10])
print(a1[2])
print(a1[2:])
print(a1[:-2])
print(a1[a1>3])

names = np.array(['Andre', 'Felipe', 'Amanda', 'Marcos'])

first_letter_a = np.vectorize(lambda s: s[0])(names)=='A'

print(names[first_letter_a])

print(a1[a1%4 == 0])