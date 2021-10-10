from binary_search_iteration import binary_search
n,k=0,0
components=[]
orders=[]

"""
#이진 탐색을 활용하는 방식
with open("input.txt","r") as file:
  n=int(file.readline())
  components=list(map(int,file.readline().split()))

  k=int(file.readline())
  orders=list(map(int,file.readline().split()))

components.sort()

for order in orders:
  if binary_search(components,order,0,len(components)):
    print("yes",end=" ")
  else:
    print("no",end=" ")
print()
"""
#Set을 활용하는 방식
with open("input.txt","r") as file:
  n=int(file.readline())
  components=set(map(int,file.readline().split()))

  k=int(file.readline())
  orders=list(map(int,file.readline().split()))

for order in orders:
  if order in components:
    print("yes",end=" ")
  else:
    print("no",end=" ")
print()
