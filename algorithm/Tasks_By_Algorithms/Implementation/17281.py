from itertools import permutations
from collections import deque
def solution():
    max_score=0
    for permutation in permutations([1,2,3,4,5,6,7,8]):
        batter_orders=list(permutation)
        batter_orders.insert(3,0)

        #점수
        score=0       
        #다음 타순
        next_index=0

        #이닝
        for i in range(N):
            #루
            base1,base2,base3=0,0,0
            #아웃
            outs=0    
            #out이 3번이 될때 까지 타순 반복
            while outs < 3:
                option=players[i][batter_orders[next_index]]
                #1루타:
                if option==1:
                    score+=base3
                    base1,base2,base3=1,base1,base2          
                #2루타:
                elif option==2:
                    score+=(base2+base3)
                    base1,base2,base3=0,1,base1
                    
                #3루타:
                elif option==3:
                    score+=(base1+base2+base3)
                    base1,base2,base3=0,0,1

                #홈런 --> 모두 출루
                elif option==4:
                    score+=(base1+base2+base3+1)
                    base1,base2,base3=0,0,0
                #아웃:
                else:
                    outs+=1

                #다음 타선
                next_index=(next_index+1)%9

        max_score=max(max_score,score)

    return max_score


if __name__ == "__main__":
    N=0

    players=[]

    with open("input17281.txt","r") as file:
        N=int(file.readline())
        players=[list(map(int,file.readline().split())) for _ in range(N)]
    
    print(solution())