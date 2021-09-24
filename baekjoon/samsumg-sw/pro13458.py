import math
import sys
input = sys.stdin.readline

def main():
    N = int(input())        # 시험장 개수 == 총감독관 명수
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    answer = 0
    for student in A:
        if student >= B:
            answer += math.ceil((student-B)/C)
    
    print(answer + N, end="") 


if __name__ == '__main__':
    main()