arr = ['A', 'B', 'C', 'D']
N = len(arr)

for i in range(N-2): # 맨뒤의 인덱스 요소는 뒤에 오는 인덱스가 없기에 N-2
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(arr[i], arr[j], arr[k])

# 앞의 인덱스가 뒤의 인덱스보다 값이 작다
# 현재 인덱스의 뒤의 인덱스만 선택해 조합을 만든다.

arr = ['A', 'B', 'C', 'D']
N = len(arr)
R = 3
pick = [0] * R
def backtrack(k, start):
    if k == R:
        print(pick)
    else:

        for i in range(start, N):
            # k번째 원소로 i를 선택
            pick[k] = arr[i]
            backtrack(k+1, i+1)
backtrack(0, 0)

# 1차원 배열을 2분할 하고 싶음
N = 5
arr = [i for i in range(N)]

# 2분할 => 모든 분할 위치는 4곳
for i in range(1, N):
    print(arr[:i], arr[i:])

# 3분할 => 두번 나눌 때 4C2 = 6
for i in range(1, N-1):
    for j in range(i+1, N):
        print(arr[:i], arr[i:j], arr[j:])

# 2차 배열 분할 => 케이크를 4등분 할때 딸기 토핑이 동일하기 분할해라
N = 5
arr = [[0] * N for _ in range(N)]

for i in range(1, N):
    for j in range(1, N):
        # 1번 영역
        for r in range(0, i):
            for c in range(0, j):
                arr[r][c] = '-'
        # 2번 영역
        for r in range(0, i):
            for c in range(j, N):
                arr[r][c] = '+'
        # 3번 영역
        for r in range(i, N):
            for c in range(0, j):
                arr[r][c] = '+'
        # 4번 영역
        for r in range(i, N):
            for c in range(j, N):
                arr[r][c] = '-'

        for line in arr:
            print(*line)
        print('----------')