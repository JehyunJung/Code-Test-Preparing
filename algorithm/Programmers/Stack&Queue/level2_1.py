def solution(progresses, speeds):
    answer = []
    time,count=0,0
    
    while len(progresses) > 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count+=1
        else:
            if count>0:
                answer.append(count)
            time+=1
            count=0
    answer.append(count)

    return answer

if __name__ == "__main__":
  progresses=[]
  speeds=[]

  with open("level2_1.txt","r") as file:
    progresses=list(map(int,file.readline().split()))
    speeds=list(map(int,file.readline().split()))
  
  print(solution(progresses, speeds))