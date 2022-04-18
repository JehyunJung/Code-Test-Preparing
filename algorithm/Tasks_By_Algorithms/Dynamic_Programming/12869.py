from math import inf
def solution(count,numbers):
    global answer
    if numbers[0]<=0 and numbers[1]<=0 and numbers[2]<=0:
        answer=min(answer,count)
        return
      
    for i in range(3):
        if num >2:
            numbers.sort(reverse=True)
            solution(count+1,[numbers[0]-ways[i][0],numbers[1]-ways[i][1],numbers[2]-ways[i][2]])
        elif num >1:
            numbers.sort(reverse=True)
            solution(count+1,[numbers[0]-ways[i][0],numbers[1]-ways[i][1],0])
        else:
            numbers.sort(reverse=True)
            solution(count+1,[numbers[0]-ways[i][0],0,0])
        
    
if __name__ == "__main__":
    num=0 
    hp=[]
    with open("input12869.txt","r") as file:
        num=int(file.readline())
        hp=list(map(int,file.readline().split()))
    answer=inf
    ways=[[9,3,1],[9,1,3],[3,9,1]]
    numbers=[0,0,0]
    for i in range(num):
        numbers[i]=hp[i]
    numbers.sort(reverse=True)
    solution(0,numbers)
    print(answer)