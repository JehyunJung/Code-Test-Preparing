from math import inf
def solution(index,temp,blanks):
    global answer
    print("Index:%d Temp: %d Blanks %d" % (index,temp,blanks))
  
    if index == num:
        answer=min(answer,blanks)
        return

    if temp > width:
        return
      
    solution(index+1,temp+1+numbers[index],blanks)
    solution(index+1,numbers[index],blanks+(width-temp)**2)
    
    
          
if __name__ == "__main__":
    num,width=0,0
    numbers=[]
    with open("input2281.txt","r") as file:
        num,width=map(int,file.readline().split())
        numbers=[int(file.readline()) for _ in range(num)]
    answer=inf
    solution(1,numbers[0],0)
    print(answer)