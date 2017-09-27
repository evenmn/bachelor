def atan(N,x):
    c=0
    for i in range(N):
        if i%2==0:
            None
        else:
            if (i-1)%4==0:
                c+=(x**(i))/float(i)
            else:
                c-=(x**(i))/float(i)      
    return c

N=40
for i in range(N):
    pi=16*atan(i,(1/5.))-4*atan(i,(1./239))
print 'Pi: %.16f'%pi
