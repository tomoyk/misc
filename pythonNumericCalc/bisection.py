#!/usr/bin/env python

'''
2分法による方程式解法のプログラム
'''

# 終了条件
LIMIT=1e-20

# ヘルパー関数
def f(x, a):
  return x**2-a

def cal(xp, xn, a):
  print("--- √", a, "---")
  print("xp=", xp, "xn=", xn)
  while (xp-xn)**2 > LIMIT:
    xmid = (xp+xn)/2
    if f(xmid, a) > 0:
      xp = xmid
    else:
      xn = xmid
    print("{:.15f} {:.15f}".format(xn, xp))

def main():
  cal(xp=1.5, xn=1.3, a=2) # √2 = 1.414...
  cal(xp=1.8, xn=1.6, a=3) # √3 = 1.732...
  cal(xp=2.3, xn=2.1, a=5) # √5 = 2.236...

if __name__ == '__main__':
  main()