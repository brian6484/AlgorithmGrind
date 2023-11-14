from sys import stdin

input = stdin.readline

def bf():
    # inf를 사용하지 않고 임의의 큰 수 사용
    D = [200000000] * (N+1)
    # 어느 점을 기준으로 해도 상관없음
    D[1] = 0

    # N번 검사 
    for i in range(N):
        for rou in route:
            start, goal, time = rou
            if D[goal] > D[start] + time:
                D[goal] = D[start] + time
                # N번 시행시 갱신된다면, 음의 가중치 판단.
                if i == N-1:
                    return 'YES'
    return 'NO'


# 변수 입력
TC = int(input())

for _ in range(TC):
    N, M, W = map(int,input().split())
    route = []
    for _ in range(M):
        a, b, t = map(int,input().split())
        route.append([a,b,t])
        route.append([b,a,t])

    for _ in range(W):
        s, e, t = map(int,input().split())
        route.append([s,e,-t])


    print(bf())
