

def fun(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a,b = b, a+b

for i in fun(10):
    print(i)


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))

def fi():
    name = 'Zszen John'
    firstname, lastname = name.split()
    print(firstname)
    print(lastname)

fi()