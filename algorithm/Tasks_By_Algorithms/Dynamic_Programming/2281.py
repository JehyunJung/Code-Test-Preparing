from math import inf
def solution():
    answer=inf
    for remaining in range(width+1):
        temp=0
        blanks=0
        index=-1
        while index < num:
            index+=1
            temp+=numbers[index]
          
            if index==num-1:
                if blanks==0:
                    blanks=(width-temp)**2
                break
                
            if temp > width:
                blanks+=(width-(temp-1-numbers[index]))**2
                temp=0
                index-=1
                continue
     
            if width-temp < remaining:
                blanks+=(width-temp)**2
                temp=0
                continue           
            temp+=1
          
        answer=min(answer,blanks)
    print(answer)  
          
if __name__ == "__main__":
    num,width=0,0
    numbers=[]
    with open("input2281.txt","r") as file:
        num,width=map(int,file.readline().split())
        numbers=[int(file.readline()) for _ in range(num)]
    solution()