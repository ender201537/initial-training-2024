a = 1.2+3.8
print(a)
type(a)#予想：float(5.0)

a = 10 // 100
print(a)
type(a)#予想：int(0)

a = 1 >= 0
print(a)
type(a)#予想：bool(tule)

a = 'Hello World' == 'Hello World'
print(a)
type(a)#予想：bool(true)

a = not 'Chainer' != 'Tutorial'
print(a)
type(a)#予想：bool(flase)

a = all([True, True, False])
print(a)
type(a)#予想：bool(false)

a = any([True, True, False])
print(a)
type(a)#予想：bool(true)

a = abs(-3)
print(a)
type(a)#予想：int(3) abs="絶対値"

a = 2 // 0
print(a)
type(a)#予想：error ゼロ除算：整数では無限大の値は扱えないため