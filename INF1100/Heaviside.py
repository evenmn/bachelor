#3.23
#a)
def H(x):
    if x<0:
        h=0
    else:
        h=1
    return h
#b)

def test_H(x):
    tol = 1e-20
    if x<0:
        exact=0
    else:
        exact=1
    calc=H(x)
    success=abs(exact-calc)<tol
    msg='H(%.f) was not correctly calculated'%(x)
    assert success, msg
List=[-10,-1e-15,0,1e-15,10]
for number in List:
    t=test_H(number)
