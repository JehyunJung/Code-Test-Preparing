def solution(array, commands):
    answer = []
    for i,j,k in commands:
        sub_array=array[i-1:j]
        sub_array.sort()
        answer.append(sub_array[k-1]) 
    return answer

if __name__ == "__main__":
  array=[]
  commands=[]
  with open("level1.txt","r") as file:
    array=list(map(int,file.readline().split()))
    n=int(file.readline())
    for _ in range(n):
      commands.append(list(map(int,file.readline().split())))
  print(solution(array,commands))