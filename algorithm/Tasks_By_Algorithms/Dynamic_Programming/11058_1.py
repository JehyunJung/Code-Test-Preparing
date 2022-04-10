from collections import deque
def solution():
  queue=deque()
  #step,clipboard,count
  queue.append((0,0,0))
  answer=0
  while queue:
    step,clipboard,count=queue.popleft()
    if step>n:
      continue
    if step==n:
      answer=max(answer,count)

    if clipboard > 0:
      queue.append((step+1,clipboard,count+clipboard))
    queue.append((step+2,count,count))
    queue.append((step+1,clipboard,count+1))
  
  return answer

if __name__ =="__main__":
  n=0
  with open("input11058.txt","r") as file:
    n=int(file.readline())
  print(solution())