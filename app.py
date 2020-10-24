n = 50
a = 1
b = 1
#chega ao numero de termos que � a
if n > 1:
    print(a)
    for i in range (2, n +1):
        b = b + a
        a = b - a
        print(a)
else:
    print(a)