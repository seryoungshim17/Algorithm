import sys
input = sys.stdin.readline

if __name__ == '__main__':
    squares = [[0]*100 for i in range(100)]
    for _ in range(4):
        left_x, left_y, right_x, right_y = map(int, input().split())
        for width in range(left_x, right_x):
            for height in range(left_y, right_y):
                squares[width][height] = 1

    answer = 0
    for i in range(100):
        for j in range(100):
            if squares[i][j]:
                answer += 1

    print(answer)