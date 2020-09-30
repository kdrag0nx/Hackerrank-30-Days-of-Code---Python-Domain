'''
Author : Amit Kumar
Python Version: 3 and above

'''

A = []
for i in range(6):
    t = [int(temp) for temp in input().strip().split(' ')]
    A.append(t)

smax = -9 * 7

for r in range(len(A) - 2):
    for c in range(len(A[row]) - 2):
        tl = A[r][c]
        tc = A[r][c + 1]
        tr = A[r][c + 2]
        mc = A[r + 1][c + 1]
        bl = A[r + 2][c]
        bc = A[r + 2][c + 1]
        br = A[r + 2][c + 2]
        s = tl + tc + tr + mc + bl + bc + br
        smax = max(s, smax)
        '''
        or if smax>s:
           print smax you can solve either way "Hindi: dono chalega"
           '''

print(smax)
