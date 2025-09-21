print('Введите 1 число')
a = int(input(), 2)
print('Введите 2 число')
b = int(input(), 2)
v = a + b
v = bin(v)
v = (v[2:])
print('Их сумма равна', v)