q=Exception
p=AttributeError
o=BaseException
n=float
f='https'
e='http'
b=type
W=OSError
V=isinstance
U=False
T=int
S=True
R=bool
O=str
A=None
import errno as g,logging as r,queue as Y,sys,typing as Q,warnings as s,weakref as t
from socket import timeout as d
from types import TracebackType as u
from.A import C
from.B import D
from.C import G
from.E import Í,BrokenPipeError,Á,Ì,Î,º,E,À
from.E import µ
from.H import P,a,j,h,k,N,M,K,I,L,J,B,TimeoutError
from.M.A import Ô
from.M.B import Â
from.M.C import È,É
from.M.E import Ï
from.M.G import Ç
from.M.I import Ð,Ê,Ò
from.M.J import Url,Æ
from.M.J import Å
from.M.J import Ä
from.M.K import Ã
X=r.getLogger(__name__)
Z=Q.Union[Ò,n,Ê,A]
l=Q.TypeVar('_SelfT')
class y:
	scheme:O|A=A;QueueCls=Y.LifoQueue
	def __init__(A,host:O,port:T|A=A):
		B=host
		if not B:raise N('No host specified.')
		A.host=c(B,scheme=A.scheme);A.port=port;A._tunnel_host=Å(B,scheme=A.scheme).lower()
	def __str__(A):return f"{b(A).__name__}(host={A.host!r}, port={A.port!r})"
	def __enter__(A:l):return A
	def __exit__(A,exc_type:b[o]|A,exc_val:o|A,exc_tb:u|A):A.close();return U
	def close(A):0
x={g.EAGAIN,g.EWOULDBLOCK}
class Ë(y,G):
	scheme=e;ConnectionCls:b[F]|b[H]=Ì
	def __init__(B,host:O,port:T|A=A,timeout:Z|A=Ð,maxsize:T=1,block:R=U,headers:Q.Mapping[O,O]|A=A,retries:Ï|R|T|A=A,_proxy:Url|A=A,_proxy_headers:Q.Mapping[O,O]|A=A,_proxy_config:E|A=A,**F:Q.Any):
		E=maxsize;D=retries;C=timeout;y.__init__(B,host,port);G.__init__(B,headers)
		if not V(C,Ò):C=Ò.from_float(C)
		if D is A:D=Ï.DEFAULT
		B.timeout=C;B.retries=D;B.pool=B.QueueCls(E);B.block=block;B.proxy=_proxy;B.proxy_headers=_proxy_headers or{};B.proxy_config=_proxy_config
		for I in range(E):B.pool.put(A)
		B.num_connections=0;B.num_requests=0;B.conn_kw=F
		if B.proxy:B.conn_kw.setdefault('socket_options',[]);B.conn_kw['proxy']=B.proxy;B.conn_kw['proxy_config']=B.proxy_config
		H=B.pool;t.finalize(B,m,H)
	def _new_conn(A):A.num_connections+=1;X.debug('Starting new HTTP connection (%d): %s:%s',A.num_connections,A.host,A.port or'80');B=A.ConnectionCls(host=A.host,port=A.port,timeout=A.timeout.connect_timeout,**A.conn_kw);return B
	def _get_conn(B,timeout:n|A=A):
		D='Pool is closed.';C=A
		if B.pool is A:raise P(B,D)
		try:C=B.pool.get(block=B.block,timeout=timeout)
		except p:raise P(B,D)from A
		except Y.Empty:
			if B.block:raise a(B,"Pool is empty and a new connection can't be opened due to blocking mode.")from A
			pass
		if C and Ô(C):X.debug('Resetting dropped connection: %s',B.host);C.close()
		return C or B._new_conn()
	def _put_conn(B,conn:F|A):
		C=conn
		if B.pool is not A:
			try:B.pool.put(C,block=U);return
			except p:pass
			except Y.Full:
				if C:C.close()
				if B.block:raise j(B,'Pool reached maximum size and no more connections are allowed.')from A
				X.warning('Connection pool is full, discarding connection: %s. Connection pool size: %s',B.host,B.pool.qsize())
		if C:C.close()
	def _validate_conn(A,conn:F):0
	def _prepare_proxy(A,conn:F):0
	def _get_timeout(B,timeout:Z):
		A=timeout
		if A is Ð:return B.timeout.clone()
		if V(A,Ò):return A.clone()
		else:return Ò.from_float(A)
	def _raise_timeout(B,err:Í|W|d,url:O,timeout_value:Z|A):
		C=timeout_value;A=err
		if V(A,d):raise J(B,url,f"Read timed out. (read timeout={C})")from A
		if hasattr(A,'errno')and A.errno in x:raise J(B,url,f"Read timed out. (read timeout={C})")from A
	def _make_request(C,conn:F,method:O,url:O,body:C|A=A,headers:Q.Mapping[O,O]|A=A,retries:Ï|A=A,timeout:Z=Ð,chunked:R=U,response_conn:F|A=A,preload_content:R=S,decode_content:R=S,enforce_content_length:R=S):
		L=method;F=url;A=conn;C.num_requests+=1;I=C._get_timeout(timeout);I.start_connect();A.timeout=Ò.resolve_default_timeout(I.connect_timeout)
		try:
			try:C._validate_conn(A)
			except(d,Í)as D:C._raise_timeout(err=D,url=F,timeout_value=A.timeout);raise
		except(W,K,TimeoutError,Í,Ç,B)as D:
			G=D
			if V(D,(Í,Ç)):G=B(D)
			if V(G,(W,K,TimeoutError,B))and(A and A.proxy and not A.has_connected_to_proxy):G=À(G,A.proxy.scheme)
			raise G
		try:A.request(L,F,body=body,headers=headers,chunked=chunked,preload_content=preload_content,decode_content=decode_content,enforce_content_length=enforce_content_length)
		except BrokenPipeError:pass
		except W as D:
			if D.errno!=g.EPROTOTYPE:raise
		H=I.read_timeout
		if not A.is_closed:
			if H==0:raise J(C,F,f"Read timed out. (read timeout={H})")
			A.timeout=H
		try:E=A.getresponse()
		except(Í,W)as D:C._raise_timeout(err=D,url=F,timeout_value=H);raise
		E.retries=retries;E._connection=response_conn;E._pool=C;X.debug('%s://%s:%s "%s %s %s" %s %s',C.scheme,C.host,C.port,L,F,A._http_vsn_str,E.status,E.length_remaining);return E
	def close(B):
		if B.pool is A:return
		C,B.pool=B.pool,A;m(C)
	def is_same_host(C,url:O):
		if url.startswith('/'):return S
		B,F,E,D,*F=Ä(url);B=B or e
		if E is not A:E=c(E,scheme=B)
		if C.port and not D:D=µ.get(B)
		elif not C.port and D==µ.get(B):D=A
		return(B,E,D)==(C.scheme,C.host,C.port)
	def urlopen(C,method:O,url:O,body:C|A=A,headers:Q.Mapping[O,O]|A=A,retries:Ï|R|T|A=A,redirect:R=S,assert_same_host:R=S,timeout:Z=Ð,pool_timeout:T|A=A,release_conn:R|A=A,chunked:R=U,body_pos:È|A=A,preload_content:R=S,decode_content:R=S,**k:Q.Any):
		j=decode_content;i=chunked;g=pool_timeout;f=timeout;e=assert_same_host;c=preload_content;b=body_pos;Z=redirect;T=body;P=release_conn;N=method;J=headers;F=url;E=retries;o=Ä(F);t=o.scheme
		if J is A:J=C.headers
		if not V(E,Ï):E=Ï.from_int(E,redirect=Z,default=C.retries)
		if P is A:P=c
		if e and not C.is_same_host(F):raise h(C,F,E)
		if F.startswith('/'):F=Ã(Æ(F))
		else:F=Ã(o.url)
		G=A;m=P;p=Â(C.proxy,C.proxy_config,t)
		if not p:J=J.copy();J.update(C.proxy_headers)
		r=A;l=U;b=É(T,b)
		try:
			s=C._get_timeout(f);G=C._get_conn(timeout=g);G.timeout=s.connect_timeout
			if C.proxy is not A and p and G.is_closed:
				try:C._prepare_proxy(G)
				except(Í,W,d)as Y:C._raise_timeout(err=Y,url=C.proxy.url,timeout_value=G.timeout);raise
			u=G if not P else A;H=C._make_request(G,N,F,timeout=s,body=T,headers=J,chunked=i,retries=E,response_conn=u,preload_content=c,decode_content=j,**k);l=S
		except a:l=S;m=U;raise
		except(TimeoutError,Î,W,I,Í,B,Ç,L)as Y:
			l=U;O=Y
			if V(Y,(Í,Ç)):O=B(Y)
			if V(O,(W,K,TimeoutError,B,Î))and(G and G.proxy and not G.has_connected_to_proxy):O=À(O,G.proxy.scheme)
			elif V(O,(W,Î)):O=I('Connection aborted.',O)
			E=E.increment(N,F,error=O,_pool=C,_stacktrace=sys.exc_info()[2]);E.sleep();r=Y
		finally:
			if not l:
				if G:G.close();G=A
				m=S
			if m:C._put_conn(G)
		if not G:X.warning("Retrying (%r) after connection broken by '%r': %s",E,r,F);return C.urlopen(N,F,T,J,E,Z,e,timeout=f,pool_timeout=g,release_conn=P,chunked=i,body_pos=b,preload_content=c,decode_content=j,**k)
		n=Z and H.get_redirect_location()
		if n:
			if H.status==303:N='GET';T=A;J=D(J)._prepare_for_method_change()
			try:E=E.increment(N,F,response=H,_pool=C)
			except M:
				if E.raise_on_redirect:H.drain_conn();raise
				return H
			H.drain_conn();E.sleep_for_retry(H);X.debug('Redirecting %s -> %s',F,n);return C.urlopen(N,n,T,J,retries=E,redirect=Z,assert_same_host=e,timeout=f,pool_timeout=g,release_conn=P,chunked=i,body_pos=b,preload_content=c,decode_content=j,**k)
		v=R(H.headers.get('Retry-After'))
		if E.is_retry(N,H.status,v):
			try:E=E.increment(N,F,response=H,_pool=C)
			except M:
				if E.raise_on_status:H.drain_conn();raise
				return H
			H.drain_conn();E.sleep(H);X.debug('Retry: %s',F);return C.urlopen(N,F,T,J,retries=E,redirect=Z,assert_same_host=e,timeout=f,pool_timeout=g,release_conn=P,chunked=i,body_pos=b,preload_content=c,decode_content=j,**k)
		return H
class w(Ë):
	scheme=f;ConnectionCls:b[H]=º
	def __init__(A,host:O,port:T|A=A,timeout:Z|A=Ð,maxsize:T=1,block:R=U,headers:Q.Mapping[O,O]|A=A,retries:Ï|R|T|A=A,_proxy:Url|A=A,_proxy_headers:Q.Mapping[O,O]|A=A,key_file:O|A=A,cert_file:O|A=A,cert_reqs:T|O|A=A,key_password:O|A=A,ca_certs:O|A=A,ssl_version:T|O|A=A,ssl_minimum_version:ssl.TLSVersion|A=A,ssl_maximum_version:ssl.TLSVersion|A=A,assert_hostname:O|i[U]|A=A,assert_fingerprint:O|A=A,ca_cert_dir:O|A=A,**B:Q.Any):super().__init__(host,port,timeout,maxsize,block,headers,retries,_proxy,_proxy_headers,**B);A.key_file=key_file;A.cert_file=cert_file;A.cert_reqs=cert_reqs;A.key_password=key_password;A.ca_certs=ca_certs;A.ca_cert_dir=ca_cert_dir;A.ssl_version=ssl_version;A.ssl_minimum_version=ssl_minimum_version;A.ssl_maximum_version=ssl_maximum_version;A.assert_hostname=assert_hostname;A.assert_fingerprint=assert_fingerprint
	def _prepare_proxy(A,conn:º):
		if A.proxy and A.proxy.scheme==f:B=f
		else:B=e
		conn.set_tunnel(scheme=B,host=A._tunnel_host,port=A.port,headers=A.proxy_headers);conn.connect()
	def _new_conn(B):
		B.num_connections+=1;X.debug('Starting new HTTPS connection (%d): %s:%s',B.num_connections,B.host,B.port or'443')
		if not B.ConnectionCls or B.ConnectionCls is Á:raise ImportError("Can't connect to HTTPS URL because the SSL module is not available.")
		C=B.host;D=B.port
		if B.proxy is not A and B.proxy.host is not A:C=B.proxy.host;D=B.proxy.port
		return B.ConnectionCls(host=C,port=D,timeout=B.timeout.connect_timeout,cert_file=B.cert_file,key_file=B.key_file,key_password=B.key_password,cert_reqs=B.cert_reqs,ca_certs=B.ca_certs,ca_cert_dir=B.ca_cert_dir,assert_hostname=B.assert_hostname,assert_fingerprint=B.assert_fingerprint,ssl_version=B.ssl_version,ssl_minimum_version=B.ssl_minimum_version,ssl_maximum_version=B.ssl_maximum_version,**B.conn_kw)
	def _validate_conn(B,conn:F):
		A=conn;super()._validate_conn(A)
		if A.is_closed:A.connect()
		if not A.is_verified:s.warn(f"Unverified HTTPS request is being made to host '{A.host}'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings",k)
def z(url:O,**C:Q.Any):
	A,E,D,B,*E=Ä(url);A=A or e;B=B or µ.get(A,80)
	if A==f:return w(D,port=B,**C)
	else:return Ë(D,port=B,**C)
@Q.overload
def c(host,scheme:O|A):0
@Q.overload
def c(host:O,scheme:O|A):0
def c(host:O|A,scheme:O|A):
	A=host;A=Å(A,scheme)
	if A and A.startswith('[')and A.endswith(']'):A=A[1:-1]
	return A
def ª(pool:Ë|w,path:O|A=A):A=pool;return Url(scheme=A.scheme,host=A.host,port=A.port,path=path).url
def m(pool:Y.LifoQueue[Q.Any]):
	try:
		while S:
			A=pool.get(block=U)
			if A:A.close()
	except Y.Empty:pass