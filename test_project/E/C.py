h='https'
g='socks'
f=ValueError
e=NotImplementedError
X=True
W=getattr
U=OSError
T=False
S=isinstance
E=None
import os.path
from G.H import P,F,A,H,N,M,K,I,L,J,G,B
from G.K import O,Z
from G.M import Timeout as V
from G.M import parse_url as i
from G.M.E import Ï
from.E import R
from.G import ä,ã
from.H import D
from.I import ConnectionError,r,à,u,p,ß,o,s,v,m
from.L import º
from.P import Þ
from.Q import n,q,Q,a,ª,d,À
try:from G.G.D import C
except ImportError:
	def C(*A,**B):raise p('Missing dependencies for SOCKS support.')
Y=T
b=10
c=0
k=E
class j:
	def __init__(A):super().__init__()
	def send(A,request,stream=T,timeout=E,verify=X,cert=E,proxies=E):raise e
	def close(A):raise e
class l(j):
	__attrs__=['max_retries','config','_pool_connections','_pool_maxsize','_pool_block']
	def __init__(A,pool_connections=b,pool_maxsize=b,max_retries=c,pool_block=Y):
		E=pool_block;D=max_retries;C=pool_maxsize;B=pool_connections
		if D==c:A.max_retries=Ï(0,read=T)
		else:A.max_retries=Ï.from_int(D)
		A.config={};A.proxy_manager={};super().__init__();A._pool_connections=B;A._pool_maxsize=C;A._pool_block=E;A.init_poolmanager(B,C,block=E)
	def __getstate__(A):return{B:W(A,B,E)for B in A.__attrs__}
	def __setstate__(A,state):
		A.proxy_manager={};A.config={}
		for(B,C)in state.items():setattr(A,B,C)
		A.init_poolmanager(A._pool_connections,A._pool_maxsize,block=A._pool_block)
	def init_poolmanager(A,connections,maxsize,block=Y,**E):D=block;C=maxsize;B=connections;A._pool_connections=B;A._pool_maxsize=C;A._pool_block=D;A.poolmanager=O(num_pools=B,maxsize=C,block=D,**E)
	def proxy_manager_for(A,proxy,**E):
		B=proxy
		if B in A.proxy_manager:D=A.proxy_manager[B]
		elif B.lower().startswith(g):F,G=Q(B);D=A.proxy_manager[B]=C(B,username=F,password=G,num_pools=A._pool_connections,maxsize=A._pool_maxsize,block=A._pool_block,**E)
		else:H=A.proxy_headers(B);D=A.proxy_manager[B]=Z(B,proxy_headers=H,num_pools=A._pool_connections,maxsize=A._pool_maxsize,block=A._pool_block,**E)
		return D
	def cert_verify(F,conn,url,verify,cert):
		D=verify;C=cert;A=conn
		if url.lower().startswith(h)and D:
			B=E
			if D is not X:B=D
			if not B:B=q(n)
			if not B or not os.path.exists(B):raise U(f"Could not find a suitable TLS CA certificate bundle, invalid path: {B}")
			A.cert_reqs='CERT_REQUIRED'
			if not os.path.isdir(B):A.ca_certs=B
			else:A.ca_cert_dir=B
		else:A.cert_reqs='CERT_NONE';A.ca_certs=E;A.ca_cert_dir=E
		if C:
			if not S(C,ä):A.cert_file=C[0];A.key_file=C[1]
			else:A.cert_file=C;A.key_file=E
			if A.cert_file and not os.path.exists(A.cert_file):raise U(f"Could not find the TLS certificate file, invalid path: {A.cert_file}")
			if A.key_file and not os.path.exists(A.key_file):raise U(f"Could not find the TLS key file, invalid path: {A.key_file}")
	def build_response(F,req,resp):
		C=resp;B=req;A=º();A.status_code=W(C,'status',E);A.headers=Þ(W(C,'headers',{}));A.encoding=a(A.headers);A.raw=C;A.reason=A.raw.reason
		if S(B.url,bytes):A.url=B.url.decode('utf-8')
		else:A.url=B.url
		D(A.cookies,B,C);A.request=B;A.connection=F;return A
	def get_connection(C,url,proxies=E):
		A=url;B=d(A,proxies)
		if B:
			B=ª(B,'http');E=i(B)
			if not E.host:raise u('Please check proxy URL. It is malformed and could be missing the host.')
			F=C.proxy_manager_for(B);D=F.connection_from_url(A)
		else:G=ã(A);A=G.geturl();D=C.poolmanager.connection_from_url(A)
		return D
	def close(A):
		A.poolmanager.clear()
		for B in A.proxy_manager.values():B.clear()
	def request_url(H,request,proxies):
		A=request;B=d(A.url,proxies);E=ã(A.url).scheme;F=B and E!=h;C=T
		if B:G=ã(B).scheme.lower();C=G.startswith(g)
		D=A.path_url
		if F and not C:D=À(A.url)
		return D
	def add_headers(A,request,**B):0
	def proxy_headers(D,proxy):
		A={};B,C=Q(proxy)
		if B:A['Proxy-Authorization']=R(B,C)
		return A
	def send(Q,request,stream=T,timeout=E,verify=X,cert=E,proxies=E):
		W=verify;R=proxies;O=timeout;D=request
		try:X=Q.get_connection(D.url,R)
		except N as C:raise ß(C,request=D)
		Q.cert_verify(X,D.url,W,cert);Y=Q.request_url(D,R);Q.add_headers(D,stream=stream,timeout=O,verify=W,cert=cert,proxies=R);Z=not(D.body is E or'Content-Length'in D.headers)
		if S(O,tuple):
			try:a,b=O;O=V(connect=a,read=b)
			except f:raise f(f"Invalid timeout {O}. Pass a (connect, read) timeout tuple, or a single float to set both timeouts to the same value.")
		elif S(O,V):0
		else:O=V(connect=O,read=O)
		try:c=X.urlopen(method=D.method,url=Y,body=D.body,headers=D.headers,redirect=T,assert_same_host=T,preload_content=T,decode_content=T,retries=Q.max_retries,timeout=O,chunked=Z)
		except(I,U)as d:raise ConnectionError(d,request=D)
		except M as C:
			if S(C.reason,F):
				if not S(C.reason,K):raise r(C,request=D)
			if S(C.reason,G):raise v(C,request=D)
			if S(C.reason,L):raise o(C,request=D)
			if S(C.reason,B):raise m(C,request=D)
			raise ConnectionError(C,request=D)
		except P as C:raise ConnectionError(C,request=D)
		except L as C:raise o(C)
		except(B,A)as C:
			if S(C,B):raise m(C,request=D)
			elif S(C,J):raise s(C,request=D)
			elif S(C,H):raise à(C,request=D)
			else:raise
		return Q.build_response(D,c)