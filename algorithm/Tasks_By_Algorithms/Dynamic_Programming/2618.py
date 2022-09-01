from math import inf
def solution(index,police1_index,police2_index):
    global dp,path
    
    if index == (n_locations+1):
        return 0

    if dp[police1_index][police2_index] != -1:
        return dp[police1_index][police2_index]

    next_val=locations[index-1]

    distance1=abs(next_val[0]-police1[police1_index][0])+abs(next_val[1]-police1[police1_index][1])+solution(index+1,index,police2_index)
    distance2=abs(next_val[0]-police2[police2_index][0])+abs(next_val[1]-police2[police2_index][1])+solution(index+1,police1_index,index)

    if distance1 < distance2:
        dp[police1_index][police2_index]=distance1
        return distance1
    else:
        dp[police1_index][police2_index]=distance2
        return distance2

def track_path(index,police1_index,police2_index):
    global dp,path
    
    if index == (n_locations+1):
        return 0

    next_val=locations[index-1]

    distance1=abs(next_val[0]-police1[police1_index][0])+abs(next_val[1]-police1[police1_index][1]) + dp[index][police2_index]
    distance2=abs(next_val[0]-police2[police2_index][0])+abs(next_val[1]-police2[police2_index][1]) + dp[police1_index][index]

    if distance1 < distance2:
        print(1)
        track_path(index+1,index,police2_index)
    else:
        print(2)
        track_path(index+1,police1_index,index)



if __name__ == "__main__":
    N=0
    n_locations=0
    locations=[]
    path=[]
    minimum_distance=inf
    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Dynamic_Programming\\input2618.txt","r") as file:
        N=int(file.readline())
        n_locations=int(file.readline())

        for _ in range(n_locations):
            row,col=map(int,file.readline().split())
            locations.append((row-1,col-1))

    path=[0]*n_locations

    police1=[[0,0]] + locations
    police2=[[N-1,N-1]]+ locations

    dp=[[-1]*(n_locations+1) for _ in range(n_locations+1)]

    print(solution(1,0,0))
    track_path(1,0,0)