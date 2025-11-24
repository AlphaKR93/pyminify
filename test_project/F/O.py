Ã='content-range'
Â='http.response.pathsend'
Á='last-modified'
À='text/plain'
º=classmethod
µ=RuntimeError
ª=Exception
q='rb'
p='content-length'
o='none'
n='strict'
m=min
l=ValueError
k='-'
j=memoryview
i=isinstance
f='http.response.start'
e='headers'
d='status'
c='lax'
a=b''
Y='latin-1'
V=list
U=bytes
T=tuple
S='more_body'
R='http.response.body'
Q=bool
O=False
N='body'
M=True
L=len
I='type'
G=int
F=str
B=None
import hashlib,http.cookies,json,os,stat,warnings as Ä
from collections.abc import AsyncIterable as r,Awaitable as Å,Callable as s,Iterable as Æ,Mapping as Z,Sequence as Ç
from datetime import datetime as t
from email.utils import format_datetime as È,formatdate as É
from functools import partial as u
from mimetypes import guess_type as Ê
from secrets import token_hex as Ë
from typing import Any as g,Literal as v
from urllib.parse import quote as w
import anyio,anyio.to_thread
from F.B import E
from F.E import A
from F.F import Ï
from F.I import W,D,J
from F.N import Ð
from F.V import Ò,Ñ,Send
class C:
	media_type=B;charset='utf-8'
	def __init__(A,content:g=B,status_code:G=200,headers:Z[F,F]|B=B,media_type:F|B=B,background:A|B=B):
		C=media_type;A.status_code=status_code
		if C is not B:A.media_type=C
		A.background=background;A.body=A.render(content);A.init_headers(headers)
	def render(C,content:g):
		A=content
		if A is B:return a
		if i(A,U|j):return A
		return A.encode(C.charset)
	def init_headers(A,headers:Z[F,F]|B=B):
		O=b'content-type';K=b'content-length';E=headers
		if E is B:C=[];G=M;H=M
		else:C=[(A.lower().encode(Y),B.encode(Y))for(A,B)in E.items()];I=[A[0]for A in C];G=K not in I;H=O not in I
		J=getattr(A,N,B)
		if J is not B and G and not(A.status_code<200 or A.status_code in(204,304)):P=F(L(J));C.append((K,P.encode(Y)))
		D=A.media_type
		if D is not B and H:
			if D.startswith('text/')and'charset='not in D.lower():D+='; charset='+A.charset
			C.append((O,D.encode(Y)))
		A.raw_headers=C
	@property
	def headers(self):
		A=self
		if not hasattr(A,'_headers'):A._headers=J(raw=A.raw_headers)
		return A._headers
	def set_cookie(J,key:F,value:F='',max_age:G|B=B,expires:t|F|G|B=B,path:F|B='/',domain:F|B=B,secure:Q=O,httponly:Q=O,samesite:v[c,n,o]|B=c,partitioned:Q=O):
		I='expires';H=domain;G=max_age;E=samesite;D=expires;C=key;A=http.cookies.SimpleCookie();A[C]=value
		if G is not B:A[C]['max-age']=G
		if D is not B:
			if i(D,t):A[C][I]=È(D,usegmt=M)
			else:A[C][I]=D
		if path is not B:A[C]['path']=path
		if H is not B:A[C]['domain']=H
		if secure:A[C]['secure']=M
		if httponly:A[C]['httponly']=M
		if E is not B:assert E.lower()in[n,c,o],"samesite must be either 'strict', 'lax' or 'none'";A[C]['samesite']=E
		if partitioned:raise l('Partitioned cookies are only supported in Python 3.14 and above.');A[C]['partitioned']=M
		K=A.output(header='').strip();J.raw_headers.append((b'set-cookie',K.encode(Y)))
	def delete_cookie(A,key:F,path:F='/',domain:F|B=B,secure:Q=O,httponly:Q=O,samesite:v[c,n,o]|B=c):A.set_cookie(key,max_age=0,expires=0,path=path,domain=domain,secure=secure,httponly=httponly,samesite=samesite)
	async def __call__(A,scope:Ñ,receive:Ò,send:Send):
		C='websocket.'if scope[I]=='websocket'else'';await send({I:C+f,d:A.status_code,e:A.raw_headers});await send({I:C+R,N:A.body})
		if A.background is not B:await A.background()
class X(C):media_type='text/html'
class K(C):media_type=À
class H(C):
	media_type='application/json'
	def __init__(A,content:g,status_code:G=200,headers:Z[F,F]|B=B,media_type:F|B=B,background:A|B=B):super().__init__(content,status_code,headers,media_type,background)
	def render(A,content:g):return json.dumps(content,ensure_ascii=O,allow_nan=O,indent=B,separators=(',',':')).encode('utf-8')
class P(C):
	def __init__(A,url:F|W,status_code:G=307,headers:Z[F,F]|B=B,background:A|B=B):super().__init__(content=a,status_code=status_code,headers=headers,background=background);A.headers['location']=w(F(url),safe=":/%#?=@[]!$&'()*+,;")
x=F|U|j
Ì=Æ[x]
y=r[x]
Í=y|Ì
class Î(C):
	body_iterator:y
	def __init__(A,content:Í,status_code:G=200,headers:Z[F,F]|B=B,media_type:F|B=B,background:A|B=B):
		D=media_type;C=content
		if i(C,r):A.body_iterator=C
		else:A.body_iterator=Ï(C)
		A.status_code=status_code;A.media_type=A.media_type if D is B else D;A.background=background;A.init_headers(headers)
	async def listen_for_disconnect(B,receive:Ò):
		while M:
			A=await receive()
			if A[I]=='http.disconnect':break
	async def stream_response(A,send:Send):
		C=send;await C({I:f,d:A.status_code,e:A.raw_headers})
		async for B in A.body_iterator:
			if not i(B,U|j):B=B.encode(A.charset)
			await C({I:R,N:B,S:M})
		await C({I:R,N:a,S:O})
	async def __call__(A,scope:Ñ,receive:Ò,send:Send):
		F=T(map(G,scope.get('asgi',{}).get('spec_version','2.0').split('.')))
		if F>=(2,4):
			try:await A.stream_response(send)
			except OSError:raise Ð()
		else:
			with E():
				async with anyio.create_task_group()as C:
					async def D(func:s[[],Å[B]]):await func();C.cancel_scope.cancel()
					C.start_soon(D,u(A.stream_response,send));await D(u(A.listen_for_disconnect,receive))
		if A.background is not B:await A.background()
class b(ª):
	def __init__(A,content:F='Malformed range header.'):A.content=content
class z(ª):
	def __init__(A,max_size:G):A.max_size=max_size
class h(C):
	chunk_size=64*1024
	def __init__(A,path:F|os.PathLike[F],status_code:G=200,headers:Z[F,F]|B=B,media_type:F|B=B,background:A|B=B,filename:F|B=B,stat_result:os.stat_result|B=B,method:F|B=B,content_disposition_type:F='attachment'):
		F=content_disposition_type;E=filename;D=stat_result;C=media_type;A.path=path;A.status_code=status_code;A.filename=E
		if method is not B:Ä.warn("The 'method' parameter is not used, and it will be removed.",DeprecationWarning)
		if C is B:C=Ê(E or path)[0]or À
		A.media_type=C;A.background=background;A.init_headers(headers);A.headers.setdefault('accept-ranges','bytes')
		if A.filename is not B:
			G=w(A.filename)
			if G!=A.filename:H=f"{F}; filename*=utf-8''{G}"
			else:H=f'{F}; filename="{A.filename}"'
			A.headers.setdefault('content-disposition',H)
		A.stat_result=D
		if D is not B:A.set_stat_headers(D)
	def set_stat_headers(B,stat_result:os.stat_result):A=stat_result;C=F(A.st_size);D=É(A.st_mtime,usegmt=M);E=F(A.st_mtime)+k+F(A.st_size);G=f'"{hashlib.md5(E.encode(),usedforsecurity=O).hexdigest()}"';B.headers.setdefault(p,C);B.headers.setdefault(Á,D);B.headers.setdefault('etag',G)
	async def __call__(A,scope:Ñ,receive:Ò,send:Send):
		J=receive;F=send;E=scope;G=E['method'].upper()=='HEAD';P=Â in E.get('extensions',{})
		if A.stat_result is B:
			try:C=await anyio.to_thread.run_sync(os.stat,A.path);A.set_stat_headers(C)
			except FileNotFoundError:raise µ(f"File at path {A.path} does not exist.")
			else:
				R=C.st_mode
				if not stat.S_ISREG(R):raise µ(f"File at path {A.path} is not a file.")
		else:C=A.stat_result
		M=D(scope=E);N=M.get('range');O=M.get('if-range')
		if N is B or O is not B and not A._should_use_range(O):await A._handle_simple(F,G,P)
		else:
			try:H=A._parse_range_header(N,C.st_size)
			except b as I:return await K(I.content,status_code=400)(E,J,F)
			except z as I:S=K(status_code=416,headers={'Content-Range':f"*/{I.max_size}"});return await S(E,J,F)
			if L(H)==1:T,U=H[0];await A._handle_single_range(F,T,U,C.st_size,G)
			else:await A._handle_multiple_ranges(F,H,C.st_size,G)
		if A.background is not B:await A.background()
	async def _handle_simple(A,send:Send,send_header_only:Q,send_pathsend:Q):
		B=send;await B({I:f,d:A.status_code,e:A.raw_headers})
		if send_header_only:await B({I:R,N:a,S:O})
		elif send_pathsend:await B({I:Â,'path':F(A.path)})
		else:
			async with await anyio.open_file(A.path,mode=q)as E:
				C=M
				while C:D=await E.read(A.chunk_size);C=L(D)==A.chunk_size;await B({I:R,N:D,S:C})
	async def _handle_single_range(A,send:Send,start:G,end:G,file_size:G,send_header_only:Q):
		D=send;C=end;B=start;A.headers[Ã]=f"bytes {B}-{C-1}/{file_size}";A.headers[p]=F(C-B);await D({I:f,d:206,e:A.raw_headers})
		if send_header_only:await D({I:R,N:a,S:O})
		else:
			async with await anyio.open_file(A.path,mode=q)as H:
				await H.seek(B);E=M
				while E:G=await H.read(m(A.chunk_size,C-B));B+=L(G);E=L(G)==A.chunk_size and B<C;await D({I:R,N:G,S:E})
	async def _handle_multiple_ranges(A,send:Send,ranges:V[T[G,G]],file_size:G,send_header_only:Q):
		G=ranges;B=send;D=Ë(13);K,P=A.generate_multipart(G,D,file_size,A.headers['content-type']);A.headers[Ã]=f"multipart/byteranges; boundary={D}";A.headers[p]=F(K);await B({I:f,d:206,e:A.raw_headers})
		if send_header_only:await B({I:R,N:a,S:O})
		else:
			async with await anyio.open_file(A.path,mode=q)as H:
				for(C,E)in G:
					await B({I:R,N:P(C,E),S:M});await H.seek(C)
					while C<E:J=await H.read(m(A.chunk_size,E-C));C+=L(J);await B({I:R,N:J,S:M})
					await B({I:R,N:b'\n',S:M})
				await B({I:R,N:f"\n--{D}--\n".encode(Y),S:O})
	def _should_use_range(A,http_if_range:F):B=http_if_range;return B==A.headers[Á]or B==A.headers['etag']
	@º
	def _parse_range_header(cls,http_range:F,file_size:G):
		E=file_size;A=[]
		try:F,K=http_range.split('=',1)
		except l:raise b()
		F=F.strip().lower()
		if F!='bytes':raise b('Only support bytes range')
		A=cls._parse_ranges(K,E)
		if L(A)==0:raise b('Range header: range must be requested')
		if any(not 0<=A<E for(A,B)in A):raise z(E)
		if any(A>B for(A,B)in A):raise b('Range header: start must be less than end')
		if L(A)==1:return A
		B=[]
		for(C,D)in A:
			for H in range(L(B)):
				I,J=B[H]
				if C>J:continue
				elif D<I:B.insert(H,(C,D));break
				else:B[H]=m(C,I),max(D,J);break
			else:B.append((C,D))
		return B
	@º
	def _parse_ranges(cls,range_:F,file_size:G):
		D=file_size;E=[]
		for A in range_.split(','):
			A=A.strip()
			if not A or A==k:continue
			if k not in A:continue
			C,B=A.split(k,1);C=C.strip();B=B.strip()
			try:F=G(C)if C else D-G(B);H=G(B)+1 if C and B and G(B)<D else D;E.append((F,H))
			except l:continue
		return E
	def generate_multipart(H,ranges:Ç[T[G,G]],boundary:F,max_size:G,content_type:F):C=content_type;B=max_size;A=boundary;D=L(A);E=44+D+L(C)+L(F(B));G=sum(L(F(A))+L(F(B-1))+E+(B-A)for(A,B)in ranges)+(5+D);return G,lambda start,end:f"--{A}\nContent-Type: {C}\nContent-Range: bytes {start}-{end-1}/{B}\n\n".encode(Y)