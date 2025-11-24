g='POST'
f='https'
Y='cert'
X='verify'
W='HEAD'
V='response'
U=len
O='stream'
N='proxies'
M='GET'
I=isinstance
G='allow_redirects'
H=False
E=True
B=None
import os,sys,time as a
from collections import OrderedDict as P
from datetime import timedelta as h
from.B import ë
from.C import l
from.E import R
from.G import Mapping,r,urljoin,ã
from.H import J,C,D,K
from.I import n,q,p,t
from.K import s,m
from.L import Ç,x,y
from.O import A
from.P import Þ
from.Q import o,v,Q,c,Z,S,e,Á,L
if sys.platform=='win32':T=a.perf_counter
else:T=a.time
def F(request_setting,session_setting,dict_class=P):
	C=session_setting;A=request_setting
	if C is B:return A
	if A is B:return C
	if not(I(C,Mapping)and I(A,Mapping)):return A
	D=dict_class(L(C));D.update(L(A));E=[A for(A,C)in D.items()if C is B]
	for F in E:del D[F]
	return D
def i(request_hooks,session_hooks,dict_class=P):
	C=session_hooks;A=request_hooks
	if C is B or C.get(V)==[]:return A
	if A is B or A.get(V)==[]:return C
	return F(A,C,dict_class)
class j:
	def get_redirect_target(B,resp):
		if resp.is_redirect:A=resp.headers['location'];A=A.encode('latin1');return ë(A,'utf8')
	def should_strip_auth(I,old_url,new_url):
		A=ã(old_url);C=ã(new_url)
		if A.hostname!=C.hostname:return E
		if A.scheme=='http'and A.port in(80,B)and C.scheme==f and C.port in(443,B):return H
		G=A.port!=C.port;D=A.scheme!=C.scheme;F=o.get(A.scheme,B),B
		if not D and A.port in F and C.port in F:return H
		return G or D
	def resolve_redirects(G,resp,req,stream=H,timeout=B,verify=E,cert=B,proxies=B,yield_requests=H,**R):
		Q='Transfer-Encoding';P='Content-Length';L=proxies;J=req;C=resp;O=[];F=G.get_redirect_target(C);M=ã(J.url).fragment
		while F:
			E=J.copy();O.append(C);C.history=O[1:]
			try:0
			except(n,q,RuntimeError):C.raw.read(decode_content=H)
			if U(C.history)>=G.max_redirects:raise t(f"Exceeded {G.max_redirects} redirects.",response=C)
			C.close()
			if F.startswith('//'):T=ã(C.url);F=':'.join([ë(T.scheme),F])
			I=ã(F)
			if I.fragment==''and M:I=I._replace(fragment=M)
			elif I.fragment:M=I.fragment
			F=I.geturl()
			if not I.netloc:F=urljoin(C.url,S(F))
			else:F=S(F)
			E.url=ë(F);G.rebuild_method(E,C)
			if C.status_code not in(A.temporary_redirect,A.permanent_redirect):
				V=P,'Content-Type',Q
				for W in V:E.headers.pop(W,B)
				E.body=B
			N=E.headers;N.pop('Cookie',B);D(E._cookies,J,C.raw);K(E._cookies,G.cookies);E.prepare_cookies(E._cookies);L=G.rebuild_proxies(E,L);G.rebuild_auth(E,C);X=E._body_position is not B and(P in N or Q in N)
			if X:Á(E)
			J=E
			if yield_requests:yield J
			else:C=G.send(J,stream=stream,timeout=timeout,verify=verify,cert=cert,proxies=L,allow_redirects=H,**R);D(G.cookies,E,C.raw);F=G.get_redirect_target(C);yield C
	def rebuild_auth(C,prepared_request,response):
		G='Authorization';A=prepared_request;D=A.headers;E=A.url
		if G in D and C.should_strip_auth(response.request.url,E):del D[G]
		F=Z(E)if C.trust_env else B
		if F is not B:A.prepare_auth(F)
	def rebuild_proxies(I,prepared_request,proxies):
		F='Proxy-Authorization';A=prepared_request;C=A.headers;G=ã(A.url).scheme;H=e(A,proxies,I.trust_env)
		if F in C:del C[F]
		try:D,E=Q(H[G])
		except KeyError:D,E=B,B
		if not G.startswith(f)and D and E:C[F]=R(D,E)
		return H
	def rebuild_method(E,prepared_request,response):
		D=prepared_request;C=response;B=D.method
		if C.status_code==A.see_other and B!=W:B=M
		if C.status_code==A.found and B!=W:B=M
		if C.status_code==A.moved and B==g:B=M
		D.method=B
class d(j):
	__attrs__=['headers','cookies','auth',N,'hooks','params',X,Y,'adapters',O,'trust_env','max_redirects']
	def __init__(A):A.headers=v();A.auth=B;A.proxies={};A.hooks=s();A.params={};A.stream=H;A.verify=E;A.cert=B;A.max_redirects=Ç;A.trust_env=E;A.cookies=C({});A.adapters=P();A.mount('https://',l());A.mount('http://',l())
	def __enter__(A):return A
	def __exit__(A,*B):A.close()
	def prepare_request(B,request):
		A=request;D=A.cookies or{}
		if not I(D,r.CookieJar):D=C(D)
		H=K(K(J(),B.cookies),D);E=A.auth
		if B.trust_env and not E and not B.auth:E=Z(A.url)
		G=x();G.prepare(method=A.method.upper(),url=A.url,files=A.files,data=A.data,json=A.json,headers=F(A.headers,B.headers,dict_class=Þ),params=F(A.params,B.params),auth=F(E,B.auth),cookies=H,hooks=i(A.hooks,B.hooks));return G
	def request(A,method,url,params=B,data=B,headers=B,cookies=B,files=B,auth=B,timeout=B,allow_redirects=E,proxies=B,hooks=B,stream=B,verify=B,cert=B,json=B):B=proxies;E=y(method=method.upper(),url=url,headers=headers,files=files,data=data or{},json=json,params=params or{},auth=auth,cookies=cookies,hooks=hooks);C=A.prepare_request(E);B=B or{};F=A.merge_environment_settings(C.url,B,stream,verify,cert);D={'timeout':timeout,G:allow_redirects};D.update(F);H=A.send(C,**D);return H
	def get(B,url,**A):A.setdefault(G,E);return B.request(M,url,**A)
	def options(B,url,**A):A.setdefault(G,E);return B.request('OPTIONS',url,**A)
	def head(B,url,**A):A.setdefault(G,H);return B.request(W,url,**A)
	def post(A,url,data=B,json=B,**B):return A.request(g,url,data=data,json=json,**B)
	def put(A,url,data=B,**B):return A.request('PUT',url,data=data,**B)
	def patch(A,url,data=B,**B):return A.request('PATCH',url,data=data,**B)
	def delete(A,url,**B):return A.request('DELETE',url,**B)
	def send(C,request,**B):
		F=request;B.setdefault(O,C.stream);B.setdefault(X,C.verify);B.setdefault(Y,C.cert)
		if N not in B:B[N]=e(F,C.proxies,C.trust_env)
		if I(F,y):raise ValueError('You can only send PreparedRequests.')
		J=B.pop(G,E);L=B.get(O);M=F.hooks;P=C.get_adapter(url=F.url);Q=T();A=P.send(F,**B);R=T()-Q;A.elapsed=h(seconds=R);A=m(V,M,A,**B)
		if A.history:
			for K in A.history:D(C.cookies,K.request,K.raw)
		D(C.cookies,F,A.raw)
		if J:S=C.resolve_redirects(A,F,**B);H=[A for A in S]
		else:H=[]
		if H:H.insert(0,A);A=H.pop();A.history=H
		if not J:
			try:A._next=next(C.resolve_redirects(A,F,yield_requests=E,**B))
			except StopIteration:pass
		if not L:0
		return A
	def merge_environment_settings(D,url,proxies,stream,verify,cert):
		H=cert;G=stream;C=proxies;A=verify
		if D.trust_env:
			I=C.get('no_proxy')if C is not B else B;J=c(url,no_proxy=I)
			for(K,L)in J.items():C.setdefault(K,L)
			if A is E or A is B:A=os.environ.get('REQUESTS_CA_BUNDLE')or os.environ.get('CURL_CA_BUNDLE')or A
		C=F(C,D.proxies);G=F(G,D.stream);A=F(A,D.verify);H=F(H,D.cert);return{N:C,O:G,X:A,Y:H}
	def get_adapter(A,url):
		for(B,C)in A.adapters.items():
			if url.lower().startswith(B.lower()):return C
		raise p(f"No connection adapters were found for {url!r}")
	def close(A):
		for B in A.adapters.values():B.close()
	def mount(A,prefix,adapter):
		B=prefix;A.adapters[B]=adapter;D=[A for A in A.adapters if U(A)<U(B)]
		for C in D:A.adapters[C]=A.adapters.pop(C)
	def __getstate__(A):C={C:getattr(A,C,B)for C in A.__attrs__};return C
	def __setstate__(A,state):
		for(B,C)in state.items():setattr(A,B,C)
def k():return d()