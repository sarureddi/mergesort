t1=int(input())
l11=[]
for i1 in range(t1):
	l01=list(map(int,input().split()))
	for i1 in l01:
		l11.append(i1)
l11.sort()
print(*l11)
