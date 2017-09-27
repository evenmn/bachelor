inhabitants=dict(Oslo=600000,Bergen=350000,Trondheim=275000)
inhabitants['Mexico city']=25000000
#print inhabitants

for city in inhabitants:
    print 'The number of inhabitants in %s is %d'%(city,inhabitants[city])

print sorted(inhabitants)

inhabitants_copy=inhabitants.copy()
del inhabitants_copy['Mexico city']
print inhabitants
print inhabitants_copy
