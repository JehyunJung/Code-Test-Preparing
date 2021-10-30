input_data=[]

with open("input3.txt","r") as file:
  input_data=list(file.readline())

count0,count1=0,0
if input_data[0]=='0':
  count0+=1
else:
  count1+=1

for i in range(1,len(input_data)):
  previous_data,current_data=input_data[i-1],input_data[i]
  if previous_data!=current_data:
    if current_data=='1':
      count1+=1
    else:
      count0+=1

print(min(count1,count0))