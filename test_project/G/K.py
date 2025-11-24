m='_proxy_headers'
l=DeprecationWarning
k=BaseException
d='port'
c=isinstance
a=type
X='https'
W=frozenset
U='retries'
S='host'
R=tuple
P='http'
L='scheme'
K=bool
J=False
I=dict
H='headers'
F=int
B=str
A=None
import functools as e,logging as n,typing as C,warnings as f
from types import TracebackType as o
from urllib.parse import urljoin as p
from.B import D,T
from.C import G
from.E import E
from.F import Ë,w,µ
from.H import N,M,q,b
from.M.A import x
from.M.B import Â
from.M.E import Ï
from.M.I import Ò
from.M.J import Url,Ä
r=n.getLogger(__name__)
s='key_file','cert_file','cert_reqs','ca_certs','ssl_version','ssl_minimum_version','ssl_maximum_version','ca_cert_dir','ssl_context','key_password','server_hostname'
h=16384
i=C.TypeVar('_SelfT')
class Q(C.NamedTuple):key_scheme:B;key_host:B;key_port:F|A;key_timeout:Ò|float|F|A;key_retries:Ï|K|F|A;key_block:K|A;key_source_address:R[B,F]|A;key_key_file:B|A;key_key_password:B|A;key_cert_file:B|A;key_cert_reqs:B|A;key_ca_certs:B|A;key_ssl_version:F|B|A;key_ssl_minimum_version:V.TLSVersion|A;key_ssl_maximum_version:V.TLSVersion|A;key_ca_cert_dir:B|A;key_ssl_context:V.SSLContext|A;key_maxsize:F|A;key_headers:W[R[B,B]]|A;key__proxy:Url|A;key__proxy_headers:W[R[B,B]]|A;key__proxy_config:E|A;key_socket_options:x|A;key__socks_options:W[R[B,B]]|A;key_assert_hostname:K|B|A;key_assert_fingerprint:B|A;key_server_hostname:B|A;key_blocksize:F|A
def j(key_class:a[Q],request_context:I[B,C.Any]):
	I='key_blocksize';G='socket_options';D=key_class;B=request_context.copy();B[L]=B[L].lower();B[S]=B[S].lower()
	for C in(H,m,'_socks_options'):
		if C in B and B[C]is not A:B[C]=W(B[C].items())
	E=B.get(G)
	if E is not A:B[G]=R(E)
	for C in list(B.keys()):B['key_'+C]=B.pop(C)
	for F in D._fields:
		if F not in B:B[F]=A
	if B.get(I)is A:B[I]=h
	return D(**B)
t={P:e.partial(j,Q),X:e.partial(j,Q)}
u={P:Ë,X:w}
class O(G):
	proxy:Url|A=A;proxy_config:E|A=A
	def __init__(D,num_pools:F=10,headers:C.Mapping[B,B]|A=A,**A:C.Any):
		super().__init__(headers)
		if U in A:
			B=A[U]
			if not c(B,Ï):E=B is not J;B=Ï.from_int(B,redirect=J);B.raise_on_redirect=E;A=A.copy();A[U]=B
		D.connection_pool_kw=A;D.pools=T(num_pools);D.pool_classes_by_scheme=u;D.key_fn_by_scheme=t.copy()
	def __enter__(A:i):return A
	def __exit__(A,exc_type:a[k]|A,exc_val:k|A,exc_tb:o|A):A.clear();return J
	def _new_pool(C,scheme:B,host:B,port:F,request_context:I[B,C.Any]|A=A):
		E='blocksize';D=scheme;B=request_context;F=C.pool_classes_by_scheme[D]
		if B is A:B=C.connection_pool_kw.copy()
		if B.get(E)is A:B[E]=h
		for G in(L,S,d):B.pop(G,A)
		if D==P:
			for H in s:B.pop(H,A)
		return F(host,port,**B)
	def clear(A):A.pools.clear()
	def connection_from_host(C,host:B|A,port:F|A=A,scheme:B|A=P,pool_kwargs:I[B,C.Any]|A=A):
		B=port
		if not host:raise N('No host specified.')
		A=C._merge_pool_kwargs(pool_kwargs);A[L]=scheme or P
		if not B:B=µ.get(A[L].lower(),80)
		A[d]=B;A[S]=host;return C.connection_from_context(A)
	def connection_from_context(B,request_context:I[B,C.Any]):
		E='strict';A=request_context
		if E in A:f.warn("The 'strict' parameter is no longer needed on Python 3+. This will raise an error in urllib3 v2.1.0.",l);A.pop(E)
		C=A[L].lower();D=B.key_fn_by_scheme.get(C)
		if not D:raise b(C)
		F=D(A);return B.connection_from_pool_key(F,request_context=A)
	def connection_from_pool_key(B,pool_key:Q,request_context:I[B,C.Any]):
		D=pool_key;C=request_context
		with B.pools.lock:
			A=B.pools.get(D)
			if A:return A
			E=C[L];F=C[S];G=C[d];A=B._new_pool(E,F,G,request_context=C);B.pools[D]=A
		return A
	def connection_from_url(B,url:B,pool_kwargs:I[B,C.Any]|A=A):A=Ä(url);return B.connection_from_host(A.host,port=A.port,scheme=A.scheme,pool_kwargs=pool_kwargs)
	def _merge_pool_kwargs(F,override:I[B,C.Any]|A):
		C=override;B=F.connection_pool_kw.copy()
		if C:
			for(D,E)in C.items():
				if E is A:
					try:del B[D]
					except KeyError:pass
				else:B[D]=E
		return B
	def _proxy_requires_url_absolute_form(B,parsed_url:Url):
		if B.proxy is A:return J
		return not Â(B.proxy,B.proxy_config,parsed_url.scheme)
	def urlopen(N,method:B,url:B,redirect:K=True,**B:C.Any):
		S='redirect';P=redirect;L=url;K=method;G=Ä(L)
		if G.scheme is A:f.warn("URLs without a scheme (ie 'https://') are deprecated and will raise an error in a future version of urllib3. To avoid this DeprecationWarning ensure all URLs start with 'https://' or 'http://'. Read more in this issue: https://github.com/urllib3/urllib3/issues/2920",category=l,stacklevel=2)
		O=N.connection_from_host(G.host,port=G.port,scheme=G.scheme);B['assert_same_host']=J;B[S]=J
		if H not in B:B[H]=N.headers
		if N._proxy_requires_url_absolute_form(G):E=O.urlopen(K,L,**B)
		else:E=O.urlopen(K,G.request_uri,**B)
		I=P and E.get_redirect_location()
		if not I:return E
		I=p(L,I)
		if E.status==303:K='GET';B['body']=A;B[H]=D(B[H])._prepare_for_method_change()
		F=B.get(U,E.retries)
		if not c(F,Ï):F=Ï.from_int(F,redirect=P)
		if F.remove_headers_on_redirect and not O.is_same_host(I):
			Q=B[H].copy()
			for R in B[H]:
				if R.lower()in F.remove_headers_on_redirect:Q.pop(R,A)
			B[H]=Q
		try:F=F.increment(K,L,response=E,_pool=O)
		except M:
			if F.raise_on_redirect:E.drain_conn();raise
			return E
		B[U]=F;B[S]=P;r.info('Redirecting %s -> %s',L,I);E.drain_conn();return N.urlopen(K,I,**B)
class Y(O):
	def __init__(A,proxy_url:B,num_pools:F=10,headers:C.Mapping[B,B]|A=A,proxy_headers:C.Mapping[B,B]|A=A,proxy_ssl_context:V.SSLContext|A=A,use_forwarding_for_https:K=J,proxy_assert_hostname:A|B|g[J]=A,proxy_assert_fingerprint:B|A=A,**F:C.Any):
		G=proxy_ssl_context;D=proxy_url
		if c(D,Ë):H=f"{D.scheme}://{D.host}:{D.port}"
		else:H=D
		B=Ä(H)
		if B.scheme not in(P,X):raise q(B.scheme)
		if not B.port:I=µ.get(B.scheme,80);B=B._replace(port=I)
		A.proxy=B;A.proxy_headers=proxy_headers or{};A.proxy_ssl_context=G;A.proxy_config=E(G,use_forwarding_for_https,proxy_assert_hostname,proxy_assert_fingerprint);F['_proxy']=A.proxy;F[m]=A.proxy_headers;F['_proxy_config']=A.proxy_config;super().__init__(num_pools,headers,**F)
	def connection_from_host(A,host:B|A,port:F|A=A,scheme:B|A=P,pool_kwargs:I[B,C.Any]|A=A):
		C=pool_kwargs;B=scheme
		if B==X:return super().connection_from_host(host,port,B,pool_kwargs=C)
		return super().connection_from_host(A.proxy.host,A.proxy.port,A.proxy.scheme,pool_kwargs=C)
	def _set_proxy_headers(D,url:B,headers:C.Mapping[B,B]|A=A):
		B=headers;A={'Accept':'*/*'};C=Ä(url).netloc
		if C:A['Host']=C
		if B:A.update(B)
		return A
	def urlopen(A,method:B,url:B,redirect:K=True,**D:C.Any):
		B=url;E=Ä(B)
		if not Â(A.proxy,A.proxy_config,E.scheme):F=D.get(H,A.headers);D[H]=A._set_proxy_headers(B,F)
		return super().urlopen(method,B,redirect=redirect,**D)
def Z(url:B,**A:C.Any):return Y(proxy_url=url,**A)