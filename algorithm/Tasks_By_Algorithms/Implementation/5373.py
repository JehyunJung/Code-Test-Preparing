from copy import deepcopy
def clock_wise(list):
    new_list=[[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            new_list[j][2-i]=list[i][j]
    return new_list

def counter_clock_wise(list):
    new_list=[[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            new_list[j][i]=list[i][2-j]
    return new_list

def solution(operations):
    #윗면,아랫면,앞면,뒷면,왼쪽면,오른쪽면
    dice=[
        [['w'] * 3 for _ in range(3)],
        [['y'] * 3 for _ in range(3)],
        [['r'] * 3 for _ in range(3)],
        [['o'] * 3 for _ in range(3)],
        [['g'] * 3 for _ in range(3)],
        [['b'] * 3 for _ in range(3)]
        ]
    for operation in operations:
        new_dice=deepcopy(dice)
        #윗면
        if operation[0] == "U":
            if operation[1]=="+":
                for i in range(3):
                    new_dice[5][0][i]=dice[3][0][i]
                    new_dice[2][0][i]=dice[5][0][i]
                    new_dice[4][0][i]=dice[2][0][i]
                    new_dice[3][0][i]=dice[4][0][i]
                new_dice[0]=clock_wise(dice[0])

            if operation[1]=="-":
                for i in range(3):
                    new_dice[4][0][i]=dice[3][0][i]
                    new_dice[2][0][i]=dice[4][0][i]
                    new_dice[5][0][i]=dice[2][0][i]
                    new_dice[3][0][i]=dice[5][0][i]                   
                new_dice[0]=counter_clock_wise(dice[0])
        
        #아랫면
        if operation[0] == "D":
            if operation[1]=="+":
                for i in range(3):
                    new_dice[4][2][i]=dice[3][2][i]
                    new_dice[2][2][i]=dice[4][2][i]
                    new_dice[5][2][i]=dice[2][2][i]
                    new_dice[3][2][i]=dice[5][2][i]   
                    
                new_dice[1]=clock_wise(dice[1])
      
            if operation[1]=="-":
                for i in range(3):
                    new_dice[5][2][i]=dice[3][2][i]
                    new_dice[2][2][i]=dice[5][2][i]
                    new_dice[4][2][i]=dice[2][2][i]
                    new_dice[3][2][i]=dice[4][2][i]
                new_dice[1]=counter_clock_wise(dice[1])
        #앞면
        if operation[0] == "F":
            if operation[1]=="+":
                for i in range(3):
                    new_dice[5][i][0]=dice[0][2][i]
                    new_dice[1][0][i]=dice[5][2-i][0]
                    new_dice[4][i][2]=dice[1][0][i]
                    new_dice[0][2][i]=dice[4][2-i][2]
                new_dice[2]=clock_wise(dice[2])

            if operation[1]=="-":
                for i in range(3):
                    new_dice[4][i][2]=dice[0][2][2-i]
                    new_dice[1][0][i]=dice[4][i][2]
                    new_dice[5][i][0]=dice[1][0][2-i]
                    new_dice[0][2][i]=dice[5][i][0]
                    
                new_dice[2]=counter_clock_wise(dice[2])
        #뒷면
        if operation[0] == "B":
            if operation[1]=="+":
                for i in range(3):
                    new_dice[4][i][0]=dice[0][0][2-i]
                    new_dice[1][2][i]=dice[4][i][0]
                    new_dice[5][i][2]=dice[1][2][2-i]
                    new_dice[0][0][i]=dice[5][i][2]
                new_dice[3]=clock_wise(dice[3])
            
            if operation[1]=="-":
                for i in range(3):
                    new_dice[5][i][2]=dice[0][0][i]
                    new_dice[1][2][i]=dice[5][2-i][2]
                    new_dice[4][i][0]=dice[1][2][i]
                    new_dice[0][0][i]=dice[4][2-i][0]
                new_dice[3]=counter_clock_wise(dice[3])
        #왼쪽면
        if operation[0] == "L":
            if operation[1]=="+":
                for i in range(3):
                    new_dice[2][i][0]=dice[0][i][0]
                    new_dice[1][i][0]=dice[2][i][0]
                    new_dice[3][i][2]=dice[1][2-i][0]
                    new_dice[0][i][0]=dice[3][2-i][2]
                new_dice[4]=clock_wise(dice[4])
            
            if operation[1]=="-":
                for i in range(3):
                    new_dice[3][i][2]=dice[0][2-i][0]
                    new_dice[1][i][0]=dice[3][2-i][2]
                    new_dice[2][i][0]=dice[1][i][0]
                    new_dice[0][i][0]=dice[2][i][0]
                new_dice[4]=counter_clock_wise(dice[4])
        #오른쪽면
        if operation[0] == "R":
            if operation[1]=="+":
                for i in range(3):
                    new_dice[3][i][0]=dice[0][2-i][2]
                    new_dice[1][i][2]=dice[3][2-i][0]
                    new_dice[2][i][2]=dice[1][i][2]
                    new_dice[0][i][2]=dice[2][i][2]
                new_dice[5]=clock_wise(dice[5])
            
            if operation[1]=="-":
                for i in range(3):
                    new_dice[2][i][2]=dice[0][i][2]
                    new_dice[1][i][2]=dice[2][i][2]
                    new_dice[3][i][0]=dice[1][2-i][2]
                    new_dice[0][i][2]=dice[3][2-i][0]
                new_dice[5]=counter_clock_wise(dice[5])

        dice=new_dice
    for i in range(3):
        print("".join(dice[0][i]))

if __name__ == "__main__":
    test_cases=0
    
    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input5373.txt","r") as file:
        test_cases=int(file.readline())
        for _ in range(test_cases):
            n_rotates=int(file.readline())
            operations=list(map(str,file.readline().split()))
            solution(operations)