import sys
input = sys.stdin.readline

def  getSubset(lst, start, end):
    if start > end:
        return 0
    if start == end:
        return lst[start] ** 2
    
    mid = (start + end) // 2
    subset = max(getSubset(lst, start, mid), getSubset(lst, mid+1, end))

    left, right = mid, mid+1
    sum_ = lst[left] + lst[right]
    min_val = min(lst[left], lst[right])
    subset = max(subset, sum_ * min_val)
    while left > start or right < end:
        if right < end and (left == start or lst[left-1] < lst[right + 1]):
            right += 1
            sum_ += lst[right]
            min_val = min(min_val, lst[right])
        else:
            left -= 1
            sum_ += lst[left]
            min_val = min(min_val, lst[left])
        subset = max(subset, sum_ * min_val)
    return subset

    

if __name__ == '__main__':
    N = int(input())
    A_ = list(map(int, input().split()))

    subset = getSubset(A_, 0, len(A_)-1)
    
    print(subset)