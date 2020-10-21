import math
from queue import PriorityQueue

def heuristic(start, end):
    #This is a basic function to get a guess on the distance till the end point.  It will be used
    #in each round to find the estimated distance as the "h" in the A* equation.
    x = math.sqrt((start[0]-end[0])**2 + (start[1]-end[1])**2)
    return x

def calc_path(prevnodes, start, end):

    finalpath = [end]
    node = end
    while prevnodes[node] != None:
        finalpath.append(prevnodes[node])
        node = prevnodes[node]
    finalpath.reverse()

    return finalpath

#note, found a sample online to base some of my code on, in one of the knowledge portal questions.
def shortest_path(M, start, end):
    #use a priority queue to keep track of all the nodes that need to be considered for each round
    distq = PriorityQueue()
    #initialize a cost tracker that will be filled in as the nodes are traversed
    target = False
    #This is a bool that will be set to positive when the end node is reached

    #make a dictionary that keeps track of the distance(costs)
    g_tracker = {}
    g_tracker[start] = 0 #dist_from_start
    #maybe not necessary
    distq_dict = {0: start} #need a dictionary for all values that are being stored/ordered in the distance queue- to keep track of the nodes
    #these nodes are ones that have been taken which differ from the nodes that need to be analyzed (frontier nodes)
    prevnodes = {start : None}
    current_node = ''
    while current_node != end:
        best_dist = distq.get()
        #use the priority queue to get the best distance to then get the corresponding node.
        current_node = distq_dict[best_dist]

        for node in M.roads(current_node):
            #this will update all the neighbors gcosts as well as store their new overall costs in the priority queue.  One by one the nodes will be popped and tested to form the right path.
            g_cost = g_tracker[current_node] + heuristic(M.intersections[node], M.intersections[current_node])
            heur = heuristic(M.intersections[node], M.intersections[end]) #called "heur", basically the h value.

            if node not in g_tracker or g_cost < g_tracker[node]:
                g_tracker[node] = g_cost
                prevnodes[node] = current_node#prevnode dict is like the "path" dict in Diijkstra's algorithmm
                overall_cost = g_cost + heur
                print(overall_cost)
                distq.put(overall_cost, node)
                #this is the priority queue of all the nodes to be analyzed for each for loop
                dist_comp[overall_cost] = node


    finalpath = calc_path(prevnodes, start, end)
    return finalpath





