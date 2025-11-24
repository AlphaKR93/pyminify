k=DeprecationWarning
j=hasattr
h=BaseException
a=isinstance
Z=ValueError
Y=tuple
U=bytes
T=property
S='http'
Q='https'
M=True
I=bool
H=False
G=int
B=str
A=None
import datetime as b,logging as m,os,re,socket as P,sys,typing as O,warnings as V
from http.client import HTTPConnection as n
from http.client import ResponseNotReady as o
from socket import timeout as p
from.B import D
from.M.D import É
from.M.I import Ð,Ó,Ò
from.M.K import Ã
from.M.L import Ñ
try:import ssl as N;Í=N.SSLError
except(ImportError,AttributeError):
	N=A
	class Í(h):0
from.A import C
from.A import E
from.A import J
from.D import __version__
from.H import F,W,i,K,L,l
from.M import Ë,Ê,connection as R,ssl_ as c
from.M.C import Ï
from.M.F import Â
from.M.F import ª,Ä,y,Å,z
from.M.G import Ç,Æ
from.M.J import Url
ConnectionError=ConnectionError
BrokenPipeError=BrokenPipeError
d=m.getLogger(__name__)
µ={S:80,Q:443}
e=b.date(2022,1,1)
q=re.compile("[^-!#$%&'*+.^_`|~0-9a-zA-Z]")
r=j(sys,'audit')
class Ì(n):
	default_port:O.ClassVar[G]=µ[S];default_socket_options:O.ClassVar[R._TYPE_SOCKET_OPTIONS]=[(P.IPPROTO_TCP,P.TCP_NODELAY,1)];is_verified:I=H;proxy_is_verified:I|A=A;blocksize:G;source_address:Y[B,G]|A;socket_options:R._TYPE_SOCKET_OPTIONS|A;_has_connected_to_proxy:I;_response_options:J|A;_tunnel_host:B|A;_tunnel_port:G|A;_tunnel_scheme:B|A
	def __init__(C,host:B,port:G|A=A,*,timeout:Ó=Ð,source_address:Y[B,G]|A=A,blocksize:G=16384,socket_options:A|R._TYPE_SOCKET_OPTIONS=default_socket_options,proxy:Url|A=A,proxy_config:E|A=A):super().__init__(host=host,port=port,timeout=Ò.resolve_default_timeout(timeout),source_address=source_address,blocksize=blocksize);C.socket_options=socket_options;C.proxy=proxy;C.proxy_config=proxy_config;C._has_connected_to_proxy=H;C._response_options=A;C._tunnel_host=A;C._tunnel_port=A;C._tunnel_scheme=A
	@T
	def host(self):return self._dns_host.rstrip('.')
	@host.setter
	def host(self,value:B):self._dns_host=value
	def _new_conn(A):
		try:C=R.create_connection((A._dns_host,A.port),A.timeout,source_address=A.source_address,socket_options=A.socket_options)
		except P.gaierror as B:raise i(A.host,A,B)from B
		except p as B:raise F(A,f"Connection to {A.host} timed out. (connect timeout={A.timeout})")from B
		except OSError as B:raise K(A,f"Failed to establish a new connection: {B}")from B
		if r:sys.audit('http.client.connect',A,A.host,A.port)
		return C
	def set_tunnel(B,host:B,port:G|A=A,headers:O.Mapping[B,B]|A=A,scheme:B=S):
		A=scheme
		if A not in(S,Q):raise Z(f"Invalid proxy scheme for tunneling: {A!r}, must be either 'http' or 'https'")
		super().set_tunnel(host,port=port,headers=headers);B._tunnel_scheme=A
	def connect(A):
		A.sock=A._new_conn()
		if A._tunnel_host:A._has_connected_to_proxy=M;A._tunnel()
		A._has_connected_to_proxy=I(A.proxy)
	@T
	def is_closed(self):return self.sock is A
	@T
	def is_connected(self):
		if self.sock is A:return H
		return not Ñ(self.sock,timeout=.0)
	@T
	def has_connected_to_proxy(self):return self._has_connected_to_proxy
	def close(B):
		try:super().close()
		finally:B.sock=A;B.is_verified=H;B.proxy_is_verified=A;B._has_connected_to_proxy=H;B._response_options=A;B._tunnel_host=A;B._tunnel_port=A;B._tunnel_scheme=A
	def putrequest(C,method:B,url:B,skip_host:I=H,skip_accept_encoding:I=H):
		A=method;B=q.search(A)
		if B:raise Z(f"Method cannot contain non-token characters {A!r} (found at least {B.group()!r})")
		return super().putrequest(A,url,skip_host=skip_host,skip_accept_encoding=skip_accept_encoding)
	def putheader(E,header:B,*C:B):
		A=header
		if not any(a(A,B)and A==Ë for A in C):super().putheader(A,*C)
		elif Ã(A.lower())not in Ê:D="', '".join([B.title(A)for A in sorted(Ê)]);raise Z(f"urllib3.util.SKIP_HEADER only supports '{D}'")
	def request(C,method:B,url:B,body:C|A=A,headers:O.Mapping[B,B]|A=A,*,chunked:I=H,preload_content:I=M,decode_content:I=M,enforce_content_length:I=M):
		Q='chunked';P='Transfer-Encoding';O='transfer-encoding';I=method;G=headers;D=chunked
		if C.sock is not A:C.sock.settimeout(C.timeout)
		C._response_options=J(request_method=I,request_url=url,preload_content=preload_content,decode_content=decode_content,enforce_content_length=enforce_content_length)
		if G is A:G={}
		F=frozenset(Ã(A.lower())for A in G);R='accept-encoding'in F;S='host'in F;C.putrequest(I,url,skip_accept_encoding=R,skip_host=S);L=Ï(body,method=I,blocksize=C.blocksize);K=L.chunks;N=L.content_length
		if D:
			if O not in F:C.putheader(P,Q)
		elif'content-length'in F:D=H
		elif O in F:D=M
		else:
			D=H
			if N is A:
				if K is not A:D=M;C.putheader(P,Q)
			else:C.putheader('Content-Length',B(N))
		if'user-agent'not in F:C.putheader('User-Agent',t())
		for(T,U)in G.items():C.putheader(T,U)
		C.endheaders()
		if K is not A:
			for E in K:
				if not E:continue
				if a(E,B):E=E.encode('utf-8')
				if D:C.send(b'%x\r\n%b\r\n'%(len(E),E))
				else:C.send(E)
		if D:C.send(b'0\r\n\r\n')
	def request_chunked(A,method:B,url:B,body:C|A=A,headers:O.Mapping[B,B]|A=A):V.warn('HTTPConnection.request_chunked() is deprecated and will be removed in urllib3 v2.1.0. Instead use HTTPConnection.request(..., chunked=True).',category=k,stacklevel=2);A.request(method,url,body=body,headers=headers,chunked=M)
	def getresponse(C):
		if C._response_options is A:raise o()
		E=C._response_options;C._response_options=A;C.sock.settimeout(C.timeout);from.L import x;B=super().getresponse()
		try:É(B.msg)
		except(W,TypeError)as F:d.warning('Failed to parse headers (url=%s): %s',u(C,E.request_url),F,exc_info=M)
		G=D(B.msg.items());H=x(body=B,headers=G,status=B.status,version=B.version,reason=B.reason,preload_content=E.preload_content,decode_content=E.decode_content,original_response=B,enforce_content_length=E.enforce_content_length,request_method=E.request_method,request_url=E.request_url);return H
class º(Ì):
	default_port=µ[Q];cert_reqs:G|B|A=A;ca_certs:B|A=A;ca_cert_dir:B|A=A;ca_cert_data:A|B|U=A;ssl_version:G|B|A=A;ssl_minimum_version:G|A=A;ssl_maximum_version:G|A=A;assert_fingerprint:B|A=A
	def __init__(B,host:B,port:G|A=A,*,timeout:Ó=Ð,source_address:Y[B,G]|A=A,blocksize:G=16384,socket_options:A|R._TYPE_SOCKET_OPTIONS=Ì.default_socket_options,proxy:Url|A=A,proxy_config:E|A=A,cert_reqs:G|B|A=A,assert_hostname:A|B|X[H]=A,assert_fingerprint:B|A=A,server_hostname:B|A=A,ssl_context:N.SSLContext|A=A,ca_certs:B|A=A,ca_cert_dir:B|A=A,ca_cert_data:A|B|U=A,ssl_minimum_version:G|A=A,ssl_maximum_version:G|A=A,ssl_version:G|B|A=A,cert_file:B|A=A,key_file:B|A=A,key_password:B|A=A):
		E=ca_cert_dir;D=ca_certs;C=cert_reqs;super().__init__(host,port=port,timeout=timeout,source_address=source_address,blocksize=blocksize,socket_options=socket_options,proxy=proxy,proxy_config=proxy_config);B.key_file=key_file;B.cert_file=cert_file;B.key_password=key_password;B.ssl_context=ssl_context;B.server_hostname=server_hostname;B.assert_hostname=assert_hostname;B.assert_fingerprint=assert_fingerprint;B.ssl_version=ssl_version;B.ssl_minimum_version=ssl_minimum_version;B.ssl_maximum_version=ssl_maximum_version;B.ca_certs=D and os.path.expanduser(D);B.ca_cert_dir=E and os.path.expanduser(E);B.ca_cert_data=ca_cert_data
		if C is A:
			if B.ssl_context is not A:C=B.ssl_context.verify_mode
			else:C=y(A)
		B.cert_reqs=C
	def set_cert(B,key_file:B|A=A,cert_file:B|A=A,cert_reqs:G|B|A=A,key_password:B|A=A,ca_certs:B|A=A,assert_hostname:A|B|X[H]=A,assert_fingerprint:B|A=A,ca_cert_dir:B|A=A,ca_cert_data:A|B|U=A):
		E=ca_cert_dir;D=ca_certs;C=cert_reqs;V.warn('HTTPSConnection.set_cert() is deprecated and will be removed in urllib3 v2.1.0. Instead provide the parameters to the HTTPSConnection constructor.',category=k,stacklevel=2)
		if C is A:
			if B.ssl_context is not A:C=B.ssl_context.verify_mode
			else:C=y(A)
		B.key_file=key_file;B.cert_file=cert_file;B.cert_reqs=C;B.key_password=key_password;B.assert_hostname=assert_hostname;B.assert_fingerprint=assert_fingerprint;B.ca_certs=D and os.path.expanduser(D);B.ca_cert_dir=E and os.path.expanduser(E);B.ca_cert_data=ca_cert_data
	def connect(C):
		C.sock=D=C._new_conn();E=C.host;F=H
		if C._tunnel_host is not A:
			if C._tunnel_scheme==Q:C.sock=D=C._connect_tls_proxy(C.host,D);F=M
			C._has_connected_to_proxy=M;C._tunnel();E=C._tunnel_host
		if C.server_hostname is not A:E=C.server_hostname
		J=b.date.today()<e
		if J:V.warn(f"System time is way off (before {e}). This will probably lead to SSL verification errors",l)
		G=g(sock=D,cert_reqs=C.cert_reqs,ssl_version=C.ssl_version,ssl_minimum_version=C.ssl_minimum_version,ssl_maximum_version=C.ssl_maximum_version,ca_certs=C.ca_certs,ca_cert_dir=C.ca_cert_dir,ca_cert_data=C.ca_cert_data,cert_file=C.cert_file,key_file=C.key_file,key_password=C.key_password,server_hostname=E,ssl_context=C.ssl_context,tls_in_tls=F,assert_hostname=C.assert_hostname,assert_fingerprint=C.assert_fingerprint);C.sock=G.socket;C.is_verified=G.is_verified;C._has_connected_to_proxy=I(C.proxy)
	def _connect_tls_proxy(B,hostname:B,sock:P.socket):C=B.proxy_config;F=C.ssl_context;D=g(sock,cert_reqs=B.cert_reqs,ssl_version=B.ssl_version,ssl_minimum_version=B.ssl_minimum_version,ssl_maximum_version=B.ssl_maximum_version,ca_certs=B.ca_certs,ca_cert_dir=B.ca_cert_dir,ca_cert_data=B.ca_cert_data,server_hostname=hostname,ssl_context=F,assert_hostname=C.assert_hostname,assert_fingerprint=C.assert_fingerprint,cert_file=A,key_file=A,key_password=A,tls_in_tls=H);B.proxy_is_verified=D.is_verified;return D.socket
class f(O.NamedTuple):socket:N.SSLSocket|È;is_verified:I
def g(sock:P.socket,*,cert_reqs:A|B|G,ssl_version:A|B|G,ssl_minimum_version:G|A,ssl_maximum_version:G|A,cert_file:B|A,key_file:B|A,key_password:B|A,ca_certs:B|A,ca_cert_dir:B|A,ca_cert_data:A|B|U,assert_hostname:A|B|X[H],assert_fingerprint:B|A,server_hostname:B|A,ssl_context:N.SSLContext|A,tls_in_tls:I=H):
	Q=ssl_context;P=ca_cert_data;O=ca_cert_dir;L=ca_certs;K=cert_reqs;F=assert_fingerprint;E=assert_hostname;D=server_hostname;J=H
	if Q is A:J=M;B=ª(ssl_version=Å(ssl_version),ssl_minimum_version=ssl_minimum_version,ssl_maximum_version=ssl_maximum_version,cert_reqs=y(K))
	else:B=Q
	B.verify_mode=y(K)
	if F or E or E is H or c.IS_PYOPENSSL or not c.HAS_NEVER_CHECK_COMMON_NAME:B.check_hostname=H
	if not L and not O and not P and J and j(B,'load_default_certs'):B.load_default_certs()
	if D is not A:
		C=D.strip('[]')
		if'%'in C:C=C[:C.rfind('%')]
		if Ä(C):D=C
	G=z(sock=sock,keyfile=key_file,certfile=cert_file,key_password=key_password,ca_certs=L,ca_cert_dir=O,ca_cert_data=P,server_hostname=D,ssl_context=B,tls_in_tls=tls_in_tls)
	try:
		if F:Â(G.getpeercert(binary_form=M),F)
		elif B.verify_mode!=N.CERT_NONE and not B.check_hostname and E is not H:
			S=G.getpeercert()
			if J:R=H
			else:R=getattr(B,'hostname_checks_common_name',H)or H
			s(S,E or D,R)
		return f(socket=G,is_verified=B.verify_mode==N.CERT_REQUIRED or I(F))
	except h:G.close();raise
def s(cert:w|A,asserted_hostname:B,hostname_checks_common_name:I=H):
	B=cert;A=asserted_hostname;C=A.strip('[]')
	if Ä(C):A=C
	try:Æ(B,A,hostname_checks_common_name)
	except Ç as D:d.warning('Certificate did not match expected hostname: %s. Certificate: %s',A,B);D._peer_cert=B;raise
def À(err:Exception,proxy_scheme:B|A):A=err;C=' '.join(re.split('[^a-z]',B(A).lower()));E='wrong version number'in C or'unknown protocol'in C;F='. Your proxy appears to only use HTTP and not HTTPS, try changing your proxy URL to be HTTP. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#https-proxy-error-http-proxy';D=L(f"Unable to connect to proxy{F if E and proxy_scheme==Q else""}",A);D.__cause__=A;return D
def t():return f"python-urllib3/{__version__}"
class Á:0
if not N:º=Á
v=º
def u(conn:Ì|º,path:B|A=A):A=conn;B=Q if a(A,º)else S;return Url(scheme=B,host=A.host,port=A.port,path=path).url