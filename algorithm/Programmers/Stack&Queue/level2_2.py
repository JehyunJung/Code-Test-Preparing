from collections import deque
def solution(priorities, location):
    answer = 0
    
    waiting_list=[(index,priority) for index,priority in enumerate(priorities)]
    waiting_list=deque(waiting_list)
    
    while True:
        temp=waiting_list.popleft()
        if any(temp[1]<q[1] for q in waiting_list):
            waiting_list.append(temp)

        else:
            answer+=1
            if temp[0]==location:
                break
        
    return answer

if __name__ == "__main__":
  priorities=[]
  location=0

  with open("level2_2.txt","r") as file:
    priorities=list(map(int,file.readline().split()))
    location=int(file.readline())
  
  print(solution(priorities, location))