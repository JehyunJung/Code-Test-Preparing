from math import sqrt
def solution(brown, yellow):
    
    for i in range(1,int(sqrt(yellow))+1):
        if yellow % i ==0:
            row,col=i,yellow//i
            
            if (row *2 + col*2 + 4) == brown:
                answer=[col+2,row+2]
    
    return answer

if __name__ == "__main__":
  brown,yellow=0,0

  with open("level2_2.txt","r") as file:
    brown,yellow=map(int,file.readline().split())
  print(solution(brown,yellow))