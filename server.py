import socket
import string
import random
import math as m
import pickle
from Modelgamal import *
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
ss.bind((host,port))
ss.listen(1)
c,addr = ss.accept()
while True:
 k = genkey()
 key=pickle.dumps(k[0:3])
 c.send(key)
 recv = c.recv(10000)
 clientkey = pickle.loads(recv)
 recv = c.recv(10000)
 encmes = pickle.loads(recv)
 print("\nEncrypted message: ",encmes[1])
 decmes = decrypt(len(k[2]),encmes[0],k[3],k[0],encmes[1])
 print("\nDecrypted message: ",decmes)
 print("\nEnter message:")
 mes = input()
 x = encrypt(mes,len(clientkey[2]),clientkey[0],clientkey[1],clientkey[2])
 encmes=pickle.dumps(x)
 c.send(encmes)