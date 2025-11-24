j='pypy'
i=hasattr
h=AttributeError
Y=True
X=isinstance
L=tuple
I=bytes
H=getattr
G=bool
F=False
D=int
C=str
A=None
import hmac,os,socket as M,sys as K,typing as J,warnings as k
from binascii import unhexlify as l
from hashlib import md5,sha1,sha256 as m
from..H import V,B
from.J import W,P
N=A
È=A
S=F
Z=F
n=F
a=['http/1.1']
O=J.Tuple[D,D,D,C,D]
o={32:md5,40:sha1,64:m}
def p(implementation_name:C,version_info:O,pypy_version_info:O|A):
	C=implementation_name;A=version_info
	if C==j:return pypy_version_info>=(7,3,8)and A>=(3,8)
	elif C=='cpython':B=A[:2];D=A[2];return B==(3,8)and D>=9 or B==(3,9)and D>=3 or B>=(3,10)
	else:return F
def q(openssl_version:C,openssl_version_number:D,implementation_name:C,version_info:O,pypy_version_info:O|A):A=openssl_version.startswith('OpenSSL ');B=openssl_version_number>=269488335;return A and(B or p(implementation_name,version_info,pypy_version_info))
T={}
try:
	import ssl as E;from ssl import CERT_REQUIRED as u,HAS_NEVER_CHECK_COMMON_NAME as S,OP_NO_COMPRESSION as b,OP_NO_TICKET as c,OPENSSL_VERSION as v,OPENSSL_VERSION_NUMBER as x,PROTOCOL_TLS as Q,PROTOCOL_TLS_CLIENT as U,OP_NO_SSLv2 as d,OP_NO_SSLv3 as e,SSLContext as N,TLSVersion as R;µ=Q
	if S and not q(v,x,K.implementation.name,K.version_info,K.pypy_version_info if K.implementation.name==j else A):S=F
	for f in('TLSv1','TLSv1_1','TLSv1_2'):
		try:T[H(E,f"PROTOCOL_{f}")]=H(R,f)
		except h:continue
	from.H import È
except ImportError:b=131072;c=16384;d=16777216;e=33554432;µ=Q=2;U=16
g=J.Union['_TYPE_PEER_CERT_RET_DICT',I,A]
def Â(cert:I|A,fingerprint:C):
	C=fingerprint
	if cert is A:raise B('No certificate for the peer.')
	C=C.replace(':','').lower();F=len(C);D=o.get(F)
	if not D:raise B(f"Fingerprint of invalid length: {C}")
	G=l(C.encode());E=D(cert).digest()
	if not hmac.compare_digest(E,G):raise B(f'Fingerprints did not match. Expected "{C}", got "{E.hex()}"')
def y(candidate:A|D|C):
	B=candidate
	if B is A:return u
	if X(B,C):
		D=H(E,B,A)
		if D is A:D=H(E,'CERT_'+B)
		return D
	return B
def Å(candidate:A|D|C):
	B=candidate
	if B is A:return Q
	if X(B,C):
		F=H(E,B,A)
		if F is A:F=H(E,'PROTOCOL_'+B)
		return F
	return B
def ª(ssl_version:D|A=A,cert_reqs:D|A=A,options:D|A=A,ciphers:C|A=A,ssl_minimum_version:D|A=A,ssl_maximum_version:D|A=A):
	L=ciphers;J=ssl_version;I=ssl_maximum_version;G=ssl_minimum_version;D=options;C=cert_reqs
	if N is A:raise TypeError("Can't create an SSLContext object without an ssl module")
	if J not in(A,Q,U):
		if G is not A or I is not A:raise ValueError("Can't specify both 'ssl_version' and either 'ssl_minimum_version' or 'ssl_maximum_version'")
		else:G=T.get(J,R.MINIMUM_SUPPORTED);I=T.get(J,R.MAXIMUM_SUPPORTED);k.warn("'ssl_version' option is deprecated and will be removed in urllib3 v2.1.0. Instead use 'ssl_minimum_version'",category=DeprecationWarning,stacklevel=2)
	B=N(U)
	if G is not A:B.minimum_version=G
	else:B.minimum_version=R.TLSv1_2
	if I is not A:B.maximum_version=I
	if L:B.set_ciphers(L)
	C=E.CERT_REQUIRED if C is A else C
	if D is A:D=0;D|=d;D|=e;D|=b;D|=c
	B.options|=D
	if(C==E.CERT_REQUIRED or K.version_info>=(3,7,4))and H(B,'post_handshake_auth',A)is not A:B.post_handshake_auth=Y
	if C==E.CERT_REQUIRED and not Z:B.verify_mode=C;B.check_hostname=Y
	else:B.check_hostname=F;B.verify_mode=C
	try:B.hostname_checks_common_name=F
	except h:pass
	if i(B,'keylog_filename'):
		M=os.environ.get('SSLKEYLOGFILE')
		if M:B.keylog_filename=M
	return B
@J.overload
def z(sock:M.socket,keyfile:C|A=...,certfile:C|A=...,cert_reqs:D|A=...,ca_certs:C|A=...,server_hostname:C|A=...,ssl_version:D|A=...,ciphers:C|A=...,ssl_context:E.SSLContext|A=...,ca_cert_dir:C|A=...,key_password:C|A=...,ca_cert_data:A|C|I=...,tls_in_tls:s[F]=...):0
@J.overload
def z(sock:M.socket,keyfile:C|A=...,certfile:C|A=...,cert_reqs:D|A=...,ca_certs:C|A=...,server_hostname:C|A=...,ssl_version:D|A=...,ciphers:C|A=...,ssl_context:E.SSLContext|A=...,ca_cert_dir:C|A=...,key_password:C|A=...,ca_cert_data:A|C|I=...,tls_in_tls:G=...):0
def z(sock:M.socket,keyfile:C|A=A,certfile:C|A=A,cert_reqs:D|A=A,ca_certs:C|A=A,server_hostname:C|A=A,ssl_version:D|A=A,ciphers:C|A=A,ssl_context:E.SSLContext|A=A,ca_cert_dir:C|A=A,key_password:C|A=A,ca_cert_data:A|C|I=A,tls_in_tls:G=F):
	J=ca_cert_data;I=ca_cert_dir;H=ssl_context;G=ca_certs;F=key_password;E=certfile;D=keyfile;C=H
	if C is A:C=ª(ssl_version,cert_reqs,ciphers=ciphers)
	if G or I or J:
		try:C.load_verify_locations(G,I,J)
		except OSError as K:raise B(K)from K
	elif H is A and i(C,'load_default_certs'):C.load_default_certs()
	if D and F is A and º(D):raise B('Client private key is encrypted, password is required')
	if E:
		if F is A:C.load_cert_chain(E,D)
		else:C.load_cert_chain(E,D,F)
	try:C.set_alpn_protocols(a)
	except NotImplementedError:pass
	L=À(sock,C,tls_in_tls,server_hostname);return L
def Ä(hostname:C|I):
	A=hostname
	if X(A,I):A=A.decode('ascii')
	return G(P.match(A)or W.match(A))
def º(key_file:C):
	with open(key_file)as A:
		for B in A:
			if'ENCRYPTED'in B:return Y
	return F
def À(sock:M.socket,ssl_context:E.SSLContext,tls_in_tls:G,server_hostname:C|A=A):
	B=server_hostname;A=ssl_context
	if tls_in_tls:
		if not È:raise V("TLS in TLS requires support for the 'ssl' module")
		È._validate_ssl_context_for_tls_in_tls(A);return È(sock,A,B)
	return A.wrap_socket(sock,server_hostname=B)