input_data=[]

with open("input8.txt","r") as file:
  input_data=list(file.readline())

unsorted_list=[]
result=0

for data in input_data:
  if data.isalpha():
    unsorted_list.append(data)

  else:
    result+=int(data)

unsorted_list.sort()

print(''.join(unsorted_list),result,sep="")

