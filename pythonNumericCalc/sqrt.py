#!/usr/bin/env python

'''
sqrtモジュールで平方根を求める
'''

import math

def calc(N):
  x = float(N)
  print("--- √", N, "---")
  print(math.sqrt(x))

def main():
  calc(2)
  calc(3)
  calc(5)

if __name__ == '__main__':
  main()