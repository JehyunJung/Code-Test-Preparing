from copy import deepcopy
def move(start_location,amount):
    conversion={start:[i for i in range(start+1,start+6)] for start in range(18)}
    conversion[17]=[18,19,20,21,21]
    conversion[18]=[19,20,21,21,21]
    conversion[19]=[20,21,21,21,21]
    conversion[20]=[21,21,21,21,21]
    conversion[5] =[22,23,24,25,31]
    conversion[10]=[26,27,25,31,32]
    conversion[15]=[28,29,30,25,31]
    conversion[22]=[23,24,25,31,32]
    conversion[23]=[24,25,31,32,20]
    conversion[24]=[25,31,32,20,21]
    conversion[25]=[31,32,20,21,21]
    conversion[26]=[27,25,31,32,20]
    conversion[27]=[25,31,32,20,21]
    conversion[28]=[29,30,25,31,32]
    conversion[29]=[30,25,31,32,20]
    conversion[30]=[25,31,32,20,21]
    conversion[31]=[32,20,21,21,21]
    conversion[32]=[20,21,21,21,21]

    return conversion[start_location][amount]

def check_if_horse_exists(expected_location,horses,horse_index):
    for index in range(4):
        if index == horse_index:
            continue

        if horses[index]==expected_location:
            return True
    return False

def dfs(cnt,horses,result):
    global max_result
    
    if cnt==10:
        max_result=max(max_result,result)
        return

    for horse_index in range(4):
        if horses[horse_index] == 21:
            continue
        new_location=move(horses[horse_index],dices[cnt]-1)
        #도착칸에는 여러개의 말이 있을 수 있다.
        if new_location ==21 or not check_if_horse_exists(new_location,horses,horse_index):
            temp=deepcopy(horses)
            temp[horse_index]=new_location
            dfs(cnt+1,temp,result+graph[new_location])

if __name__ == "__main__":
    dices=[]
    max_result=0
    graph=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,13,16,19,25,22,24,28,27,26,30,35]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input17825.txt","r") as file:
        dices=list(map(int,file.readline().split()))
    
    dfs(0,[0,0,0,0],0)
    print(max_result)