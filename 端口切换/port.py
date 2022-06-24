#!/usr/bin/env python
import os,subprocess,socket,time,sys


def check_port(name,port1,port2):
        f=open(name,'r+',encoding='utf-8')
        f.seek(0)
        old=f.read()
        port1=str(port1,encoding='utf-8')
        port2=str(port2,encoding='utf-8')
        
        new=old.replace(str(port1),str(port2),1)
        f.seek(0)
        f.truncate()
        f.write(new)
        
        f.flush()
        f.close()


