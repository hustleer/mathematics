import math

f=lambda x:(x**3-4*x-9)
a=1.0
b=1.0
while((f(a)*f(b)>0)):
    a=float(input('Please enter the values of a: '))
    b=float(input('Please enter the values of b: '))
    e=float(input('Please enter the values of e: '))

c=(a+b)/2
loop=0
while( abs(f(c)) > e):
    c=b-(b-a)/(f(b) - f(a)) * f(b);
    if f(a) * f(c) < 0:
        b=c;
    else:
        a=c
    loop+=1
    print('loop:{} a={} b={} c:{} f(a):{} f(b):{} f(c):{}'.format(loop, a, b, c, f(a), f(b), f(c)))


print("abs(f(c)))>e",int(abs(f(c)))>e)
print("Required root is:", c);
print("f(c): ",f(c));
print(loop)

# non-linear eqn:
'''
from scipy.optimize import fsolve
import math

def equations(p):
    x, y = p
    return (x+y**2-4, math.exp(x) + x*y - 3)

x, y =  fsolve(equations, (1, 1))

print equations((x, y))


'''
