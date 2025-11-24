b='ascii'
a='(?:'
R='@'
K='?'
J='$'
I='^'
N=int
L=''
H=property
G='/'
B=None
A=str
import re as E,typing as C
from..H import D
from.K import Ã
T='http','https',B
c=E.compile('%[a-fA-F0-9]{2}')
d=E.compile('^(?:[a-zA-Z][a-zA-Z0-9+-]*:|/)')
e=E.compile('^(?:([a-zA-Z][a-zA-Z0-9+.-]*):)?(?://([^\\\\/?#]*))?([^?#]*)(?:\\?([^#]*))?(?:#(.*))?$',E.UNICODE|E.DOTALL)
M='(?:[0-9]{1,3}\\.){3}[0-9]{1,3}'
S='[0-9A-Fa-f]{1,4}'
f='(?:{hex}:{hex}|{ipv4})'.format(hex=S,ipv4=M)
g={'hex':S,'ls32':f}
h=['(?:%(hex)s:){6}%(ls32)s','::(?:%(hex)s:){5}%(ls32)s','(?:%(hex)s)?::(?:%(hex)s:){4}%(ls32)s','(?:(?:%(hex)s:)?%(hex)s)?::(?:%(hex)s:){3}%(ls32)s','(?:(?:%(hex)s:){0,2}%(hex)s)?::(?:%(hex)s:){2}%(ls32)s','(?:(?:%(hex)s:){0,3}%(hex)s)?::%(hex)s:%(ls32)s','(?:(?:%(hex)s:){0,4}%(hex)s)?::%(ls32)s','(?:(?:%(hex)s:){0,5}%(hex)s)?::%(hex)s','(?:(?:%(hex)s:){0,6}%(hex)s)?::']
i='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._\\-~'
U=a+'|'.join([A%g for A in h])+')'
V='(?:%25|%)(?:['+i+']|%[a-fA-F0-9]{2})+'
O='\\['+U+a+V+')?\\]'
j='(?:[^\\[\\]%:/?#]|%[a-fA-F0-9]{2})*'
k=E.compile('^(/[^?#]*)(?:\\?([^#]*))?(?:#.*)?$')
P=E.compile(I+M+J)
t=E.compile(I+U+J)
l=E.compile(I+O+J)
W=E.compile(I+O[2:-2]+J)
m=E.compile('('+V+')\\]$')
n='^(%s|%s|%s)(?::0*?(|0|[1-9][0-9]{0,4}))?$'%(j,M,O)
o=E.compile(n,E.UNICODE|E.DOTALL)
X=set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-~')
p=set("!$&'()*+,;=")
Y=X|p|{':'}
Q=Y|{R,G}
Z=q=Q|{K}
class Url(C.NamedTuple('Url',[('scheme',C.Optional[A]),('auth',C.Optional[A]),('host',C.Optional[A]),('port',C.Optional[N]),('path',C.Optional[A]),('query',C.Optional[A]),('fragment',C.Optional[A])])):
	def __new__(D,scheme:A|B=B,auth:A|B=B,host:A|B=B,port:N|B=B,path:A|B=B,query:A|B=B,fragment:A|B=B):
		C=scheme;A=path
		if A and not A.startswith(G):A=G+A
		if C is not B:C=C.lower()
		return super().__new__(D,C,auth,host,port,A,query,fragment)
	@H
	def hostname(self):return self.host
	@H
	def request_uri(self):
		A=self;C=A.path or G
		if A.query is not B:C+=K+A.query
		return C
	@H
	def authority(self):
		C=self.auth;A=self.netloc
		if A is B or C is B:return A
		else:return f"{C}@{A}"
	@H
	def netloc(self):
		A=self
		if A.host is B:return
		if A.port:return f"{A.host}:{A.port}"
		return A.host
	@H
	def url(self):
		D,E,F,G,H,I,J=self;C=L
		if D is not B:C+=D+'://'
		if E is not B:C+=E+R
		if F is not B:C+=F
		if G is not B:C+=':'+A(G)
		if H is not B:C+=H
		if I is not B:C+=K+I
		if J is not B:C+='#'+J
		return C
	def __str__(A):return A.url
@C.overload
def F(component:A,allowed_chars:C.Container[A]):0
@C.overload
def F(component,allowed_chars:C.Container[A]):0
def F(component:A|B,allowed_chars:C.Container[A]):
	F=b'%';A=component
	if A is B:return A
	A=Ã(A);A,I=c.subn(lambda match:match.group(0).upper(),A);D=A.encode('utf-8','surrogatepass');J=I==D.count(F);E=bytearray()
	for G in range(0,len(D)):
		C=D[G:G+1];H=ord(C)
		if J and C==F or H<128 and C.decode()in allowed_chars:E+=C;continue
		E.extend(F+hex(H)[2:].encode().zfill(2).upper())
	return E.decode()
def r(path:A):
	B=path;D=B.split(G);A=[]
	for C in D:
		if C=='.':continue
		if C!='..':A.append(C)
		elif A:A.pop()
	if B.startswith(G)and(not A or A[0]):A.insert(0,L)
	if B.endswith(('/.','/..')):A.append(L)
	return G.join(A)
@C.overload
def Å(host,scheme:A|B):0
@C.overload
def Å(host:A,scheme:A|B):0
def Å(host:A|B,scheme:A|B):
	G='%25';A=host
	if A:
		if scheme in T:
			H=l.match(A)
			if H:
				C=m.search(A)
				if C:
					D,E=C.span(1);B=A[D:E]
					if B.startswith(G)and B!=G:B=B[3:]
					else:B=B[1:]
					B=F(B,X);return f"{A[:D].lower()}%{B}{A[E:]}"
				else:return A.lower()
			elif not P.match(A):return Ã(b'.'.join([s(A)for A in A.split('.')]),b)
	return A
def s(name:A):
	A=name
	if not A.isascii():
		try:import idna as C
		except ImportError:raise D("Unable to parse URL without the 'idna' module")from B
		try:return C.encode(A.lower(),strict=True,std3_rules=True)
		except C.IDNAError:raise D(f"Name '{A}' is not a valid IDNA label")from B
	return A.lower().encode(b)
def Æ(target:A):
	C=target;E=k.match(C)
	if not E:raise D(f"{C!r} is not a valid request URI")
	H,A=E.groups();G=F(H,Q)
	if A is not B:A=F(A,Z);G+=K+A
	return G
def Ä(url:A):
	H=url
	if not H:return Url()
	U=H
	if not d.search(H):H='//'+H
	try:
		E,S,C,J,K=e.match(H).groups();P=E is B or E.lower()in T
		if E:E=E.lower()
		if S:
			G,X,V=S.rpartition(R);G=G or B;M,I=o.match(V).groups()
			if G and P:G=F(G,Y)
			if I==L:I=B
		else:G,M,I=B,B,B
		if I is not B:
			O=N(I)
			if not 0<=O<=65535:raise D(H)
		else:O=B
		M=Å(M,E)
		if P and C:C=r(C);C=F(C,Q)
		if P and J:J=F(J,Z)
		if P and K:K=F(K,q)
	except(ValueError,AttributeError)as W:raise D(U)from W
	if not C:
		if J is not B or K is not B:C=L
		else:C=B
	return Url(scheme=E,auth=G,host=M,port=O,path=C,query=J,fragment=K)