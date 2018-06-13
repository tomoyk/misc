#!/usr/bin/env python

import sqlite3
import datetime as dt

con = sqlite3.connect('hoge.db')
cur = con.cursor()
START = dt.date(2018, 4, 13)
ADDITION_DAY = 2

for prefix in range(0, 40/ADDITION_DAY):
	base = START + dt.timedelta(days=ADDITION_DAY * prefix)
	next_day = base + dt.timedelta(days=ADDITION_DAY)
	dates=[str(base), str(next_day)]

	rows = cur.execute('SELECT firstdate from team WHERE ? < firstdate AND firstdate < ?', dates)

	print str(base), '-', str(next_day - dt.timedelta(days=1)), '\t', len(list(rows))
