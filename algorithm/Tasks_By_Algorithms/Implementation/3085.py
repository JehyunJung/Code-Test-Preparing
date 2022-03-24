def candy_matcher(graph):
  max_length=0
  for i in range(n):
    for j in range(n):
      candy_color=graph[i][j]
      length=0
      for adj_i in range(n-i):
        if graph[i+adj_i][j] == candy_color:
          length+=1
      max_length=max(length,max_length)
      length=0
      for adj_j in range(n-j):
        if graph[i][j+adj_j] == candy_color:
          length+=1
      max_length=max(length,max_length)
  return max_length

def print_map(count,graph):
  print("move:",count)
  for i in range(n):
    print(graph[i])
print()
      
def solution():
  answer=0
  count=0
  for i in range(n):
    for j in range(n):
      if j <n-1 and candy_map[i][j] != candy_map[i][j+1]:
        count+=1
        candy_map[i][j],candy_map[i][j+1]=candy_map[i][j+1],candy_map[i][j]  
        answer=max(candy_matcher(candy_map),answer)

        candy_map[i][j+1],candy_map[i][j]=candy_map[i][j],candy_map[i][j+1]
      if i<n-1 and candy_map[i][j] != candy_map[i+1][j]:
        count+=1
        candy_map[i][j],candy_map[i+1][j]=candy_map[i+1][j],candy_map[i][j]
        answer=max(candy_matcher(candy_map),answer)

        candy_map[i+1][j],candy_map[i][j]=candy_map[i][j],candy_map[i+1][j]
      
  return answer

  
if __name__ == "__main__":
  n=0
  candy_map=[]
  
  with open("input3085.txt","r") as file:
    n=int(file.readline())
    for _ in range(n):
      candy_map.append(list(file.readline().strip()))
  print(solution())