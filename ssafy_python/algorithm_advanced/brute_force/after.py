# 최소합
N = 4
arr = [[0] * N for _ in range(N)]

cnt = 0
def gogo(r, c):
    if r >= N or c >= N: # 경계체크
        return

    arr[r][c] += 1

    if r == N - 1 and c == N - 1:
        global cnt
        cnt += 1 # 마지막에 도착했을 때 +1
        return

    gogo(r, c+1)
    gogo(r+1, c)

gogo(0, 0)

for line in arr:
    print(*line)
print('cnt =', cnt)

# ----------------------------------------------------


# 최소합 - 재귀 이해를 위한
N = 4
arr = [[0] * N for _ in range(N)]


def gogo(r, c):
    if r >= N or c >= N: # 경계체크
        return

    arr[r][c] = 1

    if r == N - 1 and c == N - 1:
        for line in arr:
            print(*line)
        print('-'*N)
        return

    gogo(r, c+1) # 오른쪽
    gogo(r+1, c) # 아래

    arr[r][c] = 0

gogo(0, 0)
