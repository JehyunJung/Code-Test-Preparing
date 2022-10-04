def solution(remaining_players,guilty_point,nights):
    global max_nights
    #모든 시민이 죽은 경우
    if remaining_players==1:
        max_nights=max(max_nights,nights)
        return
    
    #밤인경우
    if remaining_players % 2==0:
        for i in range(N):
            if i == mafia: 
                continue
            if killed[i]:
                continue

            #특정 참가자를 죽이는 경우
            temp_guilty_point=[0]*N
            for j in range(N):
                if i==j:
                    temp_guilty_point[j]=guilty_point[j]
                else:
                    temp_guilty_point[j]=guilty_point[j]+reactions[i][j]

            killed[i]=True         
            solution(remaining_players-1,temp_guilty_point,nights+1)
            killed[i]=False
    #낮인 경우
    else:
        max_point=0
        candidate=0
        for i in range(N):
            if killed[i]:
                continue
            if guilty_point[i] > max_point:
                max_point=guilty_point[i]
                candidate=i
        
        #마피아가 죽는 경우
        if candidate==mafia:
            max_nights=max(max_nights,nights)
            return
        killed[candidate]=True
        solution(remaining_players-1,guilty_point,nights)
        killed[candidate]=False


if __name__ == "__main__":
    N=0
    guilty_point=[]
    reactions=[]
    mafia=0
    max_nights=0
    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input1079.txt","r") as file:
        N=int(file.readline())
        guilty_point=list(map(int,file.readline().split()))
        reactions=[list(map(int,file.readline().split())) for _ in range(N)]
        mafia=int(file.readline())
    killed=[False]*N
    solution(N,guilty_point,0)

    print(max_nights)