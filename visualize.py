#!/usr/bin/env python

from matplotlib import pyplot as plt

years = [1991,1993,1994,1997,1999,2000]
gdp = [200,240.3,314,284.2,221,302]

plt.plot(years, gdp, color="green", marker="o", linestyle="solid")
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.show()
