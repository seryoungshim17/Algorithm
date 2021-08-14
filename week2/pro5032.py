import sys
input = sys.stdin.readline

if __name__ == '__main__':
    e, f, c = map(int, input().split())
    # 갖고 있는 병 + 주운 병
    empty = e + f
    
    soda = 0
    while empty >= c:
        # 새로운 음료수, 남은 빈 병
        new_soda, empty = empty // c, empty % c
        soda += new_soda
        # 새로운 음료수 빈 병
        empty += new_soda
    print(soda)