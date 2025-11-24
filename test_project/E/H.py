g='HttpOnly'
f='secure'
e='version'
d='_cookies_lock'
c=ValueError
b=TypeError
T='comment'
S='expires'
R=KeyError
Q=hasattr
P=property
M='path'
L=list
I='domain'
H=True
G=bool
F=isinstance
E=False
B=iter
A=None
import calendar as h,copy as N,time as U
from.B import ë
from.G import Morsel,k,r,ã,å
try:import threading as V
except ImportError:import dummy_threading as V
class W:
	def __init__(A,request):A._r=request;A._new_headers={};A.type=ã(A._r.url).scheme
	def get_type(A):return A.type
	def get_host(A):return ã(A._r.url).netloc
	def get_origin_req_host(A):return A.get_host()
	def get_full_url(B):
		C='Host'
		if not B._r.headers.get(C):return B._r.url
		D=ë(B._r.headers[C],encoding='utf-8');A=ã(B._r.url);return å([A.scheme,D,A.path,A.params,A.query,A.fragment])
	def is_unverifiable(A):return H
	def has_header(A,name):return name in A._r.headers or name in A._new_headers
	def get_header(A,name,default=A):return A._r.headers.get(name,A._new_headers.get(name,default))
	def add_header(A,key,val):raise NotImplementedError('Cookie headers should be added with add_unredirected_header()')
	def add_unredirected_header(A,name,value):A._new_headers[name]=value
	def get_new_headers(A):return A._new_headers
	@P
	def unverifiable(self):return self.is_unverifiable()
	@P
	def origin_req_host(self):return self.get_origin_req_host()
	@P
	def host(self):return self.get_host()
class i:
	def __init__(A,headers):A._headers=headers
	def info(A):return A._headers
	def getheaders(A,name):A._headers.getheaders(name)
def D(jar,request,response):
	A=response
	if not(Q(A,'_original_response')and A._original_response):return
	B=W(request);C=i(A._original_response.msg);jar.extract_cookies(C,B)
def X(jar,request):A=W(request);jar.add_cookie_header(A);return A.get_new_headers().get('Cookie')
def Y(cookiejar,name,domain=A,path=A):
	F=cookiejar;E=name;D=path;C=domain;G=[]
	for B in F:
		if B.name!=E:continue
		if C is not A and C!=B.domain:continue
		if D is not A and D!=B.path:continue
		G.append((B.domain,B.path,B.name))
	for(C,D,E)in G:F.clear(C,D,E)
class Z(RuntimeError):0
class J(r.CookieJar,k):
	def get(A,name,default=A,domain=A,path=A):
		try:return A._find_no_duplicates(name,domain,path)
		except R:return default
	def set(E,name,value,**C):
		B=value
		if B is A:Y(E,name,domain=C.get(I),path=C.get(M));return
		if F(B,Morsel):D=j(B)
		else:D=O(name,B,**C)
		E.set_cookie(D);return D
	def iterkeys(A):
		for C in B(A):yield C.name
	def keys(A):return L(A.iterkeys())
	def itervalues(A):
		for C in B(A):yield C.value
	def values(A):return L(A.itervalues())
	def iteritems(C):
		for A in B(C):yield(A.name,A.value)
	def items(A):return L(A.iteritems())
	def list_domains(D):
		A=[]
		for C in B(D):
			if C.domain not in A:A.append(C.domain)
		return A
	def list_paths(D):
		A=[]
		for C in B(D):
			if C.path not in A:A.append(C.path)
		return A
	def multiple_domains(F):
		D=[]
		for C in B(F):
			if C.domain is not A and C.domain in D:return H
			D.append(C.domain)
		return E
	def get_dict(F,domain=A,path=A):
		D=domain;E={}
		for C in B(F):
			if(D is A or C.domain==D)and(path is A or C.path==path):E[C.name]=C.value
		return E
	def __contains__(A,name):
		try:return super().__contains__(name)
		except Z:return H
	def __getitem__(A,name):return A._find_no_duplicates(name)
	def __setitem__(A,name,value):A.set(name,value)
	def __delitem__(A,name):Y(A,name)
	def set_cookie(D,cookie,*B,**C):
		A=cookie
		if Q(A.value,'startswith')and A.value.startswith('"')and A.value.endswith('"'):A.value=A.value.replace('\\"','')
		return super().set_cookie(A,*B,**C)
	def update(B,other):
		A=other
		if F(A,r.CookieJar):
			for C in A:B.set_cookie(N.copy(C))
		else:super().update(A)
	def _find(F,name,domain=A,path=A):
		E=path;D=domain
		for C in B(F):
			if C.name==name:
				if D is A or C.domain==D:
					if E is A or C.path==E:return C.value
		raise R(f"{name=}, domain={D!r}, path={E!r}")
	def _find_no_duplicates(H,name,domain=A,path=A):
		G=path;F=domain;E=name;C=A
		for D in B(H):
			if D.name==E:
				if F is A or D.domain==F:
					if G is A or D.path==G:
						if C is not A:raise Z(f"There are multiple cookies with name, {E!r}")
						C=D.value
		if C:return C
		raise R(f"name={E!r}, domain={F!r}, path={G!r}")
	def __getstate__(B):A=B.__dict__.copy();A.pop(d);return A
	def __setstate__(A,state):
		A.__dict__.update(state)
		if d not in A.__dict__:A._cookies_lock=V.RLock()
	def copy(B):A=J();A.set_policy(B.get_policy());A.update(B);return A
	def get_policy(A):return A._policy
def a(jar):
	B=jar
	if B is A:return
	if Q(B,'copy'):return B.copy()
	C=N.copy(B);C.clear()
	for D in B:C.set_cookie(N.copy(D))
	return C
def O(name,value,**C):
	F='port';B={e:0,'name':name,'value':value,F:A,I:'',M:'/',f:E,S:A,'discard':H,T:A,'comment_url':A,'rest':{g:A},'rfc2109':E};D=set(C)-set(B)
	if D:raise b(f"create_cookie() got unexpected keyword arguments: {L(D)}")
	B.update(C);B['port_specified']=G(B[F]);B['domain_specified']=G(B[I]);B['domain_initial_dot']=B[I].startswith('.');B['path_specified']=G(B[M]);return r.Cookie(**B)
def j(morsel):
	D='max-age';B=morsel;C=A
	if B[D]:
		try:C=int(U.time()+int(B[D]))
		except c:raise b(f"max-age: {B[D]} must be integer")
	elif B[S]:F='%a, %d-%b-%Y %H:%M:%S GMT';C=h.timegm(U.strptime(B[S],F))
	return O(comment=B[T],comment_url=G(B[T]),discard=E,domain=B[I],expires=C,name=B.key,path=B[M],port=A,rest={g:B['httponly']},rfc2109=E,secure=G(B[f]),value=B.value,version=B[e]or 0)
def C(cookie_dict,cookiejar=A,overwrite=H):
	C=cookie_dict;B=cookiejar
	if B is A:B=J()
	if C is not A:
		E=[A.name for A in B]
		for D in C:
			if overwrite or D not in E:B.set_cookie(O(D,C[D]))
	return B
def K(cookiejar,cookies):
	B=cookies;A=cookiejar
	if not F(A,r.CookieJar):raise c('You can only merge into CookieJar')
	if F(B,dict):A=C(B,cookiejar=A,overwrite=E)
	elif F(B,r.CookieJar):
		try:A.update(B)
		except AttributeError:
			for D in B:A.set_cookie(D)
	return A