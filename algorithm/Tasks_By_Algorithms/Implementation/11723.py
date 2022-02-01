num=0
operations=[]

with open("input11723.txt","r") as file:
  num=int(file.readline())
  for _ in range(num):
    operations.append(list(map(str,file.readline().split())))
    
test_set=set()
for idx in range(num):
    operation=operations[idx][0]
    if operation =="all":
        test_set=set([i for i in range(1,21)])
    elif operation=="empty":
        test_set=set()
    else:
        option=int(operations[idx][1])
        if operation == "add":
            test_set.add(option)
        elif operation == "check":
            if option in test_set:
                print(1)
            else:
                print(0)
        elif operation == "remove":
            test_set.discard(option)
        elif operation == "toggle":
            if option in test_set:
                test_set.remove(option)
            else:
                test_set.add(option)
        
                         
                         
                       