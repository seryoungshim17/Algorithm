import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    first = [i for i in range(1, N+1)]
    second = []

    # 두번째 줄 받아오기
    for _ in range(N):
        second.append(int(input()))
    
    while set(first) != set(second):    # 서로 같지 않으면 갖고 있지 않는 원소쌍 제거
        remove = []
        idx = 0
        # 갖고 있지 않는 원소쌍 위치 찾기
        for (f, s) in zip(first, second):
            if (f not in second) or (s not in first):
                remove.append(idx)
            idx += 1
        # 원소쌍 제거
        while remove:
            i = remove.pop()
            del first[i]
            del second[i]

    # PRINT
    print(len(first))
    for elem in first:
        print(elem)