#!/usr/bin/env python
import http.server as web

bindAddress = ("127.0.0.1", 3000)
requestHandler = web.BaseHTTPRequestHandler(request, client_address, server)

httpd = web.HTTPServer(bindAddress, requestHandler)
httpd.serve_forever()
