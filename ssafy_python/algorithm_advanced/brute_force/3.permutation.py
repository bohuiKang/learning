path = []
# used = [False, False, False] # 고를 수 있는 수 만큼 만든다.
# used = [False] * N # N개의 카드 종류가 있는 경우

used = [False] * 7 # 1~6까지의 카드 숫자 사용여부를 기록 (0을 버린다)


def recur(cnt):
    if cnt == 3:
        print(*path)
        return

    for num in range(1, 7): # 6개의 카드
        # in 을 쓰면 리스트 전부를 다 확인
        # if num in path: # 이미 path에 있는 숫자는 생략
        #     continue
        if used[num]:
            continue

        used[num] = 1
        path.append(num)
        recur(cnt + 1)
        path.pop()
        used[num] = 0

recur(0)
