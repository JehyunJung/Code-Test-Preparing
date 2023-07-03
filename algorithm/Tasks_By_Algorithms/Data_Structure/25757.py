import sys
def solution():
    print(len(players) // (games[game_type]-1))

if __name__ == "__main__":
    sys.stdin=open("input25757.txt","r")
    n,game_type=map(str,input().split())
    n=int(n)
    players=set([input().strip() for _ in range(n)])
    
    games={"Y":2,"F":3,"O":4}
    solution()

