from collections import defaultdict
def solution():
    keyword_count=n
    for note_keywords in notes:
        for keyword in note_keywords:
            if keyword in keywords:
                keyword_count-=1
                keywords.remove(keyword)
                
        print(keyword_count)


if __name__ == "__main__":
    with open("input22233.txt","r") as file:
        n,m=map(int,file.readline().split())
        keywords=set()
        
        for _ in range(n):
            keyword=file.readline().strip()
            keywords.add(keyword)
        
        notes=[list(map(str,file.readline().strip().split(","))) for _ in range(m)]
    
    solution()
        