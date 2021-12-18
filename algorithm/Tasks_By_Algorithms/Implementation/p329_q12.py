def checkIfPossible(answer):
    for x,y,a in answer:
        if a==0:
            if y==0:
                continue
            elif [x,y,1] in answer or [x-1,y,1] in answer:
                continue
            elif [x,y-1,0] in answer:
                continue
            return False
        else:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer:
                continue
            elif [x-1,y,1] in answer and [x+1,y,1] in answer:
                continue
            return False
    return True
    
def solution(n, build_frame):
    answer = []

    for x,y,a,b in build_frame:
      print(x,y,a,b)
      if b==0:
          answer.remove([x,y,a])
          if not checkIfPossible(answer):
              answer.append([x,y,a])
      if b==1:
        answer.append([x,y,a])
        if not checkIfPossible(answer):
            answer.remove([x,y,a])
    answer.sort()
    return answer

build_frame=[]
n=0
with open("input12.txt","r") as file:
  n=int(file.readline())
  index=int(file.readline())
  for _ in range(index):
    build_frame.append(list(map(int,file.readline().split())))

print(solution(n,build_frame))
