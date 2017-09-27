import numpy as np
import random

#---To fix---
#Bug: When you're stuck, the game shouldn't give you another new tile
#Make program as universial as possible: adjust size with one click
#pick_list: need to fill a list with x elements with a certain value
#Make all time best list (need pointer)

#Variables
N = 4                   #System size, NxN
M = 2                   #Starting multiplicator
goal = M**11            #Goal (usually M**11, ex: 2**11=2048)
prob_doubleM = 1/10.    #Probability of getting 2*M, fraction
points = 0              #Initial points

#---Creating matrix---
matrix = np.zeros([N, N])

#---Initial number position---
def ran_pos():
    row = np.random.randint(0, N)
    column = np.random.randint(0, N)
    return row, column
'''
#---Pick number of 2*M correctly---
tol = 0.01
freq_doubleM = 1./prob_doubleM
count = 1
while abs(freq_doubleM-int(freq_doubleM))>tol:
    freq_doubleM = freq_doubleM*2
    count += 1
pick_list = []      #Filled with freq_doubleM Ms
for i in range(count):
    pick_list[i]=2*M
'''
pick_list=[4,2,2,2,2,2,2,2,2,2]

#---Set value to two random tiles---
i, j = ran_pos()
matrix[i, j] = random.choice(pick_list)        #Pick randomly from pick_list
m = 0
while m == 0:
    i, j = ran_pos()
    if matrix[i,j] == 0:
        matrix[i,j] = random.choice(pick_list)
        m += 1

#---Print matrix---
def print_matrix():
    print matrix[0,0],"\t",matrix[0,1],"\t",matrix[0,2],"\t",matrix[0,3],"\n"
    print matrix[1,0],"\t",matrix[1,1],"\t",matrix[1,2],"\t",matrix[1,3],"\n"
    print matrix[2,0],"\t",matrix[2,1],"\t",matrix[2,2],"\t",matrix[2,3],"\n"
    print matrix[3,0],"\t",matrix[3,1],"\t",matrix[3,2],"\t",matrix[3,3],"\n"
print_matrix()          #Printing initial matrix

num_goal = 0            #Number of times goal is reached

while True:
    arrow = raw_input("Please use 'w', 's', 'a' and 'd' to move the tiles: ")
    moves = 0

    #UpArrow
    if arrow == "w":
        i=0

        #---Move the tiles---
        for j in range(N):
            if matrix[i,j]!=0 or matrix[i+1,j]!=0 or matrix[i+2,j]!=0 or matrix[i+3,j]!=0:

                if matrix[i,j]==0:
                    while matrix[i,j]==0:
                        for n in range(0,N-1):
                            matrix[i+n,j]=matrix[i+n+1,j]
                        matrix[i+N-1,j]=0
	                
                if matrix[i+1,j]==0 and (matrix[i+2,j]!=0 or matrix[i+3,j]!=0):
                    while matrix[i+1,j]==0:
                        for n in range(N-2):
                            matrix[i+1+n,j]=matrix[i+2+n,j]
                        matrix[i+N-1,j]=0
	                
                if matrix[i+2,j]==0 and (matrix[i+3,j]!=0):
                    while matrix[i+2,j]==0:
                        for n in range(N-3):
                            matrix[i+2+n,j]=matrix[i+3+n,j]  
                        matrix[i+N-1,j]=0
    
                '''
                for p in range(N-2):
                    if matrix[i+1+p,j]==0 and (matrix[i+2+p,j]!=0 or ... or matrix[i+N-1,j]!=0):
                        while matrix[i+1+p]==0:
                            for n in range(N-1-p):
                                matrix[i+1+p+n,j]=matrix[i+2+p+n,j]
                            matrix[i+N-1,j]=0
                '''
	
        i=0
	
        #---Merge the tiles---
        for j in range(N):
            if matrix[i,j]==matrix[i+1,j]:
                matrix[i,j]=matrix[i,j]+matrix[i+1,j]
                matrix[i+1,j]=matrix[i+2,j]
                matrix[i+2,j]=matrix[i+3,j]
                matrix[i+3,j]=0
                points += matrix[i,j]
                if matrix[i,j] == goal:
                    num_goal += 1
                moves += 1
	            
            if matrix[i+1,j]==matrix[i+2,j]:
                matrix[i+1,j]=matrix[i+1,j]+matrix[i+2,j]
                matrix[i+2,j]=matrix[i+3,j]
                matrix[i+3,j]=0
                points += matrix[i+1,j]
                if matrix[i+1,j] == goal:
                    num_goal += 1
                moves += 1
	            
            if matrix[i+2,j]==matrix[i+3,j]:
                matrix[i+2,j]=matrix[i+2,j]+matrix[i+3,j]
                matrix[i+3,j]=0
                points += matrix[i+2,j]
                if matrix[i+2,j] == goal:
                    num_goal += 1
                moves += 1
                            
    #DownArrow
    if arrow == "s":
        i=0

        #---Move the tiles---
        for j in range(N):
            if matrix[i,j]!=0 or matrix[i+1,j]!=0 or matrix[i+2,j]!=0 or matrix[i+3,j]!=0:

                if matrix[i+3,j]==0:
                    while matrix[i+3,j]==0: 
                        matrix[i+3,j]=matrix[i+2,j]   
                        matrix[i+2,j]=matrix[i+1,j]    
                        matrix[i+1,j]=matrix[i,j]    
                        matrix[i,j]=0
                        moves += 1
	                
                if matrix[i+2,j]==0 and (matrix[i+1,j]!=0 or matrix[i,j]!=0):
                    while matrix[i+2,j]==0:  
                        matrix[i+2,j]=matrix[i+1,j]    
                        matrix[i+1,j]=matrix[i,j]
                        matrix[i,j]=0
                        moves += 1
	                
                if matrix[i+1,j]==0 and (matrix[i,j]!=0):
                    while matrix[i+1,j]==0:
                        matrix[i+1,j]=matrix[i,j]   
                        matrix[i,j]=0
                        moves += 1
	
        i=0
	
        #---Merge the tiles---
        for j in range(N):
            if matrix[i+3,j]==matrix[i+2,j]:
                matrix[i+3,j]=matrix[i+3,j]+matrix[i+2,j]
                matrix[i+2,j]=matrix[i+1,j]
                matrix[i+1,j]=matrix[i,j]
                matrix[i,j]=0
                points += matrix[i+3,j]
                if matrix[i+3,j] == goal:
                    num_goal += 1
                moves += 1
	            
            if matrix[i+2,j]==matrix[i+1,j]:
                matrix[i+2,j]=matrix[i+2,j]+matrix[i+1,j]
                matrix[i+1,j]=matrix[i,j]
                matrix[i,j]=0
                points += matrix[i+2,j]
                if matrix[i+2,j] == goal:
                    num_goal += 1
                moves += 1
	            
            if matrix[i+1,j]==matrix[i,j]:
                matrix[i+1,j]=matrix[i+1,j]+matrix[i,j]
                matrix[i,j]=0
                points += matrix[i+1,j]
                if matrix[i+1,j] == goal:
                    num_goal += 1
                moves += 1

    #LeftArrow
    if arrow == "a":
        j=0

        #---Move the tiles---
        for i in range(N):
            if matrix[i,j]!=0 or matrix[i,j+1]!=0 or matrix[i,j+2]!=0 or matrix[i,j+3]!=0:

                if matrix[i,j]==0:
                    while matrix[i,j]==0: 
                        matrix[i,j]=matrix[i,j+1]   
                        matrix[i,j+1]=matrix[i,j+2]    
                        matrix[i,j+2]=matrix[i,j+3]    
                        matrix[i,j+3]=0
                        moves += 1
	                
                if matrix[i,j+1]==0 and (matrix[i,j+2]!=0 or matrix[i,j+3]!=0):
                    while matrix[i,j+1]==0:  
                        matrix[i,j+1]=matrix[i,j+2]    
                        matrix[i,j+2]=matrix[i,j+3]
                        matrix[i,j+3]=0
                        moves += 1
	                
                if matrix[i,j+2]==0 and (matrix[i,j+3]!=0):
                    while matrix[i,j+2]==0:
                        matrix[i,j+2]=matrix[i,j+3]   
                        matrix[i,j+3]=0
                        moves += 1
	
        j=0
	
        #---Merge the tiles---
        for i in range(N):
            if matrix[i,j]==matrix[i,j+1]:
                matrix[i,j]=matrix[i,j]+matrix[i,j+1]
                matrix[i,j+1]=matrix[i,j+2]
                matrix[i,j+2]=matrix[i,j+3]
                matrix[i,j+3]=0
                points += matrix[i,j]
                if matrix[i,j] == goal:
                    num_goal += 1
                moves += 1
	            
            if matrix[i,j+1]==matrix[i,j+2]:
                matrix[i,j+1]=matrix[i,j+1]+matrix[i,j+2]
                matrix[i,j+2]=matrix[i,j+3]
                matrix[i,j+3]=0
                points += matrix[i,j+1]
                if matrix[i,j+1] == goal:
                    num_goal += 1
                moves += 1
	            
            if matrix[i,j+2]==matrix[i,j+3]:
                matrix[i,j+2]=matrix[i,j+2]+matrix[i,j+3]
                matrix[i,j+3]=0
                points += matrix[i,j+2]
                if matrix[i,j+2] == goal:
                    num_goal += 1
                moves += 1

    if arrow == "d":
        j=0

        #---Move the tiles---
        for i in range(N):
            if matrix[i,j]!=0 or matrix[i,j+1]!=0 or matrix[i,j+2]!=0 or matrix[i,j+3]!=0:

                if matrix[i,j+3]==0:
                    while matrix[i,j+3]==0: 
                        matrix[i,j+3]=matrix[i,j+2]   
                        matrix[i,j+2]=matrix[i,j+1]    
                        matrix[i,j+1]=matrix[i,j]    
                        matrix[i,j]=0
                        moves += 1
	                
                if matrix[i,j+2]==0 and (matrix[i,j+1]!=0 or matrix[i,j]!=0):
                    while matrix[i,j+2]==0:  
                        matrix[i,j+2]=matrix[i,j+1]    
                        matrix[i,j+1]=matrix[i,j]
                        matrix[i,j]=0
                        moves += 1
	                
                if matrix[i,j+1]==0 and (matrix[i,j]!=0):
                    while matrix[i,j+1]==0:
                        matrix[i,j+1]=matrix[i,j]   
                        matrix[i,j]=0
                        moves += 1
	
        j=0
	
        #---Merge the tiles---
        for i in range(N):
            if matrix[i,j+3]==matrix[i,j+2]:
                matrix[i,j+3]=matrix[i,j+3]+matrix[i,j+2]
                matrix[i,j+2]=matrix[i,j+1]
                matrix[i,j+1]=matrix[i,j]
                matrix[i,j]=0
                points += matrix[i,j+3]
                if matrix[i,j+3] == goal:
                    num_goal += 1
                moves += 1
	            
            if matrix[i,j+2]==matrix[i,j+1]:
                matrix[i,j+2]=matrix[i,j+2]+matrix[i,j+1]
                matrix[i,j+1]=matrix[i,j]
                matrix[i,j]=0
                points += matrix[i,j+2]
                if matrix[i,j+2] == goal:
                    num_goal += 1
                moves += 1
	            
            if matrix[i,j+1]==matrix[i,j]:
                matrix[i,j+1]=matrix[i,j+1]+matrix[i,j]
                matrix[i,j]=0
                points += matrix[i,j+1]
                if matrix[i,j+1] == goal:
                    num_goal += 1
                moves += 1

    #---Add 'M' on random empty spot---
    listfori = []
    listforj = []

    counter = 0
    for i in range(4):
        for j in range(4):
            if matrix[i,j]==0:
                counter+=1
                listfori.append(i)
                listforj.append(j)
        
    if counter > 0:
        if moves > 0:
            if counter > 1:
                randomindex = listfori.index(random.choice(listfori))
                matrix[listfori[randomindex],listforj[randomindex]] = random.choice(pick_list)
                #print matrix
                print_matrix()
                #print moves
                print "Points: ",int(points)
            else:
                matrix[listfori[0]][listforj[0]] = random.choice(pick_list)
                #print matrix
                print_matrix()
                #print moves
                print "Points: ",int(points)
        else:
            print "Please swipe in another direction!"
        
    else:
        break
        print "Game over"
    if num_goal > 0:
        print "Congratulation, you've reached %.d for the %.d. time"%(goal,num_goal)
