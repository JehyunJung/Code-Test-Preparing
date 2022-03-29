from collections import deque
def solution():
  numbers=deque()
  for i in range(10):
    numbers.append(str(i))

  if n <10:
    print(numbers[n])
    return
  index=9
  
  while True:
    number=numbers.popleft()
    for i in range(0,10):
      if int(number[-1]) <= i: 
        break
      new_number=number+str(i)
      if int(new_number)>=1000000:
        return -1
      numbers.append(new_number)
      index+=1
      if index==n:
        return numbers[-1]
      index+=1
  print(-1)
    
  
if __name__ == "__main__":
  n=0
  with open("input1038.txt","r") as file:
    n=int(file.readline())
  answer=solution()
  print(answer)
  