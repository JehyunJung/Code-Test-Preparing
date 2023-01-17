def solution():
    acount=0 
    for char in string:
        if char=="a":
            acount+=1
    
    length=len(string)

    min_count=1000
    for index in range(length):
        count=0
        for offset in range(acount):
            if string[(index+offset)%length]=="b":
                count+=1
        min_count=min(min_count,count)
    
    return min_count

if __name__ == "__main__":
    with open("input1522.txt","r") as file:
        string=file.readline().strip()
    
    print(solution())