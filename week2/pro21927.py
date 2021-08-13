import sys
input = sys.stdin.readline

### 크루스칼

# 생성된 트리 root 찾기
def find_root(parent, x):
    # root 아니라면 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

# 트리 합치기
def union_tree(parent, a, b):
    a = find_root(parent, a)
    b = find_root(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == '__main__':
    # 건물 개수 N, 도로 개수 M
    N, M = map(int, input().split())
    # 건물 번호 a, b , 두 건물 사이 도로 만들 때 드는 비용 c (a, b, c)-> edges에 추가
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split())))
    # cost 기준으로 정렬
    edges.sort(key=lambda x: x[-1])
    
    # parent table
    parent = [i for i in range(N)]
    result = 0

    for edge in edges:
        a, b, cost = edge
        if find_root(parent, a-1) != find_root(parent, b-1):        # 사이클 X
            # tree 합치기
            union_tree(parent, a-1, b-1)
            result += cost

    answer = sum([cost for _, _, cost in edges]) - result
    # parent가 다른 경우 -> 서로 다른 tree -> 연결되어 있지 X
    roots = list(set(parent))
    if len(roots) != 1:
        for i in range(len(roots)-1):
            if find_root(parent, roots[i]) != find_root(parent, roots[i+1]):    # 서로 다른 root -> 같은 tree에 속하지 않음
                answer = -1

    print(answer)
        