rente = 0.4
dager = 730
penger = 100000 #dag 0

for dag in range(dager):
    penger += (rente/3.6e4)*penger

print penger
