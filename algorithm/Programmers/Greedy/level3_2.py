def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    camera_location=-30001
    
    for route in routes:
        if camera_location < route[0]:
            answer+=1
            camera_location=route[1]
    
    return answer
if __name__ == "__main__":
    num=0
    routes=[]
    with open("input3_2.txt","r") as file:
        num=int(file.readline())
        routes=[list(map(int,file.readline().split())) for _ in range(num)]
    solution(routes)