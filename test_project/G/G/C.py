f='timed out'
e=float
d=bytearray
Y=ValueError
X=len
W=list
V=Exception
U=OSError
Q=property
O=bool
N=hasattr
K=False
I=True
G=str
D=bytes
B=int
A=None
import contextlib as g,ctypes as E,errno as J,os.path,shutil as h,socket as P,ssl as C,struct as i,threading as j,typing as H,warnings as k,weakref as Z
from socket import socket as R
from..import util as F
from.A.A import v,u
from.A.B import w,x,º,z,y,µ,ª
k.warn("'urllib3.contrib.securetransport' module is deprecated and will be removed in urllib3 v2.1.0. Read more in this issue: https://github.com/urllib3/urllib3/issues/2681",category=DeprecationWarning,stacklevel=2)
a=F.ssl_.SSLContext
S=Z.WeakValueDictionary()
l=j.Lock()
m=16384
M={F.ssl_.PROTOCOL_TLS:(w.kTLSProtocol1,w.kTLSProtocol12),F.ssl_.PROTOCOL_TLS_CLIENT:(w.kTLSProtocol1,w.kTLSProtocol12)}
if N(C,'PROTOCOL_SSLv2'):M[C.PROTOCOL_SSLv2]=w.kSSLProtocol2,w.kSSLProtocol2
if N(C,'PROTOCOL_SSLv3'):M[C.PROTOCOL_SSLv3]=w.kSSLProtocol3,w.kSSLProtocol3
if N(C,'PROTOCOL_TLSv1'):M[C.PROTOCOL_TLSv1]=w.kTLSProtocol1,w.kTLSProtocol1
if N(C,'PROTOCOL_TLSv1_1'):M[C.PROTOCOL_TLSv1_1]=w.kTLSProtocol11,w.kTLSProtocol11
if N(C,'PROTOCOL_TLSv1_2'):M[C.PROTOCOL_TLSv1_2]=w.kTLSProtocol12,w.kTLSProtocol12
b={C.TLSVersion.MINIMUM_SUPPORTED:w.kTLSProtocol1,C.TLSVersion.TLSv1:w.kTLSProtocol1,C.TLSVersion.TLSv1_1:w.kTLSProtocol11,C.TLSVersion.TLSv1_2:w.kTLSProtocol12,C.TLSVersion.MAXIMUM_SUPPORTED:w.kTLSProtocol12}
def s():F.SSLContext=c;F.ssl_.SSLContext=c;F.IS_SECURETRANSPORT=I;F.ssl_.IS_SECURETRANSPORT=I
def t():F.SSLContext=a;F.ssl_.SSLContext=a;F.IS_SECURETRANSPORT=K;F.ssl_.IS_SECURETRANSPORT=K
def n(connection_id:B,data_buffer:B,data_length_pointer:d):
	G=data_length_pointer;C=A
	try:
		C=S.get(connection_id)
		if C is A:return w.errSSLInternal
		L=C.socket;H=G[0];I=C.gettimeout();D=A;B=0
		try:
			while B<H:
				if I is A or I>=0:
					if not F.wait_for_read(L,I):raise U(J.EAGAIN,f)
				M=H-B;O=(E.c_char*M).from_address(data_buffer+B);N=L.recv_into(O,M);B+=N
				if not N:
					if not B:return w.errSSLClosedGraceful
					break
		except U as K:
			D=K.errno
			if D is not A and D!=J.EAGAIN:
				G[0]=B
				if D==J.ECONNRESET or D==J.EPIPE:return w.errSSLClosedAbort
				raise
		G[0]=B
		if B!=H:return w.errSSLWouldBlock
		return 0
	except V as K:
		if C is not A:C._exception=K
		return w.errSSLInternal
def o(connection_id:B,data_buffer:B,data_length_pointer:d):
	G=data_length_pointer;B=A
	try:
		B=S.get(connection_id)
		if B is A:return w.errSSLInternal
		M=B.socket;H=G[0];I=E.string_at(data_buffer,H);K=B.gettimeout();C=A;D=0
		try:
			while D<H:
				if K is A or K>=0:
					if not F.wait_for_write(M,K):raise U(J.EAGAIN,f)
				N=M.send(I);D+=N;I=I[N:]
		except U as L:
			C=L.errno
			if C is not A and C!=J.EAGAIN:
				G[0]=D
				if C==J.ECONNRESET or C==J.EPIPE:return w.errSSLClosedAbort
				raise
		G[0]=D
		if D!=H:return w.errSSLWouldBlock
		return 0
	except V as L:
		if B is not A:B._exception=L
		return w.errSSLInternal
p=u.SSLReadFunc(n)
q=u.SSLWriteFunc(o)
class T:
	def __init__(B,socket:R):B.socket=socket;B.context=A;B._io_refs=0;B._closed=K;B._real_closed=K;B._exception=A;B._keychain=A;B._keychain_dir=A;B._client_cert_chain=A;B._timeout=B.socket.gettimeout();B.socket.settimeout(0)
	@g.contextmanager
	def _raise_on_error(self):
		B=self;B._exception=A;yield
		if B._exception is not A:C,B._exception=B._exception,A;B._real_close();raise C
	def _set_alpn_protocols(C,protocols:W[D]|A):
		A=protocols
		if not A:return
		B=y(A)
		try:D=u.SSLSetALPNProtocols(C.context,B);x(D)
		finally:v.CFRelease(B)
	def _custom_validate(D,verify:O,trust_bundle:D|A):
		E=trust_bundle
		if not verify or E is A:return
		J=w.kSecTrustResultUnspecified,w.kSecTrustResultProceed
		try:
			F=D._evaluate_trust(E)
			if F in J:return
			G=f"error code: {B(F)}";H=A
		except V as I:G=f"exception: {I!r}";H=I
		K=º(D.version());D.socket.sendall(K);L=i.pack('ii',1,0);D.socket.setsockopt(P.SOL_SOCKET,P.SO_LINGER,L);D._real_close();raise C.SSLError(f"certificate verify failed, {G}")from H
	def _evaluate_trust(J,trust_bundle:D):
		F=trust_bundle
		if os.path.isfile(F):
			with open(F,'rb')as K:F=K.read()
		G=A;B=u.SecTrustRef()
		try:
			G=z(F);D=u.SSLCopyPeerTrust(J.context,E.byref(B));x(D)
			if not B:raise C.SSLError('Failed to copy trust reference')
			D=u.SecTrustSetAnchorCertificates(B,G);x(D);D=u.SecTrustSetAnchorCertificatesOnly(B,I);x(D);H=u.SecTrustResultType();D=u.SecTrustEvaluate(B,E.byref(H));x(D)
		finally:
			if B:v.CFRelease(B)
			if G is not A:v.CFRelease(G)
		return H.value
	def handshake(B,server_hostname:D|G|A,verify:O,trust_bundle:D|A,min_version:B,max_version:B,client_cert:G|A,client_key:G|A,client_key_passphrase:H.Any,alpn_protocols:W[D]|A):
		J=client_cert;H=trust_bundle;G=verify;E=server_hostname;B.context=u.SSLCreateContext(A,w.kSSLClientSide,w.kSSLStreamType);C=u.SSLSetIOFuncs(B.context,p,q);x(C)
		with l:
			F=id(B)%2147483647
			while F in S:F=(F+1)%2147483647
			S[F]=B
		C=u.SSLSetConnection(B.context,F);x(C)
		if E:
			if not isinstance(E,D):E=E.encode('utf-8')
			C=u.SSLSetPeerDomainName(B.context,E,X(E));x(C)
		B._set_alpn_protocols(alpn_protocols);C=u.SSLSetProtocolVersionMin(B.context,min_version);x(C);C=u.SSLSetProtocolVersionMax(B.context,max_version);x(C)
		if not G or H is not A:C=u.SSLSetSessionOption(B.context,w.kSSLSessionOptionBreakOnServerAuth,I);x(C)
		if J:B._keychain,B._keychain_dir=ª();B._client_cert_chain=µ(B._keychain,J,client_key);C=u.SSLSetCertificate(B.context,B._client_cert_chain);x(C)
		while I:
			with B._raise_on_error():
				C=u.SSLHandshake(B.context)
				if C==w.errSSLWouldBlock:raise P.timeout('handshake timed out')
				elif C==w.errSSLServerAuthCompleted:B._custom_validate(G,H);continue
				else:x(C);break
	def fileno(A):return A.socket.fileno()
	def _decref_socketios(A):
		if A._io_refs>0:A._io_refs-=1
		if A._closed:A.close()
	def recv(C,bufsiz:B):A=bufsiz;B=E.create_string_buffer(A);F=C.recv_into(B,A);G=B[:F];return G
	def recv_into(B,buffer:E.Array[E.c_char],nbytes:B|A=A):
		D=nbytes;C=buffer
		if B._real_closed:return 0
		if D is A:D=X(C)
		C=(E.c_char*D).from_buffer(C);F=E.c_size_t(0)
		with B._raise_on_error():G=u.SSLRead(B.context,C,D,E.byref(F))
		if G==w.errSSLWouldBlock:
			if F.value==0:raise P.timeout('recv timed out')
		elif G in(w.errSSLClosedGraceful,w.errSSLClosedNoNotify):B._real_close()
		else:x(G)
		return F.value
	def settimeout(A,timeout:e):A._timeout=timeout
	def gettimeout(A):return A._timeout
	def send(B,data:D):
		A=E.c_size_t(0)
		with B._raise_on_error():C=u.SSLWrite(B.context,data,X(data),E.byref(A))
		if C==w.errSSLWouldBlock and A.value==0:raise P.timeout('send timed out')
		else:x(C)
		return A.value
	def sendall(B,data:D):
		A=0
		while A<X(data):C=B.send(data[A:A+m]);A+=C
	def shutdown(A):
		with A._raise_on_error():u.SSLClose(A.context)
	def close(A):
		A._closed=I
		if A._io_refs<=0:A._real_close()
	def _real_close(B):
		B._real_closed=I
		if B.context:v.CFRelease(B.context);B.context=A
		if B._client_cert_chain:v.CFRelease(B._client_cert_chain);B._client_cert_chain=A
		if B._keychain:u.SecKeychainDelete(B._keychain);v.CFRelease(B._keychain);h.rmtree(B._keychain_dir);B._keychain=B._keychain_dir=A
		return B.socket.close()
	def getpeercert(G,binary_form:O=K):
		if not binary_form:raise Y('SecureTransport only supports dumping binary certs')
		B=u.SecTrustRef();C=A;D=A
		try:
			H=u.SSLCopyPeerTrust(G.context,E.byref(B));x(H)
			if not B:return
			I=u.SecTrustGetCertificateCount(B)
			if not I:return
			F=u.SecTrustGetCertificateAtIndex(B,0);assert F;C=u.SecCertificateCopyData(F);assert C;J=v.CFDataGetLength(C);K=v.CFDataGetBytePtr(C);D=E.string_at(K,J)
		finally:
			if C:v.CFRelease(C)
			if B:v.CFRelease(B)
		return D
	def version(B):
		A=u.SSLProtocol();D=u.SSLGetNegotiatedProtocolVersion(B.context,E.byref(A));x(D)
		if A.value==w.kTLSProtocol13:raise C.SSLError('SecureTransport does not support TLS 1.3')
		elif A.value==w.kTLSProtocol12:return'TLSv1.2'
		elif A.value==w.kTLSProtocol11:return'TLSv1.1'
		elif A.value==w.kTLSProtocol1:return'TLSv1'
		elif A.value==w.kSSLProtocol3:return'SSLv3'
		elif A.value==w.kSSLProtocol2:return'SSLv2'
		else:raise C.SSLError(f"Unknown TLS version: {A!r}")
def r(self:R,mode:L['r']|L['w']|L['rw']|L['wr']|L['']='r',buffering:B|A=A,*B:H.Any,**C:H.Any):A=buffering;A=0;return R.makefile(self,mode,A,*B,**C)
T.makefile=r
class c:
	def __init__(E,protocol:B):
		F=protocol;E._minimum_version=C.TLSVersion.MINIMUM_SUPPORTED;E._maximum_version=C.TLSVersion.MAXIMUM_SUPPORTED
		if F not in(A,C.PROTOCOL_TLS,C.PROTOCOL_TLS_CLIENT):E._min_version,E._max_version=M[F]
		E._options=0;E._verify=K;E._trust_bundle=A;E._client_cert=A;E._client_key=A;E._client_key_passphrase=A;E._alpn_protocols=A
	@Q
	def check_hostname(self):return I
	@check_hostname.setter
	def check_hostname(self,value:H.Any):0
	@Q
	def options(self):return self._options
	@options.setter
	def options(self,value:B):self._options=value
	@Q
	def verify_mode(self):return C.CERT_REQUIRED if self._verify else C.CERT_NONE
	@verify_mode.setter
	def verify_mode(self,value:B):self._verify=value==C.CERT_REQUIRED
	def set_default_verify_paths(A):0
	def load_default_certs(A):return A.set_default_verify_paths()
	def set_ciphers(A,ciphers:H.Any):raise Y("SecureTransport doesn't support custom cipher strings")
	def load_verify_locations(C,cafile:G|A=A,capath:G|A=A,cadata:D|A=A):
		B=cafile
		if capath is not A:raise Y('SecureTransport does not support cert directories')
		if B is not A:
			with open(B):0
		C._trust_bundle=B or cadata
	def load_cert_chain(A,certfile:G,keyfile:G|A=A,password:G|A=A):A._client_cert=certfile;A._client_key=keyfile;A._client_cert_passphrase=password
	def set_alpn_protocols(A,protocols:W[G|D]):
		if not N(u,'SSLSetALPNProtocols'):raise NotImplementedError('SecureTransport supports ALPN only in macOS 10.12+')
		A._alpn_protocols=[F.util.to_bytes(A,'ascii')for A in protocols]
	def wrap_socket(A,sock:R,server_side:O=K,do_handshake_on_connect:O=I,suppress_ragged_eofs:O=I,server_hostname:D|G|A=A):assert not server_side;assert do_handshake_on_connect;assert suppress_ragged_eofs;B=T(sock);B.handshake(server_hostname,A._verify,A._trust_bundle,b[A._minimum_version],b[A._maximum_version],A._client_cert,A._client_key,A._client_key_passphrase,A._alpn_protocols);return B
	@Q
	def minimum_version(self):return self._minimum_version
	@minimum_version.setter
	def minimum_version(self,minimum_version:B):self._minimum_version=minimum_version
	@Q
	def maximum_version(self):return self._maximum_version
	@maximum_version.setter
	def maximum_version(self,maximum_version:B):self._maximum_version=maximum_version