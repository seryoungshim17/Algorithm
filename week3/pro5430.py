import sys
from collections import Counter
input = sys.stdin.readline

def cmdPerform(cmd, lst, reverse):
    # print(cmd, lst, reverse)
    if cmd == 'R':
        return False, (not reverse)
    elif cmd == 'D':
        if lst == []:
            return True, reverse
        if reverse:
            lst.pop(-1)
        else:
            lst.pop(0)
        return False, reverse
    return False, reverse
    

if __name__ == '__main__':
    T = int(input())        # Test case #
    for _ in range(T):
        cmd = input()[:-1]
        N = input()

        lst_str = input()[1:-2]
        if lst_str == '':
            lst = []
        else:
            lst = list(map(int, lst_str.split(',')))

        # D 개수 > list len => Error
        # isError = Counter(cmd)['D'] > len(lst)
        isError = False
        reverse = False

        # RR 연속 -> 삭제
        idx = 0
        while not isError and idx < len(cmd):
            isError, reverse = cmdPerform(cmd[idx], lst, reverse)
            idx += 1

        if isError:
            print("error")
        else:
            if reverse:
                lst = lst[::-1]
            print("[", end="")
            print(','.join(map(str, lst)), end="")
            print(']')