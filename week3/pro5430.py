import sys
from collections import Counter
input = sys.stdin.readline

def cmdPerform(cmd, lst, reverse):
    if cmd == 'R':
        return False, (not reverse)
    elif cmd == 'D':
        if lst == []:
            # 삭제할 원소 없음 -> ERROR
            return True, reverse
        if reverse:
            # reverse == True -> 맨 뒤 원소 삭제
            lst.pop(-1)
        else:
            # 맨 앞 원소 삭제
            lst.pop(0)
        return False, reverse
    return False, reverse
    

if __name__ == '__main__':
    T = int(input())        # Test case #
    for _ in range(T):
        cmd = input()[:-1]      # \n 삭제
        N = input()

        lst_str = input()[1:-2]     # [, ], \n 삭제
        if lst_str == '':
            lst = []
        else:
            lst = list(map(int, lst_str.split(',')))    # 숫자 배열로 변경

        # list 뒤집으면 시간초과 -> 뒤집히는 것을 변수로
        isError = False
        reverse = False

        idx = 0
        while not isError and idx < len(cmd):
            isError, reverse = cmdPerform(cmd[idx], lst, reverse)
            idx += 1

        ### 결과 ###
        if isError:
            print("error")
        else:
            if reverse:
                lst = lst[::-1]
            print("[", end="")
            print(','.join(map(str, lst)), end="")
            print(']')