#!/usr/bin/env python

import urllib.request, urllib.parse

data = {
        'name': 'john doe',
        'age' : '22'
}
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request('http://yahoo.co.jp/')
req.add_header('Referer', 'http://google.com/')

with urllib.request.urlopen(req, data) as res:
    html = res.read().decode('utf-8')
    print(html)
