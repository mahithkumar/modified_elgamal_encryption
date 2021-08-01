import math,random
import string
primel=[]
for i in range(11,255):
 f=1
 for j in range(2,int(math.sqrt(i))+1):
   if i%j == 0:
    f=0
    break
 if f:
  primel.append(i)
def primitive_root(p):
 if p == 2:
   return 1
 p1 = 2
 p2 = (p-1) // p1
 while(1):
   g = random.randint( 2, (p-1) )
   if not (pow( g, (p-1)//p1, p ) == 1):
     if not pow( g, (p-1)//p2, p ) == 1:
       return g
def genkey():
 p=primel[random.randint(0,len(primel)-1)]
 g = primitive_root(p)
 n = random.randint(4,9)
 b=[]
 B=[]
 while len(b)!=n:
  x = random.randint(2,p-2)
  if x not in b:
     b.append(x)
 for i in range(n):
    B.append(pow(g,b[i],p))
 return [p,g,B,b]
def encrypt(z,n,p,g,B):
 a=[]
 while len(a)!=n:
    x=random.randint(2,p-2)
    if x not in a:
     a.append(x)
 c=1
 A=[]
 for i in range(n):
    sec = pow(B[i],a[i],p)
    A.append( pow(g,a[i],p))
    c*=sec
 c%=p
 if(c==1):
  c=5
 mes=random.choices(string.ascii_letters + string.digits, k = c)
 for i in z:
   mes.append(i)
 mes+=random.choices(string.ascii_letters + string.digits, k = c//2)
 for i in range(0,len(mes)):
  w=(c*ord(mes[i]))
  mes[i]=chr(w)
 return [A,''.join(mes)]
def decrypt(n,A,b,p,l):
 s=[];l2=[]
 for i in range(n):
   l2.append(pow(A[i],b[i],p))
 c=1
 for i in l2:
   c*=i
 c%=p
 if(c==1):
   c=5
 s=""
 ll = len(l)-c//2
 for i in range(c,ll):
    w=(ord(l[i])//c)
    s+=chr(w)
 return s

 
