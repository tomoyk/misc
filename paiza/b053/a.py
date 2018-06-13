#!/usr/bin/env python

H,W = [int(i) for i in input().split()]
a = [ [int(i) for i in input().split()] for _ in range(2) ]
diff_x = a[0][1] - a[0][0]
diff_y = a[1][0] - a[0][0]
ans=[]
# print(a)
# print(diff_x, diff_y)

# 最初の2行だけ片付ける
for y in range(2):
    tmp=[a[y][0], a[y][1]]
    start = a[y][1]
    diff_x = a[y][1] - a[y][0]
    for x in range(1, W-1):
        # print(x, diff_x)
        tmp.append( start + x*diff_x )
    ans.append(tmp)

# print(ans)

# 2行より後ろを片付ける
for y in range(2, H):
    tmp = []
    for x in range(0, W):
        diff_y = ans[y-1][x] - ans[y-2][x]
        tmp.append( ans[y-1][x] + diff_y )
    ans.append(tmp)
        
for i in ans:
    print( ' '.join( str(c) for c in i ) )
