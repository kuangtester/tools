#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: areful
 
'a socket example which send echo message to server.'
 
import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.179', 8000))
print(s.recv(1024))
for data in ['Michael', 'Tracy', 'Sarah']:
    s.send(bytes(data, encoding='utf-8'))
    print(s.recv(1024))
s.send(bytes('exit', encoding='utf-8'))
s.close()
