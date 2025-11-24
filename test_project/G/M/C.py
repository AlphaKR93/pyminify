S='user-agent'
R='accept-encoding'
Q=OSError
P=getattr
L=TypeError
K=bool
G=ImportError
J=bytes
I=isinstance
H=int
B=str
A=None
import io,typing as D
from base64 import b64encode as M
from enum import Enum
from..H import c
from.K import F
Ë='@@@SKIP_HEADER@@@'
Ê=frozenset([R,'host',S])
E='gzip,deflate'
try:
	try:0
	except G:pass
except G:pass
else:E+=',br'
try:0
except G:pass
else:E+=',zstd'
class C(Enum):token=0
N=C.token
È=D.Union[H,C]
U={'GET','HEAD','DELETE','TRACE','OPTIONS','CONNECT'}
def V(keep_alive:K|A=A,accept_encoding:K|list[B]|B|A=A,user_agent:B|A=A,basic_auth:B|A=A,proxy_basic_auth:B|A=A,disable_cache:K|A=A):
	H='latin-1';G=proxy_basic_auth;F=basic_auth;D=user_agent;A=accept_encoding;C={}
	if A:
		if I(A,B):0
		elif I(A,list):A=','.join(A)
		else:A=E
		C[R]=A
	if D:C[S]=D
	if keep_alive:C['connection']='keep-alive'
	if F:C['authorization']=f"Basic {M(F.encode(H)).decode()}"
	if G:C['proxy-authorization']=f"Basic {M(G.encode(H)).decode()}"
	if disable_cache:C['cache-control']='no-cache'
	return C
def É(body:D.Any,pos:È|A):
	C=body;B=pos
	if B is not A:W(C,B)
	elif P(C,'tell',A)is not A:
		try:B=C.tell()
		except Q:B=N
	return B
def W(body:D.IO[D.AnyStr],body_pos:È):
	B=body_pos;C=P(body,'seek',A)
	if C is not A and I(B,H):
		try:C(B)
		except Q as D:raise c('An error occurred when rewinding request body for redirect/retry.')from D
	elif B is N:raise c('Unable to record file position for rewinding request body during a redirect/retry.')
	else:raise ValueError(f"body_pos must be of type integer, instead it was {type(B)}.")
class O(D.NamedTuple):chunks:D.Iterable[J]|A;content_length:H|A
def Ï(body:D.Any|A,method:B,blocksize:H):
	K=blocksize;C=body
	if C is A:
		E=A
		if method.upper()not in U:G=0
		else:G=A
	elif I(C,(B,J)):E=F(C),;G=len(E[0])
	elif hasattr(C,'read'):
		def M():
			nonlocal C,K;B=I(C,io.TextIOBase)
			while True:
				A=C.read(K)
				if not A:break
				if B:A=A.encode('iso-8859-1')
				yield A
		E=M();G=A
	else:
		try:N=memoryview(C)
		except L:
			try:E=iter(C);G=A
			except L:raise L(f"'body' must be a bytes-like object, file-like object, or iterable. Instead was {C!r}")from A
		else:E=C,;G=N.nbytes
	return O(chunks=E,content_length=G)