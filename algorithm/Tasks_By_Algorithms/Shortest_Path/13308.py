from math import inf
from heapq import heappush,heappop
def solution():
    distances=[[inf] * 6 for _ in range(n_vertex+1)]
    heap=[]

    distances[1][oil_costs[1]]=0

    heappush(heap,(0,oil_costs[1],1))

    while heap:
        distance,cost,vertex=heappop(heap)

        if vertex==n_vertex:
            return distance
        
        if distance > distances[vertex][cost]:
            continue


        print("vertex: {},oil_cost:{},distance:{}".format(vertex,oil_costs[vertex],distance))
        for adj_vertex,next_distance in graph[vertex]:
            next_cost=min(cost,oil_costs[adj_vertex])
            print("adj_vertex: {} , {} ,{}".format(adj_vertex,distance + cost * next_distance, distances[adj_vertex][cost]))
            if distance + cost * next_distance < distances[adj_vertex][cost]:
                distances[adj_vertex][cost]=distance + cost * next_distance 
                heappush(heap,(distances[adj_vertex][cost],next_cost,adj_vertex))



if __name__ =="__main__":
    n_vertex,n_edge=0,0
    graph=[]
    oil_costs=[]

    with open("input13308.txt","r") as file:
        n_vertex,n_edge=map(int,file.readline().split())
        oil_costs=list(map(int,file.readline().split()))
        
        graph=[[] for _ in range(n_vertex+1)]

        for _ in range(n_edge):
            v1,v2,distance=map(int,file.readline().split())
            graph[v1].append((v2,distance))
            graph[v2].append((v1,distance))
    oil_costs.insert(0,0)
    print(solution())
        
