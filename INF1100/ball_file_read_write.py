#4.14
#a)
filename='zfile.txt'
def extract_data(filename):
    infile=open(filename,'r')
    numbers=[]
    for line in infile:
        number = line.split()
        numbers.append(number)
    v0=float(numbers[0][1])
    t=[]
    for i in range(2,len(numbers)):
        for j in numbers[i]:
            t.append(float(j))
    return v0, t
values=extract_data(filename)

#b)
g=9.81
def table(values):
    v0=values[0]
    t_list=sorted(values[1])
    y_list=[v0*t-0.5*g*t**2 for t in t_list]
    print 'Time      Height'
    for i in range(len(t_list)):
        print '%.2f      %.2f' % (t_list[i], y_list[i])
d=table(values)

#c)
#Testfunksjon
