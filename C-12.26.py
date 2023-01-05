a = [0,0,0,0,0,1,1,1,1,1,1,1,2,3,4,5,6,6]
x = len(a)
print(x)
i = 0
count = 0
for i in range(x-1):
    print(a[i])
    print(a[i])
    if a[i] == a[i+1]:
        count+= 1
    i+= 1
print(x)
print(count)



res = []
[res.append(y) for x in a if x not in res]
print(res)
