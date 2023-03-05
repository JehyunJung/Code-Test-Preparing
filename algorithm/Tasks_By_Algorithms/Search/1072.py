from math import inf
from decimal import Decimal
def solution():
    z=int(Decimal(y)*100/x)
    start,end=1,x
    min_games=inf

    while start <= end:
        
        mid=(start+end)//2

        if int(Decimal(y+mid)*100/(x+mid)) >z:
            min_games=min(min_games,mid)
            end=mid-1
        else:
            start=mid+1

    print(min_games if min_games != inf else -1)        

if __name__ == "__main__":
    with open("input1072.txt","r") as file:
        x,y=map(int,file.readline().split())
    solution()

    print(1/3)
    print(Decimal(1/3*100))
    print(Decimal(1/3)*100)
    print(Decimal(1*100)/3)

