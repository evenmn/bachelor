from SineFunc import SineFunc

f = SineFunc(p=0.1, q=4, r=0.05)
for t in [0.2, 0.4, 1, 2]:
    f_value = f(t)
    print 'f(%g)=%g' % (t, f_value)
