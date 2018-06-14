#!/usr/bin/env python

'''
計算誤差の例題プログラム
桁落ち誤差の例題
'''

import math

def calc(x):
  print("x=", x)
  res1 = math.sqrt(x+1) - math.sqrt(x)
  res2 = 1 / (math.sqrt(x+1) + math.sqrt(x))
  print("通常の計算:\t", res1)
  print("有理化後の計算:\t", res2)

def main():
  calc(1e15)
  calc(1e16)

if __name__ == '__main__':
  main()