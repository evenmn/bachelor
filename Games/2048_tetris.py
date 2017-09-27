import numpy as np
import time

#Variables
N = 11                  #Number of rows
M = 5                   #Number of columns
O = 4                   #Orientations

#Probabilities
prob_1 = 80
prob_2 = 15
prob_4 = 5
pick_list = []
if (prob_1 + prob_2 + prob_4) != 100:
    raise ValueError('Error')
else:
    for i in range(prob_1):
        pick_list.append(1)
    for i in range(prob_2):
        pick_list.append(2)
    for i in range(prob_4):
        pick_list.append(4)

#---Creating matrix---
matrix = np.zeros(shape=[2, N, M])

matrix[0, 0, int(M/2.)] = np.random.choice(pick_list)
matrix[1, 0, int(M/2.)] = np.random.randint(O)

#---Print color---
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   GRAY = '\033[2m'
   KURSIV = '\033[3m'
   END = '\033[0m'

#---Printing matrix---
def print_matrix(matrix):
    print "\t"
    for i in range(N):
        print "\t",int(matrix[0,i,0]),\
              "\t",int(matrix[0,i,1]),\
              "\t",int(matrix[0,i,2]),\
              "\t",int(matrix[0,i,3]),\
              "\t",int(matrix[0,i,4]),"\n"
print_matrix(matrix)          #Printing initial matrix

#---Leaderboard---
def leaderboard(name, point, filename):
    outfile = open(filename,'a')
    outfile.write('%s %.d\n'%(name,point))
    outfile.close()
    infile = open(filename,'r')
    names = []; points = []
    for line in infile:
        objects = line.split()
        names.append(objects[0])
        points.append(int(objects[1]))
    infile.close()
    indices = sorted(range(len(points)), key=lambda k: points[k])
    points = sorted(points); points = list(reversed(points))
    names_sorted = []; indices = list(reversed(indices))
    for i in range(len(names)):
        names_sorted.append(names[indices[i]])
    print '--------------------------------------'
    print 'Top 10 highscores of all time:'
    print '--------------------------------------'
    if len(names)>10:
        for i in range(10):
            print '%d. %s\t \t\t\t %d'%(i+1,names_sorted[i],int(points[i]))
    else:
        for i in range(len(names)):
            print '%d. %s\t \t\t\t %d'%(i+1,names_sorted[i],int(points[i]))
    print '--------------------------------------'

while True:
    time.sleep(1)  # Delay for 1 second
    tiles = 0
    for i in range(N-1):
        for j in range(M):
            if matrix[0,N-2-i,j] != 0:
                matrix[0,N-1-i,j] += matrix[0,N-2-i,j]
                matrix[0,N-2-i,j] = 0
                tiles += 1
    if tiles == 0:
        matrix[0, 0, int(M/2.)] = np.random.choice(pick_list)
    print_matrix(matrix)
    
