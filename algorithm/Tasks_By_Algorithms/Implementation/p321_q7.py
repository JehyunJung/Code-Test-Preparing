n=0
with open("input7.txt","r") as file:
  n=file.readline()

input_len=len(n)//2
left=list(map(int,n[:input_len]))
right=list(map(int,n[input_len:]))

if sum(left) == sum(right):
  print("LUCKY")
else:
  print("READY")