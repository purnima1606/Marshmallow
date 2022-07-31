

n = int(input())
eng = set(map(int,input().split()))
b = int(input())
fren = set(map(int, input().split()))
res = eng.union(fren)
print(len(res))
