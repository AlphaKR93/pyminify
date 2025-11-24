L='password'
K='username'
J=DeprecationWarning
G='Authorization'
A=getattr
E=isinstance
B=None
import hashlib as H,os,re,threading as M,time,warnings as C
from base64 import b64encode as N
from.B import ë
from.G import ä,str,ã
from.H import D
from.Q import r
O='application/x-www-form-urlencoded'
P='multipart/form-data'
def R(username,password):
	D='latin1';B=password;A=username
	if not E(A,ä):C.warn("Non-string usernames will no longer be supported in Requests 3.0.0. Please convert the object you've passed in ({!r}) to a string or bytes object in the near future to avoid problems.".format(A),category=J);A=str(A)
	if not E(B,ä):C.warn("Non-string passwords will no longer be supported in Requests 3.0.0. Please convert the object you've passed in ({!r}) to a string or bytes object in the near future to avoid problems.".format(type(B)),category=J);B=str(B)
	if E(A,str):A=A.encode(D)
	if E(B,str):B=B.encode(D)
	F='Basic '+ë(N(b':'.join((A,B))).strip());return F
class I:
	def __call__(A,r):raise NotImplementedError('Auth hooks must be callable.')
class F(I):
	def __init__(A,username,password):A.username=username;A.password=password
	def __eq__(C,other):D=other;return all([C.username==A(D,K,B),C.password==A(D,L,B)])
	def __ne__(A,other):return not A==other
	def __call__(A,r):r.headers[G]=R(A.username,A.password);return r
class Q(F):
	def __call__(A,r):r.headers['Proxy-Authorization']=R(A.username,A.password);return r
class S(I):
	def __init__(A,username,password):A.username=username;A.password=password;A._thread_local=M.local()
	def init_per_thread_state(A):
		if not hasattr(A._thread_local,'init'):A._thread_local.init=True;A._thread_local.last_nonce='';A._thread_local.nonce_count=0;A._thread_local.chal={};A._thread_local.pos=B;A._thread_local.num_401_calls=B
	def build_digest_header(A,method,url):
		Z='auth';Y='MD5-SESS';X='MD5';G='utf-8';Q=A._thread_local.chal['realm'];D=A._thread_local.chal['nonce'];J=A._thread_local.chal.get('qop');K=A._thread_local.chal.get('algorithm');R=A._thread_local.chal.get('opaque');C=B
		if K is B:F=X
		else:F=K.upper()
		if F==X or F==Y:
			def a(x):
				if E(x,str):x=x.encode(G)
				return H.md5(x).hexdigest()
			C=a
		elif F=='SHA':
			def b(x):
				if E(x,str):x=x.encode(G)
				return H.sha1(x).hexdigest()
			C=b
		elif F=='SHA-256':
			def c(x):
				if E(x,str):x=x.encode(G)
				return H.sha256(x).hexdigest()
			C=c
		elif F=='SHA-512':
			def d(x):
				if E(x,str):x=x.encode(G)
				return H.sha512(x).hexdigest()
			C=d
		S=lambda s,d:C(f"{s}:{d}")
		if C is B:return
		T=B;N=ã(url);O=N.path or'/'
		if N.query:O+=f"?{N.query}"
		e=f"{A.username}:{Q}:{A.password}";f=f"{method}:{O}";L=C(e);U=C(f)
		if D==A._thread_local.last_nonce:A._thread_local.nonce_count+=1
		else:A._thread_local.nonce_count=1
		V=f"{A._thread_local.nonce_count:08x}";M=str(A._thread_local.nonce_count).encode(G);M+=D.encode(G);M+=time.ctime().encode(G);M+=os.urandom(8);P=H.sha1(M).hexdigest()[:16]
		if F==Y:L=C(f"{L}:{D}:{P}")
		if not J:W=S(L,f"{D}:{U}")
		elif J==Z or Z in J.split(','):g=f"{D}:{V}:{P}:auth:{U}";W=S(L,g)
		else:return
		A._thread_local.last_nonce=D;I=f'username="{A.username}", realm="{Q}", nonce="{D}", uri="{O}", response="{W}"'
		if R:I+=f', opaque="{R}"'
		if K:I+=f', algorithm="{K}"'
		if T:I+=f', digest="{T}"'
		if J:I+=f', qop="auth", nc={V}, cnonce="{P}"'
		return f"Digest {I}"
	def handle_redirect(A,r,**B):
		if r.is_redirect:A._thread_local.num_401_calls=1
	def handle_401(A,r,**H):
		if not 400<=r.status_code<500:A._thread_local.num_401_calls=1;return r
		if A._thread_local.pos is not B:r.request.body.seek(A._thread_local.pos)
		F=r.headers.get('www-authenticate','')
		if'digest'in F.lower()and A._thread_local.num_401_calls<2:A._thread_local.num_401_calls+=1;I=re.compile('digest ',flags=re.IGNORECASE);A._thread_local.chal=r(I.sub('',F,count=1));r.close();C=r.request.copy();D(C._cookies,r.request,r.raw);C.prepare_cookies(C._cookies);C.headers[G]=A.build_digest_header(C.method,C.url);E=r.connection.send(C,**H);E.history.append(r);E.request=C;return E
		A._thread_local.num_401_calls=1;return r
	def __call__(A,r):
		C='response';A.init_per_thread_state()
		if A._thread_local.last_nonce:r.headers[G]=A.build_digest_header(r.method,r.url)
		try:A._thread_local.pos=r.body.tell()
		except AttributeError:A._thread_local.pos=B
		r.register_hook(C,A.handle_401);r.register_hook(C,A.handle_redirect);A._thread_local.num_401_calls=1;return r
	def __eq__(C,other):D=other;return all([C.username==A(D,K,B),C.password==A(D,L,B)])
	def __ne__(A,other):return not A==other