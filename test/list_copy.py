old = [1,[1,2,3],3]
new = old.copy()
print('Before:')
print(old)
print(new)
new[0] = 3
new[1][0] =3
print('After:')
print(old)
print(new)