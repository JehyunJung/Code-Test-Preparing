target=58
index=0
num=1

while True:
    if target <= num:
        print(index+1)
        break
    index+=1
    num+=index*6    
    