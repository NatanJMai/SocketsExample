#!/usr/bin/python3

import socket, hashlib
from threading           import Thread
from cryptography.fernet import Fernet

def abort(msg):
   print(msg)
   exit()

def read(line):
   spl = line.split(',')
   return float(spl[-2]) * float(spl[-1]) if len(spl) >= 3 else 0.0

def hash(line):
   m = hashlib.md5()
   m.update(line.encode())
   return m.digest()

def crypt(line):
   key = Fernet.generate_key()
      
   print("Key -> %s" % key)

   f   = Fernet(key)

   token = f.encrypt(line)
   print(token)
   