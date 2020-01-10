# CISC 365 - Lab 2 (Assignment 1)
# September 22nd, 2019
# Created by David Kubik (20029272)
#I certify that this submission contains my own work, except as noted.

def dijkstra(start, end, setOfFlights):
    '''This function contains a modified version of Dijkstra's Algorithm that uses a priority queue to find the optimal path from
       a starting city to a destination city.'''

    startingVertex = {} #Starting vertex for each path
    startingVertex[start] = -1
    visited = {} #Previously visited vertices
    minimumCost = -1 
    priorityQueue = {}
    priorityQueue[start] = 0

    while bool(priorityQueue):
        '''While bool takes in the priority queue and finds the fastest arrival time.'''
        departingVertex = -1 
        minimum = 99999999 
        for v in priorityQueue: #Iterates through the queue to find a faster time.
            if priorityQueue[v] < minimum:
                minimum = priorityQueue[v]
                departingVertex = v
        if departingVertex == -1: #If the departing vertex 
            break
        elif departingVertex == end:
            minimumCost = minimum
            break
        del priorityQueue[departingVertex] #Delete the current vertex from the priority queue.
        visited[departingVertex] = 1 #Set the vertex as previously visited.
        currentCost = minimum
        for flightInfo in setOfFlights[departingVertex]:
            '''Iterates through the flight infortmation of each vertex or city.'''
            arrivalVertex = flightInfo[0]
            if arrivalVertex in visited:
                continue
            departingTime = flightInfo[1]
            arrivalTime = flightInfo[2]
            if departingTime > currentCost:
                if arrivalVertex not in priorityQueue:
                    priorityQueue[arrivalVertex] = arrivalTime
                    startingVertex[arrivalVertex] = departingVertex
                else:
                    if priorityQueue[arrivalVertex] > arrivalTime:
                        priorityQueue[arrivalVertex] = arrivalTime
                        startingVertex[arrivalVertex] = departingVertex
                        
    return minimumCost, startingVertex


snIn = open("2019_Lab_2_flights_real_data.txt", "r")
flights = {} 
i = 0

for line in snIn:
    '''For loop that reads each line and assigns the starting city, destination city, departing time and
       arrival time and then appends it to the set of flights.'''
    if i == 0:
        n = int(line.split()[0])
    else:
        l = line.split()
        startVertex = int(l[0])
        endVertex = int(l[1])
        departureTime = int(l[2])
        arrivalTime = int(l[3])
        
        if startVertex not in flights:
            flights[startVertex] = []
        flights[startVertex].append((endVertex, departureTime, arrivalTime))
    i = i + 1

#Take the starting city and the ending city and find the fastest arrival time and origin.
start = int(input("Please enter the starting city: "))
end = int(input("Please enter the destination city: "))
minimumCost, x = dijkstra(start, end, flights) 

if minimumCost == -1:
    print("Unfortunately, there is no route from " + str(start) + " to " + str(end) + ".")
else:
    current = end
    path = [] #Stack that takes the path from the modified version of Dijkstra's Algorithm
    path.append(current)
    while current != start:
        current = x[current]
        path.append(current)

    #Prints out the results
    print("Optimal route from vertex " +str(start)+ " to " +str(end)+ " is:")
    for i in reversed(path):
        print (i)
    print ("The arrival time is: " +str(minimumCost))



        






    
