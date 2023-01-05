import sys
data = []
for k in range(11):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length:{0:3d};Size in bytes:{1:4d}'.format(a,b))
    data.pop()


