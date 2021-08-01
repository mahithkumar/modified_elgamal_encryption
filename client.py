import socket
import string
import random
import math as m
import pickle
from Modelgamal import *
cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
cs.connect((host,port))
while True:
 k = genkey()
 recv = cs.recv(10000)
 serverkey = pickle.loads(recv)
 key=pickle.dumps(k[0:3])
 cs.send(key)
 # Key exchange done
 print("\nEnter message:")
 mes = input()
 x = encrypt(mes,len(serverkey[2]),serverkey[0],serverkey[1],serverkey[2])
 encmes=pickle.dumps(x)
 cs.send(encmes)
 recv = cs.recv(10000)
 encmes = pickle.loads(recv)
 print("\nEncrypted message: ",encmes[1])
 decmes = decrypt(len(k[3]),encmes[0],k[3],k[0],encmes[1])
 print("\nDecrypted message: ",decmes)