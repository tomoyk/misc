#!/usr/bin/env python

import urllib.request, urllib.parse

params = {
    'name'   : 'John Doe',
    'age'    : 22,
    'message': 'hello world'
}

encoded_params = urllib.parse.urlencode(params)
req = urllib.request.Request('http://yahoo.co.jp/?' + encoded_params)
req.add_header('Referer', 'http://google.co.jp/')

with urllib.request.urlopen(req) as res:
    html = res.read().decode('utf-8')
    print(html)

# MEMO::
# https://www.yoheim.net/blog.php?q=20160204
