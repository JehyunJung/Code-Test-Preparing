def solution(N, number):
    answer = -1
    sets=[set() for _ in range(9)]
    for i in range(1,9):
        sets[i].add(int(str(N)*i))
        for j in range(i):
            for op1 in sets[j]:
                for op2 in sets[i-j]:     
                    sets[i].add(op1+op2)
                    sets[i].add(op1-op2)
                    sets[i].add(op1*op2)
                    if op2 !=0:
                        sets[i].add(op1//op2)
                        
        if number in sets[i]:
            answer=i
            break
            
    return answer
if __name__ =="__main__":
    N,number=0,0
    with open("level3_1.txt","r") as file:
        N,number=map(int,file.readline().split())
    print(solution(N,number))