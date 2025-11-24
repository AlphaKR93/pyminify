Ì='location'
Ë='encoding'
Ê=UnicodeDecodeError
É=UnicodeError
Å='read'
Ä=setattr
Ã=getattr
Â=TypeError
Á=tuple
À=staticmethod
ª='Content-Length'
v=len
o='__iter__'
l=''
k=ValueError
j='utf-8'
i=False
h=bytes
g=True
f=hasattr
e=property
d=str
c=isinstance
b=None
import datetime as Í
from io import UnsupportedOperation as Î
from G.H import O,D,I,J,B
from G.I import E
from G.J import R
from G.M import parse_url as Ï
from.B import ë,Z
from.E import F
from.G import V,P,Mapping,ä,U,W,r
from.G import T
from.G import urlencode,urlsplit,å
from.H import a,C,X
from.I import n,ConnectionError,q,K,G,ß
from.I import H
from.I import M
from.I import m
from.I import N
from.K import s
from.O import A
from.P import Þ
from.Q import µ,Q,p,z,u,w,S,t,Y,L
Æ=A.moved,A.found,A.other,A.temporary_redirect,A.permanent_redirect
Ç=30
Ð=10*1024
Ñ=512
class Ò:
	@e
	def path_url(self):
		A=[];C=urlsplit(self.url);B=C.path
		if not B:B='/'
		A.append(B);D=C.query
		if D:A.append('?');A.append(D)
		return l.join(A)
	@À
	def _encode_params(data):
		A=data
		if c(A,(d,h)):return A
		elif f(A,Å):return A
		elif f(A,o):
			E=[]
			for(D,B)in L(A):
				if c(B,ä)or not f(B,o):B=[B]
				for C in B:
					if C is not b:E.append((D.encode(j)if c(D,d)else D,C.encode(j)if c(C,d)else C))
			return urlencode(E,doseq=g)
		else:return A
	@À
	def _encode_files(files,data):
		D=files
		if not D:raise k('Files must be provided.')
		elif c(data,ä):raise k('Data must not be a string.')
		G=[];O=L(data or{});D=L(D or{})
		for(H,C)in O:
			if c(C,ä)or not f(C,o):C=[C]
			for A in C:
				if A is not b:
					if not c(A,h):A=d(A)
					G.append((H.decode(j)if c(H,h)else H,A.encode(j)if c(A,d)else A))
		for(K,A)in D:
			I=b;M=b
			if c(A,(Á,list)):
				if v(A)==2:F,B=A
				elif v(A)==3:F,B,I=A
				else:F,B,I,M=A
			else:F=p(A)or K;B=A
			if c(B,(d,h,bytearray)):J=B
			elif f(B,Å):J=B.read()
			elif B is b:continue
			else:J=B
			N=E(name=K,data=J,filename=F,headers=M);N.make_multipart(content_type=I);G.append(N)
		P,Q=R(G);return P,Q
class È:
	def register_hook(C,event,hook):
		B=hook;A=event
		if A not in C.hooks:raise k(f'Unsupported event specified, with event name "{A}"')
		if c(B,V):C.hooks[A].append(B)
		elif f(B,o):C.hooks[A].extend(A for A in B if c(A,V))
	def deregister_hook(A,event,hook):
		try:A.hooks[event].remove(hook);return g
		except k:return i
class y(È):
	def __init__(A,method=b,url=b,headers=b,files=b,data=b,params=b,auth=b,cookies=b,hooks=b,json=b):
		F=hooks;E=params;D=data;C=files;B=headers;D=[]if D is b else D;C=[]if C is b else C;B={}if B is b else B;E={}if E is b else E;F={}if F is b else F;A.hooks=s()
		for(G,H)in list(F.items()):A.register_hook(event=G,hook=H)
		A.method=method;A.url=url;A.headers=B;A.files=C;A.data=D;A.json=json;A.params=E;A.auth=auth;A.cookies=cookies
	def __repr__(A):return f"<Request [{A.method}]>"
	def prepare(A):B=x();B.prepare(method=A.method,url=A.url,headers=A.headers,files=A.files,data=A.data,json=A.json,params=A.params,auth=A.auth,cookies=A.cookies,hooks=A.hooks);return B
class x(Ò,È):
	def __init__(A):A.method=b;A.url=b;A.headers=b;A._cookies=b;A.body=b;A.hooks=s();A._body_position=b
	def prepare(A,method=b,url=b,headers=b,files=b,data=b,params=b,auth=b,cookies=b,hooks=b,json=b):A.prepare_method(method);A.prepare_url(url,params);A.prepare_headers(headers);A.prepare_cookies(cookies);A.prepare_body(data,files,json);A.prepare_auth(auth,url);A.prepare_hooks(hooks)
	def __repr__(A):return f"<PreparedRequest [{A.method}]>"
	def copy(A):B=x();B.method=A.method;B.url=A.url;B.headers=A.headers.copy()if A.headers is not b else b;B._cookies=a(A._cookies);B.body=A.body;B.hooks=A.hooks;B._body_position=A._body_position;return B
	def prepare_method(A,method):
		A.method=method
		if A.method is not b:A.method=ë(A.method.upper())
	@À
	def _get_idna_encoded_host(host):
		A=host;import idna as B
		try:A=B.encode(A,uts46=g).decode(j)
		except B.IDNAError:raise É
		return A
	def prepare_url(F,url,params):
		L='URL has an invalid label.';G=params;A=url
		if c(A,h):A=A.decode('utf8')
		else:A=d(A)
		A=A.lstrip()
		if':'in A and not A.lower().startswith('http'):F.url=A;return
		try:J,N,B,K,H,C,O=Ï(A)
		except D as P:raise ß(*P.args)
		if not J:raise M(f"Invalid URL {A!r}: No scheme supplied. Perhaps you meant https://{A}?")
		if not B:raise ß(f"Invalid URL {A!r}: No host supplied")
		if not Z(B):
			try:B=F._get_idna_encoded_host(B)
			except É:raise ß(L)
		elif B.startswith(('*','.')):raise ß(L)
		E=N or l
		if E:E+='@'
		E+=B
		if K:E+=f":{K}"
		if not H:H='/'
		if c(G,(d,h)):G=ë(G)
		I=F._encode_params(G)
		if I:
			if C:C=f"{C}&{I}"
			else:C=I
		A=S(å([J,E,H,b,C,O]));F.url=A
	def prepare_headers(A,headers):
		B=headers;A.headers=Þ()
		if B:
			for C in B.items():µ(C);D,E=C;A.headers[ë(D)]=E
	def prepare_body(A,data,files,json=b):
		E=files;C=data;B=b;D=b
		if not C and json is not b:
			D='application/json'
			try:B=T.dumps(json,allow_nan=i)
			except k as H:raise G(H,request=A)
			if not c(B,h):B=B.encode(j)
		I=all([f(C,o),not c(C,(ä,list,Á,Mapping))])
		if I:
			try:F=Y(C)
			except(Â,AttributeError,Î):F=b
			B=C
			if Ã(B,'tell',b)is not b:
				try:A._body_position=B.tell()
				except OSError:A._body_position=object()
			if E:raise NotImplementedError('Streamed bodies and files are mutually exclusive.')
			if F:A.headers[ª]=U(F)
			else:A.headers['Transfer-Encoding']='chunked'
		else:
			if E:B,D=A._encode_files(E,C)
			elif C:
				B=A._encode_params(C)
				if c(C,ä)or f(C,Å):D=b
				else:D='application/x-www-form-urlencoded'
			A.prepare_content_length(B)
			if D and'content-type'not in A.headers:A.headers['Content-Type']=D
		A.body=B
	def prepare_content_length(A,body):
		if body is not b:
			B=Y(body)
			if B:A.headers[ª]=U(B)
		elif A.method not in('GET','HEAD')and A.headers.get(ª)is b:A.headers[ª]='0'
	def prepare_auth(B,auth,url=l):
		A=auth
		if A is b:C=Q(B.url);A=C if any(C)else b
		if A:
			if c(A,Á)and v(A)==2:A=F(*A)
			D=A(B);B.__dict__.update(D.__dict__);B.prepare_content_length(B.body)
	def prepare_cookies(A,cookies):
		B=cookies
		if c(B,r.CookieJar):A._cookies=B
		else:A._cookies=C(B)
		D=X(A._cookies,A)
		if D is not b:A.headers['Cookie']=D
	def prepare_hooks(C,hooks):
		A=hooks;A=A or[]
		for B in A:C.register_hook(B,A[B])
class º:
	__attrs__=['_content','status_code','headers','url','history',Ë,'reason','cookies','elapsed','request']
	def __init__(A):A._content=i;A._content_consumed=i;A._next=b;A.status_code=b;A.headers=Þ();A.raw=b;A.url=b;A.encoding=b;A.history=[];A.reason=b;A.cookies=C({});A.elapsed=Í.timedelta(0);A.request=b
	def __enter__(A):return A
	def __exit__(A,*B):A.close()
	def __getstate__(A):
		if not A._content_consumed:0
		return{B:Ã(A,B,b)for B in A.__attrs__}
	def __setstate__(A,state):
		for(B,C)in state.items():Ä(A,B,C)
		Ä(A,'_content_consumed',g);Ä(A,'raw',b)
	def __repr__(A):return f"<Response [{A.status_code}]>"
	def __bool__(A):return A.ok
	def __nonzero__(A):return A.ok
	def __iter__(A):return A.iter_content(128)
	@e
	def ok(self):
		try:self.raise_for_status()
		except K:return i
		return g
	@e
	def is_redirect(self):return Ì in self.headers and self.status_code in Æ
	@e
	def is_permanent_redirect(self):return Ì in self.headers and self.status_code in(A.moved_permanently,A.permanent_redirect)
	@e
	def next(self):return self._next
	@e
	def apparent_encoding(self):return W.detect(self.content)[Ë]
	def iter_content(A,chunk_size=1,decode_unicode=i):
		D=chunk_size
		def E():
			if f(A.raw,'stream'):
				try:yield from A.raw.stream(D,decode_content=g)
				except I as C:raise n(C)
				except O as C:raise q(C)
				except J as C:raise ConnectionError(C)
				except B as C:raise m(C)
			else:
				while g:
					E=A.raw.read(D)
					if not E:break
					yield E
			A._content_consumed=g
		if A._content_consumed and c(A._content,bool):raise N()
		elif D is not b and not c(D,int):raise Â(f"chunk_size must be an int, it is instead a {type(D)}.")
		F=u(A._content,D);G=E();C=F if A._content_consumed else G
		if decode_unicode:C=t(C,A)
		return C
	def iter_lines(E,chunk_size=Ñ,decode_unicode=i,delimiter=b):
		D=delimiter;A=b
		for B in E.iter_content(chunk_size=chunk_size,decode_unicode=decode_unicode):
			if A is not b:B=A+B
			if D:C=B.split(D)
			else:C=B.splitlines()
			if C and C[-1]and B and C[-1][-1]==B[-1]:A=C.pop()
			else:A=b
			yield from C
		if A is not b:yield A
	@e
	def content(self):
		A=self
		if A._content is i:
			if A._content_consumed:raise RuntimeError('The content for this response was already consumed')
			if A.status_code==0 or A.raw is b:A._content=b
			else:A._content=b''.join(A.iter_content(Ð))or b''
		A._content_consumed=g;return A._content
	@e
	def text(self):
		D='replace';A=self;B=b;C=A.encoding
		if not A.content:return l
		if A.encoding is b:C=A.apparent_encoding
		try:B=d(A.content,C,errors=D)
		except(LookupError,Â):B=d(A.content,errors=D)
		return B
	def json(B,**C):
		if not B.encoding and B.content and v(B.content)>3:
			D=z(B.content)
			if D is not b:
				try:return T.loads(B.content.decode(D),**C)
				except Ê:pass
				except P as A:raise H(A.msg,A.doc,A.pos)
		try:return T.loads(B.text,**C)
		except P as A:raise H(A.msg,A.doc,A.pos)
	@e
	def links(self):
		B=self.headers.get('link');C={}
		if B:
			D=w(B)
			for A in D:E=A.get('rel')or A.get('url');C[E]=A
		return C
	def raise_for_status(A):
		B=l
		if c(A.reason,h):
			try:C=A.reason.decode(j)
			except Ê:C=A.reason.decode('iso-8859-1')
		else:C=A.reason
		if 400<=A.status_code<500:B=f"{A.status_code} Client Error: {C} for url: {A.url}"
		elif 500<=A.status_code<600:B=f"{A.status_code} Server Error: {C} for url: {A.url}"
		if B:raise K(B,response=A)
	def close(A):
		if not A._content_consumed:A.raw.close()
		B=Ã(A.raw,'release_conn',b)
		if B is not b:B()