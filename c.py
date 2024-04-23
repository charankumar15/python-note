def multiply(a,b):
    return a * b

print(multiply (5 , 6))

multi_lam = lambda a , b :a*b
print(multi_lam( 5 , 6))


def call_from_func(call_func, a,b):
    return call_func( multiply, 5,6)

print(call_from_func( multiply , 5,6))

print(call_from_func( multi_lam , 5,6))

print(call_from_func( lambda x, y :x/y,1, 2 ))

