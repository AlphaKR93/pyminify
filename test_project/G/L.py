µ='Calling read(decode_content=False) is not supported after read(decode_content=True) was called.'
ª='content-encoding'
z='gzip'
y='flush'
w=getattr
u=DeprecationWarning
t=isinstance
s=setattr
r=bytearray
q=tuple
h='closed'
g=RuntimeError
f=ImportError
d=OSError
c=ValueError
Z=','
X=property
W=hasattr
U=b''
R=False
Q=NotImplementedError
P=len
M=True
L=bool
K=str
G=int
F=bytes
E=None
import collections as º,io as a,json as À,logging,re,sys,typing as N,warnings as i,zlib as S
from contextlib import contextmanager as Á
from http.client import HTTPMessage as Â
from http.client import HTTPResponse as j
from socket import timeout as Ã
try:
	try:import brotlicffi as V
	except f:import brotli as V
except f:V=E
try:
	import zstandard as T;k=k=q(map(G,re.search('^([0-9]+)\\.([0-9]+)',T.__version__).groups()))
	if k<(0,18):T=E
except(AttributeError,f,c):T=E
from.import util as l
from.A import C
from.B import D
from.E import Í,Ì,Î
from.H import n,O,A,o,p,H,I,J,m,B
from.M.D import Ð,Ñ
from.M.E import Ï
Ä=logging.getLogger(__name__)
class Y:
	def decompress(A,data:F):raise Q
	def flush(A):raise Q
class Å(Y):
	def __init__(A):A._first_try=M;A._data=U;A._obj=S.decompressobj()
	def decompress(A,data:F):
		B=data
		if not B:return B
		if not A._first_try:return A._obj.decompress(B)
		A._data+=B
		try:
			C=A._obj.decompress(B)
			if C:A._first_try=R;A._data=E
			return C
		except S.error:
			A._first_try=R;A._obj=S.decompressobj(-S.MAX_WBITS)
			try:return A.decompress(A._data)
			finally:A._data=E
	def flush(A):return A._obj.flush()
class b:FIRST_MEMBER=0;OTHER_MEMBERS=1;SWALLOW_DATA=2
class Æ(Y):
	def __init__(A):A._obj=S.decompressobj(16+S.MAX_WBITS);A._state=b.FIRST_MEMBER
	def decompress(A,data:F):
		B=data;C=r()
		if A._state==b.SWALLOW_DATA or not B:return F(C)
		while M:
			try:C+=A._obj.decompress(B)
			except S.error:
				D=A._state;A._state=b.SWALLOW_DATA
				if D==b.OTHER_MEMBERS:return F(C)
				raise
			B=A._obj.unused_data
			if not B:return F(C)
			A._state=b.OTHER_MEMBERS;A._obj=S.decompressobj(16+S.MAX_WBITS)
	def flush(A):return A._obj.flush()
if V is not E:
	class Ç(Y):
		def __init__(A):
			B='decompress';A._obj=V.Decompressor()
			if W(A._obj,B):s(A,B,A._obj.decompress)
			else:s(A,B,A._obj.process)
		def flush(A):
			if W(A._obj,y):return A._obj.flush()
			return U
if T is not E:
	class È(Y):
		def __init__(A):A._obj=T.ZstdDecompressor().decompressobj()
		def decompress(A,data:F):
			if not data:return U
			B=[A._obj.decompress(data)]
			while A._obj.eof and A._obj.unused_data:C=A._obj.unused_data;A._obj=T.ZstdDecompressor().decompressobj();B.append(A._obj.decompress(C))
			return U.join(B)
		def flush(A):
			B=A._obj.flush()
			if not A._obj.eof:raise O('Zstandard data is incomplete')
			return B
class É(Y):
	def __init__(A,modes:K):A._decoders=[e(A.strip())for A in modes.split(Z)]
	def flush(A):return A._decoders[0].flush()
	def decompress(B,data:F):
		A=data
		for C in reversed(B._decoders):A=C.decompress(A)
		return A
def e(mode:K):
	A=mode
	if Z in A:return É(A)
	if A==z:return Æ()
	if V is not E and A=='br':return Ç()
	if T is not E and A=='zstd':return È()
	return Å()
class Ê:
	def __init__(A):A.buffer=º.deque();A._size=0
	def __len__(A):return A._size
	def put(A,data:F):A.buffer.append(data);A._size+=P(data)
	def get(A,n:G):
		if n==0:return U
		elif not A.buffer:raise g('buffer is empty')
		elif n<0:raise c('n should be > 0')
		D=0;E=a.BytesIO()
		while D<n:
			B=n-D;C=A.buffer.popleft();F=P(C)
			if B<F:G,H=C[:B],C[B:];E.write(G);A.buffer.appendleft(H);A._size-=B;break
			else:E.write(C);A._size-=F
			D+=F
			if not A.buffer:break
		return E.getvalue()
class v(a.IOBase):
	CONTENT_DECODERS=[z,'deflate']
	if V is not E:CONTENT_DECODERS+=['br']
	if T is not E:CONTENT_DECODERS+=['zstd']
	REDIRECT_STATUSES=[301,302,303,307,308];DECODER_ERROR_CLASSES:q[type[Exception],...]=(IOError,S.error)
	if V is not E:DECODER_ERROR_CLASSES+=V.error,
	if T is not E:DECODER_ERROR_CLASSES+=T.ZstdError,
	def __init__(A,*,headers:N.Mapping[K,K]|N.Mapping[F,F]|E=E,status:G,version:G,reason:K|E,decode_content:L,request_url:K|E,retries:Ï|E=E):
		B=headers
		if t(B,D):A.headers=B
		else:A.headers=D(B)
		A.status=status;A.version=version;A.reason=reason;A.decode_content=decode_content;A._has_decoded_content=R;A._request_url=request_url;A.retries=retries;A.chunked=R;C=A.headers.get('transfer-encoding','').lower();F=(A.strip()for A in C.split(Z))
		if'chunked'in F:A.chunked=M
		A._decoder=E
	def get_redirect_location(A):
		if A.status in A.REDIRECT_STATUSES:return A.headers.get('location')
		return R
	@X
	def data(self):raise Q
	def json(A):B=A.data.decode('utf-8');return À.loads(B)
	@X
	def url(self):raise Q
	@url.setter
	def url(self,url:K|E):raise Q
	@X
	def connection(self):raise Q
	@X
	def retries(self):return self._retries
	@retries.setter
	def retries(self,retries:Ï|E):
		A=retries
		if A is not E and A.history:self.url=A.history[-1].redirect_location
		self._retries=A
	def stream(A,amt:G|E=2**16,decode_content:L|E=E):raise Q
	def read(A,amt:G|E=E,decode_content:L|E=E,cache_content:L=R):raise Q
	def read_chunked(A,amt:G|E=E,decode_content:L|E=E):raise Q
	def release_conn(A):raise Q
	def drain_conn(A):raise Q
	def close(A):raise Q
	def _init_decoder(A):
		B=A.headers.get(ª,'').lower()
		if A._decoder is E:
			if B in A.CONTENT_DECODERS:A._decoder=e(B)
			elif Z in B:
				C=[B.strip()for B in B.split(Z)if B.strip()in A.CONTENT_DECODERS]
				if C:A._decoder=e(B)
	def _decode(A,data:F,decode_content:L|E,flush_decoder:L):
		B=data
		if not decode_content:
			if A._has_decoded_content:raise g(µ)
			return B
		try:
			if A._decoder:B=A._decoder.decompress(B);A._has_decoded_content=M
		except A.DECODER_ERROR_CLASSES as C:D=A.headers.get(ª,'').lower();raise O('Received response with content-encoding: %s, but failed to decode it.'%D,C)from C
		if flush_decoder:B+=A._flush_decoder()
		return B
	def _flush_decoder(A):
		if A._decoder:return A._decoder.decompress(U)+A._decoder.flush()
		return U
	def readinto(B,b:r):
		A=B.read(P(b))
		if P(A)==0:return 0
		else:b[:P(A)]=A;return P(A)
	def getheaders(A):i.warn('HTTPResponse.getheaders() is deprecated and will be removed in urllib3 v2.1.0. Instead access HTTPResponse.headers directly.',category=u,stacklevel=2);return A.headers
	def getheader(A,name:K,default:K|E=E):i.warn('HTTPResponse.getheader() is deprecated and will be removed in urllib3 v2.1.0. Instead use HTTPResponse.headers.get(name, default).',category=u,stacklevel=2);return A.headers.get(name,default)
	def info(A):return A.headers
	def geturl(A):return A.url
class x(v):
	def __init__(A,body:C='',headers:N.Mapping[K,K]|N.Mapping[F,F]|E=E,status:G=0,version:G=0,reason:K|E=E,preload_content:L=M,decode_content:L=M,original_response:j|E=E,pool:Ë|E=E,connection:Ì|E=E,msg:Â|E=E,retries:Ï|E=E,enforce_content_length:L=M,request_method:K|E=E,request_url:K|E=E,auto_close:L=M):
		C=decode_content;B=body;super().__init__(headers=headers,status=status,version=version,reason=reason,decode_content=C,request_url=request_url,retries=retries);A.enforce_content_length=enforce_content_length;A.auto_close=auto_close;A._body=E;A._fp=E;A._original_response=original_response;A._fp_bytes_read=0;A.msg=msg
		if B and t(B,(K,F)):A._body=B
		A._pool=pool;A._connection=connection
		if W(B,'read'):A._fp=B
		A.chunk_left=E;A.length_remaining=A._init_length(request_method);A._decoded_buffer=Ê()
		if preload_content and not A._body:A._body=A.read(decode_content=C)
	def release_conn(A):
		if not A._pool or not A._connection:return
		A._pool._put_conn(A._connection);A._connection=E
	def drain_conn(B):
		try:B.read()
		except(A,d,Í,Î):pass
	@X
	def data(self):
		A=self
		if A._body:return A._body
		if A._fp:return A.read(cache_content=M)
	@X
	def connection(self):return self._connection
	def isclosed(A):return Ð(A._fp)
	def tell(A):return A._fp_bytes_read
	def _init_length(B,request_method:K|E):
		C=B.headers.get('content-length')
		if C is not E:
			if B.chunked:Ä.warning('Received response with both Content-Length and Transfer-Encoding set. This is expressly forbidden by RFC 7230 sec 3.3.2. Ignoring Content-Length and attempting to process response as Transfer-Encoding: chunked.');return
			try:
				F={G(A)for A in C.split(Z)}
				if P(F)>1:raise H('Content-Length contained multiple unmatching values (%s)'%C)
				A=F.pop()
			except c:A=E
			else:
				if A<0:A=E
		else:A=E
		try:D=G(B.status)
		except c:D=0
		if D in(204,304)or 100<=D<200 or request_method=='HEAD':A=0
		return A
	@Á
	def _error_catcher(self):
		F='Read timed out.';C=self;D=R
		try:
			try:yield
			except Ã as A:raise J(C._pool,E,F)from A
			except Í as A:
				if'read operation timed out'not in K(A):raise B(A)from A
				raise J(C._pool,E,F)from A
			except(Î,d)as A:raise I(f"Connection broken: {A!r}",A)from A
			D=M
		finally:
			if not D:
				if C._original_response:C._original_response.close()
				if C._connection:C._connection.close()
			if C._original_response and C._original_response.isclosed():C.release_conn()
	def _fp_read(B,amt:G|E=E):
		A=amt;assert B._fp;F=2**31-1
		if(A and A>F or B.length_remaining and B.length_remaining>F)and not l.IS_SECURETRANSPORT and(l.IS_PYOPENSSL or sys.version_info<(3,10)):
			G=a.BytesIO();H=2**28
			while A is E or A!=0:
				if A is not E:C=min(A,H);A-=C
				else:C=H
				D=B._fp.read(C)
				if not D:break
				G.write(D);del D
			return G.getvalue()
		else:return B._fp.read(A)if A is not E else B._fp.read()
	def _raw_read(A,amt:G|E=E):
		C=amt
		if A._fp is E:return
		D=w(A._fp,h,R)
		with A._error_catcher():
			B=A._fp_read(C)if not D else U
			if C is not E and C!=0 and not B:
				A._fp.close()
				if A.enforce_content_length and A.length_remaining is not E and A.length_remaining!=0:raise o(A._fp_bytes_read,A.length_remaining)
		if B:
			A._fp_bytes_read+=P(B)
			if A.length_remaining is not E:A.length_remaining-=P(B)
		return B
	def read(A,amt:G|E=E,decode_content:L|E=E,cache_content:L=R):
		H=cache_content;D=decode_content;C=amt;A._init_decoder()
		if D is E:D=A.decode_content
		if C is not E:
			H=R
			if P(A._decoded_buffer)>=C:return A._decoded_buffer.get(C)
		B=A._raw_read(C);F=C is E or C!=0 and not B
		if not B and P(A._decoded_buffer)==0:return B
		if C is E:
			B=A._decode(B,D,F)
			if H:A._body=B
		else:
			if not D:
				if A._has_decoded_content:raise g(µ)
				return B
			G=A._decode(B,D,F);A._decoded_buffer.put(G)
			while P(A._decoded_buffer)<C and B:B=A._raw_read(C);G=A._decode(B,D,F);A._decoded_buffer.put(G)
			B=A._decoded_buffer.get(C)
		return B
	def stream(A,amt:G|E=2**16,decode_content:L|E=E):
		B=decode_content
		if A.chunked and A.supports_chunked_reads():yield from A.read_chunked(amt,decode_content=B)
		else:
			while not Ð(A._fp)or P(A._decoded_buffer)>0:
				C=A.read(amt=amt,decode_content=B)
				if C:yield C
	def readable(A):return M
	def close(A):
		if not A.closed and A._fp:A._fp.close()
		if A._connection:A._connection.close()
		if not A.auto_close:a.IOBase.close(A)
	@X
	def closed(self):
		A=self
		if not A.auto_close:return a.IOBase.closed.__get__(A)
		elif A._fp is E:return M
		elif W(A._fp,'isclosed'):return A._fp.isclosed()
		elif W(A._fp,h):return A._fp.closed
		else:return M
	def fileno(A):
		if A._fp is E:raise d('HTTPResponse has no file to get a fileno from')
		elif W(A._fp,'fileno'):return A._fp.fileno()
		else:raise d('The file-like object this HTTPResponse is wrapped around has no file descriptor')
	def flush(A):
		if A._fp is not E and W(A._fp,y)and not w(A._fp,h,R):return A._fp.flush()
	def supports_chunked_reads(A):return W(A._fp,'fp')
	def _update_chunk_length(A):
		if A.chunk_left is not E:return
		B=A._fp.fp.readline();B=B.split(b';',1)[0]
		try:A.chunk_left=G(B,16)
		except c:A.close();raise p(A,B)from E
	def _handle_chunk(A,amt:G|E):
		B=amt;C=E
		if B is E:F=A._fp._safe_read(A.chunk_left);C=F;A._fp._safe_read(2);A.chunk_left=E
		elif A.chunk_left is not E and B<A.chunk_left:D=A._fp._safe_read(B);A.chunk_left=A.chunk_left-B;C=D
		elif B==A.chunk_left:D=A._fp._safe_read(B);A._fp._safe_read(2);A.chunk_left=E;C=D
		else:C=A._fp._safe_read(A.chunk_left);A._fp._safe_read(2);A.chunk_left=E
		return C
	def read_chunked(A,amt:G|E=E,decode_content:L|E=E):
		C=decode_content;A._init_decoder()
		if not A.chunked:raise m("Response is not chunked. Header 'transfer-encoding: chunked' is missing.")
		if not A.supports_chunked_reads():raise n('Body should be http.client.HTTPResponse like. It should have have an fp attribute which returns raw chunks.')
		with A._error_catcher():
			if A._original_response and Ñ(A._original_response):A._original_response.close();return
			if A._fp.fp is E:return
			while M:
				A._update_chunk_length()
				if A.chunk_left==0:break
				F=A._handle_chunk(amt);B=A._decode(F,decode_content=C,flush_decoder=R)
				if B:yield B
			if C:
				B=A._flush_decoder()
				if B:yield B
			while A._fp is not E:
				D=A._fp.fp.readline()
				if not D:break
				if D==b'\r\n':break
			if A._original_response:A._original_response.close()
	@X
	def url(self):return self._request_url
	@url.setter
	def url(self,url:K):self._request_url=url
	def __iter__(E):
		C=b'\n';A=[]
		for D in E.stream(decode_content=M):
			if C in D:
				B=D.split(C);yield U.join(A)+B[0]+C
				for G in B[1:-1]:yield G+C
				if B[-1]:A=[B[-1]]
				else:A=[]
			else:A.append(D)
		if A:yield U.join(A)