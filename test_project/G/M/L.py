J='must specify at least one of read=True, write=True'
I=RuntimeError
H=True
F=float
C=False
B=None
A=bool
import select as D,socket as G
from functools import partial as K
def L(sock:G.socket,read:A=C,write:A=C,timeout:F|B=B):
	C=write
	if not read and not C:raise I(J)
	E=[];B=[]
	if read:E.append(sock)
	if C:B.append(sock)
	F=K(D.select,E,B,B);G,H,L=F(timeout);return A(G or H or L)
def M(sock:G.socket,read:A=C,write:A=C,timeout:F|B=B):
	E=write
	if not read and not E:raise I(J)
	C=0
	if read:C|=D.POLLIN
	if E:C|=D.POLLOUT
	G=D.poll();G.register(sock,C)
	def H(t:F|B):
		if t is not B:t*=1000
		return G.poll(t)
	return A(H(timeout))
def N():
	try:A=D.poll();A.poll(0)
	except(AttributeError,OSError):return C
	else:return H
def E(sock:G.socket,read:A=C,write:A=C,timeout:F|B=B):
	global E
	if N():E=M
	elif hasattr(D,'select'):E=L
	return E(sock,read,write,timeout)
def Ñ(sock:G.socket,timeout:F|B=B):return E(sock,read=H,timeout=timeout)
def O(sock:G.socket,timeout:F|B=B):return E(sock,write=H,timeout=timeout)