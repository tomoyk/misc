# Pythonによる数値計算とシミュレーター

## 1.2 数値計算と誤差

|項目|説明|
|---|---|
|型落ち|値のほぼ等しい数値同士を演算するなどして、有効数字が失われることによって生じる誤差|
|丸め誤差|有限桁数の2進数で実数を表現することにより生じる誤差|
|情報落ち|絶対値の大きく異なる数値同士の演算において、絶対値の小さな数値が演算結果に反映されないために生じる誤差|


### 桁落ち

xの値が大きいと桁落ちが生じる。これを避けるには分子の有理化を行う。

<img src="https://latex.codecogs.com/gif.latex?\sqrt{x+1}-\sqrt{x}" />

<img src="https://latex.codecogs.com/gif.latex?=(\sqrt{x+1}-\sqrt{x})\frac{\sqrt{x+1}+\sqrt{x}}{\sqrt{x+1}+\sqrt{x}}" />

<img src="https://latex.codecogs.com/gif.latex?=\frac{1}{\sqrt{x+1}+\sqrt{x}}" />

### 