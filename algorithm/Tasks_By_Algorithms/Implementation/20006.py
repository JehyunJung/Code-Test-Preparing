def solution():
    room_count=0
    rooms=[]
    for level, nickname in waitings:
        level=int(level)
        flag=False
        for index in range(room_count):
            if rooms[index]["player_level"]-10<=level<=rooms[index]["player_level"]+10 and len(rooms[index]["players"]) != m:
                rooms[index]["players"].append((level,nickname))
                flag=True
                break
        if not flag:
            rooms.append({"player_level":level,"players":[(level,nickname)]})
            room_count+=1
        

    for index in range(room_count):
        if len(rooms[index]["players"]) == m:
            print("Started!")
        else:
            print("Waiting!")
        rooms[index]["players"].sort(key=lambda x: x[1])
        for level, nickname in rooms[index]["players"]:
            print(level,nickname)
                
if __name__ == "__main__":
    with open("input20006.txt","r") as file:
        n,m=map(int,file.readline().split())
        waitings=[list(file.readline().split()) for _ in range(n)]
    
    solution()