Å='replace'
Ä='cannot encode objects that are not 2-tuples'
Ã=DeprecationWarning
Â=ImportError
j='all'
i='no_proxy'
h=TypeError
g=AttributeError
W='='
V='"'
U=';'
R=len
P='/'
O=hasattr
N=int
K=isinstance
J=ValueError
I=OSError
G=''
E=False
D=True
A=None
import codecs as M,contextlib as k,io,os as B,re as F,socket as H,struct as T,sys,tempfile as l,warnings as X,zipfile as m
from collections import OrderedDict as Æ
from G.M import make_headers as Ç,parse_url as È
from.import certs
from.A import __version__
from.B import í,ì
from.G import Mapping,ä,bytes,getproxies,è,ê
from.G import æ
from.G import ç,é,quote,str,unquote,ã,å
from.H import C
from.I import á,à,ß,â
from.P import Þ
É='.netrc','_netrc'
n=certs.where()
o={'http':80,'https':443}
Ê=', '.join(F.split(',\\s*',Ç(accept_encoding=D)['accept-encoding']))
if sys.platform=='win32':
	def Ë(host):
		G='.'
		try:import winreg as B
		except Â:return E
		try:H=B.OpenKey(B.HKEY_CURRENT_USER,'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings');K=N(B.QueryValueEx(H,'ProxyEnable')[0]);C=B.QueryValueEx(H,'ProxyOverride')[0]
		except(I,J):return E
		if not K or not C:return E
		C=C.split(U)
		for A in C:
			if A=='<local>':
				if G not in host:return D
			A=A.replace(G,'\\.');A=A.replace('*','.*');A=A.replace('?',G)
			if F.match(A,host,F.I):return D
		return E
	def ç(host):
		if è():return é(host)
		else:return Ë(host)
def Ö(d):
	if O(d,'items'):d=d.items()
	return d
def Y(o):
	C=A;D=0
	if O(o,'__len__'):C=R(o)
	elif O(o,'len'):C=o.len
	elif O(o,'fileno'):
		try:E=o.fileno()
		except(io.UnsupportedOperation,g):pass
		else:
			C=B.fstat(E).st_size
			if'b'not in o.mode:X.warn("Requests has determined the content-length for this request using the binary size of the file: however, the file has been opened in text mode (i.e. without the 'b' flag in the mode). This may lead to an incorrect content-length. In Requests 3.0, support will be removed for files in text mode.",á)
	if O(o,'tell'):
		try:D=o.tell()
		except I:
			if C is not A:D=C
		else:
			if O(o,'seek')and C is A:
				try:o.seek(0,2);C=o.tell();o.seek(D or 0)
				except I:C=0
	if C is A:C=0
	return max(0,C-D)
def Z(url,raise_errors=E):
	E=B.environ.get('NETRC')
	if E is not A:F=E,
	else:F=(f"~/{A}"for A in É)
	try:
		from netrc import NetrcParseError as H,netrc;D=A
		for J in F:
			try:G=B.path.expanduser(J)
			except KeyError:return
			if B.path.exists(G):D=G;break
		if D is A:return
		K=ã(url);L=K.hostname
		try:
			C=netrc(D).authenticators(L)
			if C:M=0 if C[0]else 1;return C[M],C[2]
		except(H,I):
			if raise_errors:raise
	except(Â,g):pass
def p(obj):
	C=getattr(obj,'name',A)
	if C and K(C,ä)and C[0]!='<'and C[-1]!='>':return B.path.basename(C)
def q(path):
	C=path
	if B.path.exists(C):return C
	A,D=B.path.split(C)
	while A and not B.path.exists(A):
		A,F=B.path.split(A)
		if not F:break
		D=P.join([F,D])
	if not m.is_zipfile(A):return C
	G=m.ZipFile(A)
	if D not in G.namelist():return C
	H=l.gettempdir();E=B.path.join(H,D.split(P)[-1])
	if not B.path.exists(E):
		with Ì(E)as I:I.write(G.read(D))
	return E
@k.contextmanager
def Ì(filename):
	A=filename;D,C=l.mkstemp(dir=B.path.dirname(A))
	try:
		with B.fdopen(D,'wb')as E:yield E
		B.replace(C,A)
	except BaseException:B.remove(C);raise
def Ø(value):
	B=value
	if B is A:return
	if K(B,(str,bytes,bool,N)):raise J(Ä)
	return Æ(B)
def L(value):
	B=value
	if B is A:return
	if K(B,(str,bytes,bool,N)):raise J(Ä)
	if K(B,Mapping):B=B.items()
	return list(B)
def Ù(value):
	B=[]
	for A in æ(value):
		if A[:1]==A[-1:]==V:A=s(A[1:-1])
		B.append(A)
	return B
def r(value):
	B=value;C={}
	for D in æ(B):
		if W not in D:C[D]=A;continue
		E,B=D.split(W,1)
		if B[:1]==B[-1:]==V:B=s(B[1:-1])
		C[E]=B
	return C
def s(value,is_filename=E):
	B='\\\\';A=value
	if A and A[0]==A[-1]==V:
		A=A[1:-1]
		if not is_filename or A[:2]!=B:return A.replace(B,'\\').replace('\\"',V)
	return A
def Ú(cj):
	A={}
	for B in cj:A[B.name]=B.value
	return A
def Û(cj,cookie_dict):return C(cookie_dict,cj)
def Ü(content):A=content;X.warn('In requests 3.0, get_encodings_from_content will be removed. For more information, please see the discussion on issue #2266. (This warning should only appear once.)',Ã);B=F.compile('<meta.*?charset=["\\\']*(.+?)["\\\'>]',flags=F.I);C=F.compile('<meta.*?content=["\\\']*;?charset=(.+?)["\\\'>]',flags=F.I);D=F.compile('^<\\?xml.*?encoding=["\\\']*(.+?)["\\\'>]');return B.findall(A)+C.findall(A)+D.findall(A)
def Í(header):
	C=header.split(U);I,J=C[0].strip(),C[1:];E={};F='"\' '
	for A in J:
		A=A.strip()
		if A:
			G,H=A,D;B=A.find(W)
			if B!=-1:G=A[:B].strip(F);H=A[B+1:].strip(F)
			E[G.lower()]=H
	return I,E
def a(headers):
	C='charset';A=headers.get('content-type')
	if not A:return
	A,B=Í(A)
	if C in B:return B[C].strip('\'"')
	if'text'in A:return'ISO-8859-1'
	if'application/json'in A:return'utf-8'
def t(iterator,r):
	C=iterator
	if r.encoding is A:yield from C;return
	E=M.getincrementaldecoder(r.encoding)(errors=Å)
	for F in C:
		B=E.decode(F)
		if B:yield B
	B=E.decode(b'',final=D)
	if B:yield B
def u(string,slice_length):
	D=string;B=slice_length;C=0
	if B is A or B<=0:B=R(D)
	while C<R(D):yield D[C:C+B];C+=B
def Ý(r):
	X.warn('In requests 3.0, get_unicode_from_response will be removed. For more information, please see the discussion on issue #2266. (This warning should only appear once.)',Ã);B=[];A=a(r.headers)
	if A:
		try:return str(r.content,A)
		except UnicodeError:B.append(A)
	try:return str(r.content,A,errors=Å)
	except h:return r.content
Î=frozenset('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'+'0123456789-._~')
def Ï(uri):
	A=uri.split('%')
	for B in range(1,R(A)):
		C=A[B][0:2]
		if R(C)==2 and C.isalnum():
			try:D=chr(N(C,16))
			except J:raise ß(f"Invalid percent-escape sequence: '{C}'")
			if D in Î:A[B]=D+A[B][2:]
			else:A[B]=f"%{A[B]}"
		else:A[B]=f"%{A[B]}"
	return G.join(A)
def S(uri):
	A="!#$%&'()*+,/:;=?@[]~";B="!#$&'()*+,/:;=?@[]~"
	try:return quote(Ï(uri),safe=A)
	except ß:return quote(uri,safe=B)
def Ð(ip,net):B='=L';C=T.unpack(B,H.inet_aton(ip))[0];D,E=net.split(P);A=T.unpack(B,H.inet_aton(Ñ(N(E))))[0];F=T.unpack(B,H.inet_aton(D))[0]&A;return C&A==F&A
def Ñ(mask):A=4294967295^(1<<32-mask)-1;return H.inet_ntoa(T.pack('>I',A))
def Ò(string_ip):
	try:H.inet_aton(string_ip)
	except I:return E
	return D
def Ó(string_network):
	A=string_network
	if A.count(P)==1:
		try:B=N(A.split(P)[1])
		except J:return E
		if B<1 or B>32:return E
		try:H.inet_aton(A.split(P)[0])
		except I:return E
	else:return E
	return D
@k.contextmanager
def Ô(env_name,value):
	D=value;C=env_name;E=D is not A
	if E:F=B.environ.get(C);B.environ[C]=D
	try:yield
	finally:
		if E:
			if F is A:del B.environ[C]
			else:B.environ[C]=F
def b(url,no_proxy):
	F=no_proxy
	def M(key):return B.environ.get(key)or B.environ.get(key.upper())
	N=F
	if F is A:F=M(i)
	C=ã(url)
	if C.hostname is A:return D
	if F:
		F=(A for A in F.replace(' ',G).split(',')if A)
		if Ò(C.hostname):
			for I in F:
				if Ó(I):
					if Ð(C.hostname,I):return D
				elif C.hostname==I:return D
		else:
			J=C.hostname
			if C.port:J+=f":{C.port}"
			for K in F:
				if C.hostname.endswith(K)or J.endswith(K):return D
	with Ô(i,N):
		try:L=ç(C.hostname)
		except(h,H.gaierror):L=E
	if L:return D
	return E
def c(url,no_proxy=A):
	if b(url,no_proxy=no_proxy):return{}
	else:return getproxies()
def d(url,proxies):
	B=proxies;B=B or{};C=ã(url)
	if C.hostname is A:return B.get(C.scheme,B.get(j))
	F=[C.scheme+'://'+C.hostname,C.scheme,'all://'+C.hostname,j];D=A
	for E in F:
		if E in B:D=B[E];break
	return D
def e(request,proxies,trust_env=D):
	B=proxies;B=B if B is not A else{};C=request.url;D=ã(C).scheme;E=B.get(i);F=B.copy()
	if trust_env and not b(C,no_proxy=E):
		G=c(C,no_proxy=E);H=G.get(D,G.get(j))
		if H:F.setdefault(D,H)
	return F
def Õ(name='python-requests'):return f"{name}/{__version__}"
def v():return Þ({'User-Agent':Õ(),'Accept-Encoding':Ê,'Accept':'*/*','Connection':'keep-alive'})
def w(value):
	A=value;B=[];C=' \'"';A=A.strip(C)
	if not A:return B
	for D in F.split(', *<',A):
		try:E,H=D.split(U,1)
		except J:E,H=D,G
		I={'url':E.strip('<> \'"')}
		for K in H.split(U):
			try:L,A=K.split(W)
			except J:break
			I[L.strip(C)]=A.strip(C)
		B.append(I)
	return B
f='\x00'.encode('ascii')
x=f*2
y=f*3
def z(data):
	A=data[:4]
	if A in(M.BOM_UTF32_LE,M.BOM_UTF32_BE):return'utf-32'
	if A[:3]==M.BOM_UTF8:return'utf-8-sig'
	if A[:2]in(M.BOM_UTF16_LE,M.BOM_UTF16_BE):return'utf-16'
	B=A.count(f)
	if B==0:return'utf-8'
	if B==2:
		if A[::2]==x:return'utf-16-be'
		if A[1::2]==x:return'utf-16-le'
	if B==3:
		if A[:3]==y:return'utf-32-be'
		if A[1:]==y:return'utf-32-le'
def ª(url,new_scheme):
	E=È(url);D,F,J,K,C,H,I=E;B=E.netloc
	if not B:B,C=C,B
	if F:B='@'.join([F,B])
	if D is A:D=new_scheme
	if C is A:C=G
	return å((D,B,C,G,H,I))
def Q(url):
	A=ã(url)
	try:B=unquote(A.username),unquote(A.password)
	except(g,h):B=G,G
	return B
def µ(header):A=header;B,C=A;º(A,B,0);º(A,C,1)
def º(header,header_part,header_validator_index):
	B=header_validator_index;A=header_part
	if K(A,str):C=ì[B]
	elif K(A,bytes):C=í[B]
	else:raise à(f"Header part ({A!r}) from {header} must be of type str or bytes, not {type(A)}")
	if not C.match(A):D='name'if B==0 else'value';raise à(f"Invalid leading whitespace, reserved character(s), or returncharacter(s) in header {D}: {A!r}")
def À(url):
	C,A,B,D,E,F=ã(url)
	if not A:A,B=B,A
	A=A.rsplit('@',1)[-1];return å((C,A,B,D,E,G))
def Á(prepared_request):
	B=prepared_request;C=getattr(B.body,'seek',A)
	if C is not A and K(B._body_position,ê):
		try:C(B._body_position)
		except I:raise â('An error occurred when rewinding request body for redirect.')
	else:raise â('Unable to rewind request body for redirect.')