#!/usr/bin/env python
import http.server as web 
import socketserver

def run(handler_class=web.BaseHTTPRequestHandler):
  bindAddr = ("0.0.0.0", 3000)
  req = web.BaseHTTPRequestHandler;
  httpd = web.HTTPServer(bindAddr, req)
  print("=====")
  print("IP-Address: "+str(bindAddr[0]))
  print("Port: "+str(bindAddr[1]))
  print("=====")
  httpd.serve_forever()

def run2():
  PORT = 3000
  HOST = "0.0.0.0"
  Handler = web.SimpleHTTPRequestHandler

  with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

run2()

