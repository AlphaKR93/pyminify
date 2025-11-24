k='The read operation timed out'
j='Unexpected EOF'
i='ascii'
c=isinstance
b=OSError
a=list
Z=dict
Y=ImportError
U=property
T=hasattr
N='utf-8'
M=False
L=bool
I=True
H=getattr
G=bytes
D=str
C=None
B=int
import OpenSSL.SSL
from C import x509 as J
try:from C.F import UnsupportedExtension as d
except Y:
	class d(Exception):0
import logging as l,ssl as A,typing as K
from io import BytesIO as m
from socket import socket as V
from socket import timeout as R
from..import util as E
W={E.ssl_.PROTOCOL_TLS:OpenSSL.SSL.SSLv23_METHOD,E.ssl_.PROTOCOL_TLS_CLIENT:OpenSSL.SSL.SSLv23_METHOD,A.PROTOCOL_TLSv1:OpenSSL.SSL.TLSv1_METHOD}
if T(A,'PROTOCOL_TLSv1_1')and T(OpenSSL.SSL,'TLSv1_1_METHOD'):W[A.PROTOCOL_TLSv1_1]=OpenSSL.SSL.TLSv1_1_METHOD
if T(A,'PROTOCOL_TLSv1_2')and T(OpenSSL.SSL,'TLSv1_2_METHOD'):W[A.PROTOCOL_TLSv1_2]=OpenSSL.SSL.TLSv1_2_METHOD
f={A.CERT_NONE:OpenSSL.SSL.VERIFY_NONE,A.CERT_OPTIONAL:OpenSSL.SSL.VERIFY_PEER,A.CERT_REQUIRED:OpenSSL.SSL.VERIFY_PEER+OpenSSL.SSL.VERIFY_FAIL_IF_NO_PEER_CERT}
n={B:A for(A,B)in f.items()}
F=H(OpenSSL.SSL,'OP_NO_SSLv2',0)|H(OpenSSL.SSL,'OP_NO_SSLv3',0)
O=H(OpenSSL.SSL,'OP_NO_TLSv1',0)
P=H(OpenSSL.SSL,'OP_NO_TLSv1_1',0)
Q=H(OpenSSL.SSL,'OP_NO_TLSv1_2',0)
S=H(OpenSSL.SSL,'OP_NO_TLSv1_3',0)
o={A.TLSVersion.MINIMUM_SUPPORTED:F,A.TLSVersion.TLSv1:F,A.TLSVersion.TLSv1_1:F|O,A.TLSVersion.TLSv1_2:F|O|P,A.TLSVersion.TLSv1_3:F|O|P|Q,A.TLSVersion.MAXIMUM_SUPPORTED:F|O|P|Q}
p={A.TLSVersion.MINIMUM_SUPPORTED:F|O|P|Q|S,A.TLSVersion.TLSv1:F|P|Q|S,A.TLSVersion.TLSv1_1:F|Q|S,A.TLSVersion.TLSv1_2:F|S,A.TLSVersion.TLSv1_3:F,A.TLSVersion.MAXIMUM_SUPPORTED:F}
q=16384
g=E.ssl_.SSLContext
r=l.getLogger(__name__)
def w():s();E.SSLContext=h;E.ssl_.SSLContext=h;E.IS_PYOPENSSL=I;E.ssl_.IS_PYOPENSSL=I
def x():E.SSLContext=g;E.ssl_.SSLContext=g;E.IS_PYOPENSSL=M;E.ssl_.IS_PYOPENSSL=M
def s():
	from C.F.C import y
	if H(y,'get_extension_for_class',C)is C:raise Y("'cryptography' module missing required functionality.  Try upgrading to v1.3.4 or newer.")
	from OpenSSL.crypto import X509;A=X509()
	if H(A,'_x509',C)is C:raise Y("'pyOpenSSL' module missing required functionality. Try upgrading to v0.14 or newer.")
def t(name:D):
	A=name
	def E(name:D):
		A=name;import idna as B
		try:
			for C in['*.','.']:
				if A.startswith(C):A=A[len(C):];return C.encode(i)+B.encode(A)
			return B.encode(A)
		except B.core.IDNAError:return
	if':'in A:return A
	B=E(A)
	if B is C:return
	return B.decode(N)
def u(peer_cert:e):
	E=peer_cert.to_cryptography()
	try:A=E.extensions.get_extension_for_class(J.SubjectAlternativeName).value
	except J.ExtensionNotFound:return[]
	except(J.DuplicateExtension,d,J.UnsupportedGeneralNameType,UnicodeError)as F:r.warning('A problem was encountered with the certificate that prevented urllib3 from finding the SubjectAlternativeName field. This can affect certificate validation. The error was %s',F);return[]
	B=[('DNS',A)for A in map(t,A.get_values_for_type(J.DNSName))if A is not C];B.extend(('IP Address',D(A))for A in A.get_values_for_type(J.IPAddress));return B
class X:
	def __init__(A,connection:OpenSSL.SSL.Connection,socket:V,suppress_ragged_eofs:L=I):A.connection=connection;A.socket=socket;A.suppress_ragged_eofs=suppress_ragged_eofs;A._io_refs=0;A._closed=M
	def fileno(A):return A.socket.fileno()
	def _decref_socketios(A):
		if A._io_refs>0:A._io_refs-=1
		if A._closed:A.close()
	def recv(C,*F:K.Any,**G:K.Any):
		try:H=C.connection.recv(*F,**G)
		except OpenSSL.SSL.SysCallError as B:
			if C.suppress_ragged_eofs and B.args==(-1,j):return b''
			else:raise b(B.args[0],D(B))from B
		except OpenSSL.SSL.ZeroReturnError:
			if C.connection.get_shutdown()==OpenSSL.SSL.RECEIVED_SHUTDOWN:return b''
			else:raise
		except OpenSSL.SSL.WantReadError as B:
			if not E.wait_for_read(C.socket,C.socket.gettimeout()):raise R(k)from B
			else:return C.recv(*F,**G)
		except OpenSSL.SSL.Error as B:raise A.SSLError(f"read error: {B!r}")from B
		else:return H
	def recv_into(C,*F:K.Any,**G:K.Any):
		try:return C.connection.recv_into(*F,**G)
		except OpenSSL.SSL.SysCallError as B:
			if C.suppress_ragged_eofs and B.args==(-1,j):return 0
			else:raise b(B.args[0],D(B))from B
		except OpenSSL.SSL.ZeroReturnError:
			if C.connection.get_shutdown()==OpenSSL.SSL.RECEIVED_SHUTDOWN:return 0
			else:raise
		except OpenSSL.SSL.WantReadError as B:
			if not E.wait_for_read(C.socket,C.socket.gettimeout()):raise R(k)from B
			else:return C.recv_into(*F,**G)
		except OpenSSL.SSL.Error as B:raise A.SSLError(f"read error: {B!r}")from B
	def settimeout(A,timeout:float):return A.socket.settimeout(timeout)
	def _send_until_done(B,data:G):
		while I:
			try:return B.connection.send(data)
			except OpenSSL.SSL.WantWriteError as A:
				if not E.wait_for_write(B.socket,B.socket.gettimeout()):raise R()from A
				continue
			except OpenSSL.SSL.SysCallError as A:raise b(A.args[0],D(A))from A
	def sendall(B,data:G):
		A=0
		while A<len(data):C=B._send_until_done(data[A:A+q]);A+=C
	def shutdown(A):A.connection.shutdown()
	def close(A):
		A._closed=I
		if A._io_refs<=0:A._real_close()
	def _real_close(A):
		try:return A.connection.close()
		except OpenSSL.SSL.Error:return
	def getpeercert(B,binary_form:L=M):
		A=B.connection.get_peer_certificate()
		if not A:return A
		if binary_form:return OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_ASN1,A)
		return{'subject':((('commonName',A.get_subject().CN),),),'subjectAltName':u(A)}
	def version(A):return A.connection.get_protocol_version_name()
X.makefile=V.makefile
class h:
	def __init__(C,protocol:B):C.protocol=W[protocol];C._ctx=OpenSSL.SSL.Context(C.protocol);C._options=0;C.check_hostname=M;C._minimum_version=A.TLSVersion.MINIMUM_SUPPORTED;C._maximum_version=A.TLSVersion.MAXIMUM_SUPPORTED
	@U
	def options(self):return self._options
	@options.setter
	def options(self,value:B):self._options=value;self._set_ctx_options()
	@U
	def verify_mode(self):return n[self._ctx.get_verify_mode()]
	@verify_mode.setter
	def verify_mode(self,value:A.VerifyMode):self._ctx.set_verify(f[value],v)
	def set_default_verify_paths(A):A._ctx.set_default_verify_paths()
	def set_ciphers(B,ciphers:G|D):
		A=ciphers
		if c(A,D):A=A.encode(N)
		B._ctx.set_cipher_list(A)
	def load_verify_locations(E,cafile:D|C=C,capath:D|C=C,cadata:G|C=C):
		F=cadata;D=capath;B=cafile
		if B is not C:B=B.encode(N)
		if D is not C:D=D.encode(N)
		try:
			E._ctx.load_verify_locations(B,D)
			if F is not C:E._ctx.load_verify_locations(m(F))
		except OpenSSL.SSL.Error as G:raise A.SSLError(f"unable to load trusted certificates: {G!r}")from G
	def load_cert_chain(D,certfile:D,keyfile:D|C=C,password:D|C=C):
		E=certfile;B=password
		try:
			D._ctx.use_certificate_chain_file(E)
			if B is not C:
				if not c(B,G):B=B.encode(N)
				D._ctx.set_passwd_cb(lambda*A:B)
			D._ctx.use_privatekey_file(keyfile or E)
		except OpenSSL.SSL.Error as F:raise A.SSLError(f"Unable to load certificate chain: {F!r}")from F
	def set_alpn_protocols(B,protocols:a[G|D]):A=protocols;A=[E.util.to_bytes(A,i)for A in A];return B._ctx.set_alpn_protos(A)
	def wrap_socket(H,sock:V,server_side:L=M,do_handshake_on_connect:L=I,suppress_ragged_eofs:L=I,server_hostname:G|D|C=C):
		C=sock;B=server_hostname;F=OpenSSL.SSL.Connection(H._ctx,C)
		if B and not E.ssl_.is_ipaddress(B):
			if c(B,D):B=B.encode(N)
			F.set_tlsext_host_name(B)
		F.set_connect_state()
		while I:
			try:F.do_handshake()
			except OpenSSL.SSL.WantReadError as G:
				if not E.wait_for_read(C,C.gettimeout()):raise R('select timed out')from G
				continue
			except OpenSSL.SSL.Error as G:raise A.SSLError(f"bad handshake: {G!r}")from G
			break
		return X(F,C)
	def _set_ctx_options(A):A._ctx.set_options(A._options|o[A._minimum_version]|p[A._maximum_version])
	@U
	def minimum_version(self):return self._minimum_version
	@minimum_version.setter
	def minimum_version(self,minimum_version:B):self._minimum_version=minimum_version;self._set_ctx_options()
	@U
	def maximum_version(self):return self._maximum_version
	@maximum_version.setter
	def maximum_version(self,maximum_version:B):self._maximum_version=maximum_version;self._set_ctx_options()
def v(cnx:OpenSSL.SSL.Connection,x509:e,err_no:B,err_depth:B,return_code:B):return err_no==0