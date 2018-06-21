# -*- coding: utf-8 -*-

a = 100 == 100
print(a)

b = 'a' == 'a'
print(b)

c = 'david' == 'David'
print(c)

d = 'z' > 'a'
print(d)

e = 10 != 10
print(e)

f = 15 != 10
print(f)

g = 10 > 10
print(g)

h = 15 > 10
print(h)

i = 10 > 15 and 15 > 20
print(i)

j = 'a' == 'a' and 'b' == 'b'
print(j)

k = 'a' == 'a' or 'b' != 'b'
print(k)

l = True or False
print(l)

def say_hello(age):
    if(age > 18):
        print('Hola Señor')
    else:
        print('Hola Niño')

say_hello(20)
say_hello(14)