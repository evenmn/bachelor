#6.3
#NB: ikke fullf;rt
#a)
def read_densities(filename):
    infile=open(filename, 'r')
    densities = {}
    for line in infile:
        words=line.split()
        density=float(words[-1])
        substance=''
        for i in range(len(words)-1):
            S=''.join(words[i])
            substance+=S
        densities[substance]=density
    infile.close()
    return densities
densities=read_densities('densities.dat')

#b)
def read_densities(filename):
    infile=open(filename, 'r')
    letters=[]
    for line in infile:
        S=''
        for letter in line:
            s=''.join(letter)
            S+=s
        letters.append(S)
    return letters
print read_densities('densities.dat')
