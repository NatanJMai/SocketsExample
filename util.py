#!/usr/bin/python3

from threading import Thread
import socket

def abort(msg):
   print(msg)
   exit()

def read(line):
   spl = line.split()
   return float(spl[-2]) * float(spl[-1]) if len(spl) >= 3 else 0.0

def crypt(line):
   pass
   