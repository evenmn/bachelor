def factorial(x):
    if isinstance(x,float):
        x=int(x)
        print 'Warning: the factorial number is float'
    c=1
    for i in range(x):
        c=c*(i+1)
    return c

N=40
e=1
for i in range(N):
    e+=1./factorial(i+1)
print 'e: %.16f'%e
