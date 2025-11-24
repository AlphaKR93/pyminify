R=float
Q=tuple
P=memoryview
M=False
L=True
I=bytearray
G=ValueError
E=bytes
D=str
B=int
A=None
import io as H,socket as K,ssl as F,typing as C
from..H import V
O=C.TypeVar('_SelfT',bound='SSLTransport')
S=C.Union[I,P]
J=C.TypeVar('_ReturnValue')
T=16384
class È:
	@staticmethod
	def _validate_ssl_context_for_tls_in_tls(ssl_context:F.SSLContext):
		if not hasattr(ssl_context,'wrap_bio'):raise V("TLS in TLS requires SSLContext.wrap_bio() which isn't available on non-native SSLContext")
	def __init__(A,socket:K.socket,ssl_context:F.SSLContext,server_hostname:D|A=A,suppress_ragged_eofs:bool=L):A.incoming=F.MemoryBIO();A.outgoing=F.MemoryBIO();A.suppress_ragged_eofs=suppress_ragged_eofs;A.socket=socket;A.sslobj=ssl_context.wrap_bio(A.incoming,A.outgoing,server_hostname=server_hostname);A._ssl_io_loop(A.sslobj.do_handshake)
	def __enter__(A:O):return A
	def __exit__(A,*B:C.Any):A.close()
	def fileno(A):return A.socket.fileno()
	def read(A,len:B=1024,buffer:C.Any|A=A):return A._wrap_ssl_read(len,buffer)
	def recv(A,buflen:B=1024,flags:B=0):
		if flags!=0:raise G('non-zero flags not allowed in calls to recv')
		return A._wrap_ssl_read(buflen)
	def recv_into(D,buffer:S,nbytes:B|A=A,flags:B=0):
		C=buffer;B=nbytes
		if flags!=0:raise G('non-zero flags not allowed in calls to recv_into')
		if B is A:B=len(C)
		return D.read(B,C)
	def sendall(C,data:E,flags:B=0):
		if flags!=0:raise G('non-zero flags not allowed in calls to sendall')
		A=0
		with P(data)as D,D.cast('B')as B:
			E=len(B)
			while A<E:F=C.send(B[A:]);A+=F
	def send(A,data:E,flags:B=0):
		if flags!=0:raise G('non-zero flags not allowed in calls to send')
		return A._ssl_io_loop(A.sslobj.write,data)
	def makefile(O,mode:D,buffering:B|A=A,*,encoding:D|A=A,errors:D|A=A,newline:D|A=A):
		N='w';M='r';D=mode;B=buffering
		if not set(D)<={M,N,'b'}:raise G(f"invalid mode {D!r} (only r, w, b allowed)")
		E=N in D;J=M in D or not E;assert J or E;P='b'in D;L=''
		if J:L+=M
		if E:L+=N
		F=K.SocketIO(O,L);O.socket._io_refs+=1
		if B is A:B=-1
		if B<0:B=H.DEFAULT_BUFFER_SIZE
		if B==0:
			if not P:raise G('unbuffered streams must be binary')
			return F
		if J and E:I=H.BufferedRWPair(F,F,B)
		elif J:I=H.BufferedReader(F,B)
		else:assert E;I=H.BufferedWriter(F,B)
		if P:return I
		Q=H.TextIOWrapper(I,encoding,errors,newline);Q.mode=D;return Q
	def unwrap(A):A._ssl_io_loop(A.sslobj.unwrap)
	def close(A):A.socket.close()
	@C.overload
	def getpeercert(self,binary_form:N[M]=...):0
	@C.overload
	def getpeercert(self,binary_form:N[L]):0
	def getpeercert(A,binary_form:bool=M):return A.sslobj.getpeercert(binary_form)
	def version(A):return A.sslobj.version()
	def cipher(A):return A.sslobj.cipher()
	def selected_alpn_protocol(A):return A.sslobj.selected_alpn_protocol()
	def selected_npn_protocol(A):return A.sslobj.selected_npn_protocol()
	def shared_ciphers(A):return A.sslobj.shared_ciphers()
	def compression(A):return A.sslobj.compression()
	def settimeout(A,value:R|A):A.socket.settimeout(value)
	def gettimeout(A):return A.socket.gettimeout()
	def _decref_socketios(A):A.socket._decref_socketios()
	def _wrap_ssl_read(A,len:B,buffer:I|A=A):
		try:return A._ssl_io_loop(A.sslobj.read,len,buffer)
		except F.SSLError as B:
			if B.errno==F.SSL_ERROR_EOF and A.suppress_ragged_eofs:return 0
			else:raise
	@C.overload
	def _ssl_io_loop(self,func:C.Callable[[],A]):0
	@C.overload
	def _ssl_io_loop(self,func:C.Callable[[E],B],arg1:E):0
	@C.overload
	def _ssl_io_loop(self,func:C.Callable[[B,I|A],E],arg1:B,arg2:I|A):0
	def _ssl_io_loop(B,func:C.Callable[...,J],arg1:A|E|B=A,arg2:I|A=A):
		I=arg2;H=arg1;G=func;O=L;D=A
		while O:
			K=A
			try:
				if H is A and I is A:D=G()
				elif I is A:D=G(H)
				else:D=G(H,I)
			except F.SSLError as N:
				if N.errno not in(F.SSL_ERROR_WANT_READ,F.SSL_ERROR_WANT_WRITE):raise N
				K=N.errno
			E=B.outgoing.read();B.socket.sendall(E)
			if K is A:O=M
			elif K==F.SSL_ERROR_WANT_READ:
				E=B.socket.recv(T)
				if E:B.incoming.write(E)
				else:B.incoming.write_eof()
		return D