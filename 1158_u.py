# from collections import deque
# N, K = map(int, input().split())

# josep = deque([i for i in range(1, N+1)])

n = int(input())
cards = [int(i) for i in input().split()]
dict1 = {}
for i in cards:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
m = int(input())
find = [int(i) for i in input().split()]

for i in find:
    print(dict1.get(i, 0), end=' ')

