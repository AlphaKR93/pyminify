x='testclient'
w='asyncio'
v='sec-websocket-protocol'
u='binary'
t='status'
s='reason'
r='code'
q=RuntimeError
h='state'
g=':'
f='more_body'
e=isinstance
d=list
Y='utf-8'
U='bytes'
T='websocket.receive'
X=b''
W=tuple
Q='body'
P=int
M=False
L=True
K='headers'
J='text'
I=bytes
H=bool
F=dict
E='type'
C=str
A=None
import contextlib as Z,inspect as y,io,json as i,math as N,warnings as z
from collections.abc import Awaitable as j,Callable as O,Iterable as µ,Mapping,Sequence as l
from concurrent.futures import Future
from contextlib import AbstractContextManager as º
from types import GeneratorType as Æ
from typing import Any as D,Literal as a,TypedDict as À,cast as b
from urllib.parse import unquote as m,urljoin
import anyio,anyio.abc,anyio.from_thread
from anyio.streams.stapled import StapledObjectStream as n
from F.B import G
from F.V import Ê,Ì,Ò,Ñ,Send
from F.W import Ë
try:import httpx as B
except ModuleNotFoundError:raise q('The starlette.testclient module requires the httpx package to be installed.\nYou can install this with:\n    $ pip install httpx\n')
o=O[[],º[anyio.abc.BlockingPortal]]
Â=O[[Ò,Send],j[A]]
c=O[[Ñ],Â]
R=O[[Ñ,Ò,Send],j[A]]
S=Mapping[C,C|µ[C]|I]
def Ã(app:c|R):
	A=app
	if y.isclass(A):return hasattr(A,'__await__')
	return G(A)
class Ä:
	def __init__(A,app:c):A.app=app
	async def __call__(A,scope:Ñ,receive:Ò,send:Send):B=A.app(scope);await B(receive,send)
class Å(À):backend:C;backend_options:F[C,D]
class p(Exception):
	def __init__(A,session:V):A.session=session
class Ç(B.Response,Ë):0
class V:
	def __init__(B,app:R,scope:Ñ,portal_factory:o):B.app=app;B.scope=scope;B.accepted_subprotocol=A;B.portal_factory=portal_factory;B.extra_headers=A
	def __enter__(B):
		with Z.ExitStack()as C:B.portal=F=C.enter_context(B.portal_factory());G,H=F.start_task(B._run);C.callback(G.result);C.callback(F.call,H.cancel);B.send({E:'websocket.connect'});D=B.receive();B._raise_on_close(D);B.accepted_subprotocol=D.get('subprotocol',A);B.extra_headers=D.get(K,A);C.callback(B.close,1000);B.exit_stack=C.pop_all();return B
	def __exit__(A,*B:D):return A.exit_stack.__exit__(*B)
	async def _run(A,*,task_status:anyio.abc.TaskStatus[anyio.CancelScope]):
		F=anyio.create_memory_object_stream(N.inf);B,C=F;G=anyio.create_memory_object_stream(N.inf);D,E=G
		with B,C,D,E,anyio.CancelScope()as H:A._receive_tx=D;A._send_rx=C;task_status.started(H);await A.app(A.scope,E.receive,B.send);await anyio.sleep_forever()
	def _raise_on_close(C,message:Ì):
		A=message
		if A[E]=='websocket.close':raise Ë(code=A.get(r,1000),reason=A.get(s,''))
		elif A[E]=='websocket.http.response.start':
			D=A[t];F=A[K];B=[]
			while L:
				A=C.receive();assert A[E]=='websocket.http.response.body';B.append(A[Q])
				if not A.get(f,M):break
			raise Ç(status_code=D,headers=F,content=X.join(B))
	def send(A,message:Ì):A.portal.call(A._receive_tx.send,message)
	def send_text(A,data:C):A.send({E:T,J:data})
	def send_bytes(A,data:I):A.send({E:T,U:data})
	def send_json(A,data:D,mode:a[J,u]=J):
		B=i.dumps(data,separators=(',',g),ensure_ascii=M)
		if mode==J:A.send({E:T,J:B})
		else:A.send({E:T,U:B.encode(Y)})
	def close(A,code:P=1000,reason:C|A=A):A.send({E:'websocket.disconnect',r:code,s:reason})
	def receive(A):return A.portal.call(A._send_rx.receive)
	def receive_text(A):B=A.receive();A._raise_on_close(B);return B[J]
	def receive_bytes(A):B=A.receive();A._raise_on_close(B);return B[U]
	def receive_json(B,mode:a[J,u]=J):
		A=B.receive();B._raise_on_close(A)
		if mode==J:C=A[J]
		else:C=A[U].decode(Y)
		return i.loads(C)
class È(B.BaseTransport):
	def __init__(A,app:R,portal_factory:o,raise_server_exceptions:H=L,root_path:C='',*,client:W[C,P],app_state:F[C,D]):A.app=app;A.raise_server_exceptions=raise_server_exceptions;A.root_path=root_path;A.portal_factory=portal_factory;A.app_state=app_state;A.client=client
	def handle_request(G,request:B.Request):
		Å='status_code';Ä='http.response.debug';Ã='extensions';Â='server';Á='client';À='query_string';º='scheme';µ='root_path';ª='raw_path';z='wss';y='http';x='ascii';O='stream';H=request;Z=H.url.scheme;i=H.url.netloc.decode(encoding=x);n=H.url.path;o=H.url.raw_path;q=H.url.query.decode(encoding=x);r={y:80,'ws':80,'https':443,z:443}[Z]
		if g in i:R,Ç=i.split(g,1);S=P(Ç)
		else:R=i;S=r
		if'host'in H.headers:T=[]
		elif S==r:T=[(b'host',R.encode())]
		else:T=[(b'host',f"{R}:{S}".encode())]
		T+=[(A.lower().encode(),B.encode())for(A,B)in H.headers.multi_items()]
		if Z in{'ws',z}:
			s=H.headers.get(v,A)
			if s is A:u=[]
			else:u=[A.strip()for A in s.split(',')]
			a={E:'websocket','path':m(n),ª:o.split(b'?',1)[0],µ:G.root_path,º:Z,À:q.encode(),K:T,Á:G.client,Â:[R,S],'subprotocols':u,h:G.app_state.copy(),Ã:{'websocket.http.response':{}}};È=V(G.app,a,G.portal_factory);raise p(È)
		a={E:y,'http_version':'1.1','method':H.method,'path':m(n),ª:o.split(b'?',1)[0],µ:G.root_path,º:Z,À:q.encode(),K:T,Á:G.client,Â:[R,S],Ã:{Ä:{}},h:G.app_state.copy()};b=M;N=M;J={O:io.BytesIO()};c=A;j=A
		async def É():
			G='http.request';nonlocal b
			if b:
				if not U.is_set():await U.wait()
				return{E:'http.disconnect'}
			B=H.read()
			if e(B,C):F=B.encode(Y)
			elif B is A:F=X
			elif e(B,Æ):
				try:
					D=B.send(A)
					if e(D,C):D=D.encode(Y)
					return{E:G,Q:D,f:L}
				except StopIteration:b=L;return{E:G,Q:X}
			else:F=B
			b=L;return{E:G,Q:F}
		async def Ê(message:Ì):
			B='info';A=message;nonlocal J,N,c,j
			if A[E]=='http.response.start':assert not N,'Received multiple "http.response.start" messages.';J[Å]=A[t];J[K]=[(A.decode(),B.decode())for(A,B)in A.get(K,[])];N=L
			elif A[E]=='http.response.body':
				assert N,'Received "http.response.body" without "http.response.start".';assert not U.is_set(),'Received "http.response.body" after response completed.';C=A.get(Q,X);D=A.get(f,M)
				if H.method!='HEAD':J[O].write(C)
				if not D:J[O].seek(0);U.set()
			elif A[E]==Ä:c=A[B]['template'];j=A[B]['context']
		try:
			with G.portal_factory()as w:U=w.call(anyio.Event);w.call(G.app,a,É,Ê)
		except BaseException as Ë:
			if G.raise_server_exceptions:raise Ë
		if G.raise_server_exceptions:assert N,'TestClient did not receive any response.'
		elif not N:J={Å:500,K:[],O:io.BytesIO()}
		J[O]=B.ByteStream(J[O].read());k=B.Response(**J,request=H)
		if c is not A:k.template=c;k.context=j
		return k
class É(B.Client):
	__test__=M;task:Future[A];portal:anyio.abc.BlockingPortal|A=A
	def __init__(B,app:Ê,base_url:C='http://testserver',raise_server_exceptions:H=L,root_path:C='',backend:a[w,'trio']=w,backend_options:F[C,D]|A=A,cookies:B._types.CookieTypes|A=A,headers:F[C,C]|A=A,follow_redirects:H=L,client:W[C,P]=(x,50000)):
		G=headers;E=app;B.async_backend=Å(backend=backend,backend_options=backend_options or{})
		if Ã(E):H=E
		else:E=E;H=Ä(E)
		B.app=H;B.app_state={};I=È(B.app,portal_factory=B._portal_factory,raise_server_exceptions=raise_server_exceptions,root_path=root_path,app_state=B.app_state,client=client)
		if G is A:G={}
		G.setdefault('user-agent',x);super().__init__(base_url=base_url,headers=G,transport=I,follow_redirects=follow_redirects,cookies=cookies)
	@Z.contextmanager
	def _portal_factory(self):
		B=self
		if B.portal is not A:yield B.portal
		else:
			with anyio.from_thread.start_blocking_portal(**B.async_backend)as C:yield C
	def request(D,method:C,url:B._types.URLTypes,*,content:B._types.RequestContent|A=A,data:S|A=A,files:B._types.RequestFiles|A=A,json:D=A,params:B._types.QueryParamTypes|A=A,headers:B._types.HeaderTypes|A=A,cookies:B._types.CookieTypes|A=A,auth:B._types.AuthTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,follow_redirects:H|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,timeout:B._types.TimeoutTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,extensions:F[C,D]|A=A):
		C=timeout;A=url
		if C is not B.USE_CLIENT_DEFAULT:z.warn("You should not use the 'timeout' argument with the TestClient. See https://github.com/Kludex/starlette/issues/1108 for more information.",DeprecationWarning)
		A=D._merge_url(A);return super().request(method,A,content=content,data=data,files=files,json=json,params=params,headers=headers,cookies=cookies,auth=auth,follow_redirects=follow_redirects,timeout=C,extensions=extensions)
	def get(A,url:B._types.URLTypes,*,params:B._types.QueryParamTypes|A=A,headers:B._types.HeaderTypes|A=A,cookies:B._types.CookieTypes|A=A,auth:B._types.AuthTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,follow_redirects:H|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,timeout:B._types.TimeoutTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,extensions:F[C,D]|A=A):return super().get(url,params=params,headers=headers,cookies=cookies,auth=auth,follow_redirects=follow_redirects,timeout=timeout,extensions=extensions)
	def options(A,url:B._types.URLTypes,*,params:B._types.QueryParamTypes|A=A,headers:B._types.HeaderTypes|A=A,cookies:B._types.CookieTypes|A=A,auth:B._types.AuthTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,follow_redirects:H|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,timeout:B._types.TimeoutTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,extensions:F[C,D]|A=A):return super().options(url,params=params,headers=headers,cookies=cookies,auth=auth,follow_redirects=follow_redirects,timeout=timeout,extensions=extensions)
	def head(A,url:B._types.URLTypes,*,params:B._types.QueryParamTypes|A=A,headers:B._types.HeaderTypes|A=A,cookies:B._types.CookieTypes|A=A,auth:B._types.AuthTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,follow_redirects:H|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,timeout:B._types.TimeoutTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,extensions:F[C,D]|A=A):return super().head(url,params=params,headers=headers,cookies=cookies,auth=auth,follow_redirects=follow_redirects,timeout=timeout,extensions=extensions)
	def post(A,url:B._types.URLTypes,*,content:B._types.RequestContent|A=A,data:S|A=A,files:B._types.RequestFiles|A=A,json:D=A,params:B._types.QueryParamTypes|A=A,headers:B._types.HeaderTypes|A=A,cookies:B._types.CookieTypes|A=A,auth:B._types.AuthTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,follow_redirects:H|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,timeout:B._types.TimeoutTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,extensions:F[C,D]|A=A):return super().post(url,content=content,data=data,files=files,json=json,params=params,headers=headers,cookies=cookies,auth=auth,follow_redirects=follow_redirects,timeout=timeout,extensions=extensions)
	def put(A,url:B._types.URLTypes,*,content:B._types.RequestContent|A=A,data:S|A=A,files:B._types.RequestFiles|A=A,json:D=A,params:B._types.QueryParamTypes|A=A,headers:B._types.HeaderTypes|A=A,cookies:B._types.CookieTypes|A=A,auth:B._types.AuthTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,follow_redirects:H|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,timeout:B._types.TimeoutTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,extensions:F[C,D]|A=A):return super().put(url,content=content,data=data,files=files,json=json,params=params,headers=headers,cookies=cookies,auth=auth,follow_redirects=follow_redirects,timeout=timeout,extensions=extensions)
	def patch(A,url:B._types.URLTypes,*,content:B._types.RequestContent|A=A,data:S|A=A,files:B._types.RequestFiles|A=A,json:D=A,params:B._types.QueryParamTypes|A=A,headers:B._types.HeaderTypes|A=A,cookies:B._types.CookieTypes|A=A,auth:B._types.AuthTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,follow_redirects:H|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,timeout:B._types.TimeoutTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,extensions:F[C,D]|A=A):return super().patch(url,content=content,data=data,files=files,json=json,params=params,headers=headers,cookies=cookies,auth=auth,follow_redirects=follow_redirects,timeout=timeout,extensions=extensions)
	def delete(A,url:B._types.URLTypes,*,params:B._types.QueryParamTypes|A=A,headers:B._types.HeaderTypes|A=A,cookies:B._types.CookieTypes|A=A,auth:B._types.AuthTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,follow_redirects:H|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,timeout:B._types.TimeoutTypes|B._client.UseClientDefault=B._client.USE_CLIENT_DEFAULT,extensions:F[C,D]|A=A):return super().delete(url,params=params,headers=headers,cookies=cookies,auth=auth,follow_redirects=follow_redirects,timeout=timeout,extensions=extensions)
	def websocket_connect(I,url:C,subprotocols:l[C]|A=A,**E:D):
		F=subprotocols;C=url;C=urljoin('ws://testserver',C);B=E.get(K,{});B.setdefault('connection','upgrade');B.setdefault('sec-websocket-key','testserver==');B.setdefault('sec-websocket-version','13')
		if F is not A:B.setdefault(v,', '.join(F))
		E[K]=B
		try:super().request('GET',C,**E)
		except p as G:H=G.session
		else:raise q('Expected WebSocket upgrade')
		return H
	def __enter__(B):
		with Z.ExitStack()as E:
			B.portal=F=E.enter_context(anyio.from_thread.start_blocking_portal(**B.async_backend))
			@E.callback
			def J():B.portal=A
			G=anyio.create_memory_object_stream(N.inf);H=anyio.create_memory_object_stream(N.inf)
			for I in(*G,*H):E.callback(I.close)
			B.stream_send=n(*G);B.stream_receive=n(*H);B.task=F.start_task_soon(B.lifespan);F.call(B.wait_startup)
			@E.callback
			def K():F.call(B.wait_shutdown)
			B.exit_stack=E.pop_all()
		return B
	def __exit__(A,*B:D):A.exit_stack.close()
	async def lifespan(B):
		C={E:'lifespan',h:B.app_state}
		try:await B.app(C,B.stream_receive.receive,B.stream_send.send)
		finally:await B.stream_send.send(A)
	async def wait_startup(B):
		G='lifespan.startup.failed';await B.stream_receive.send({E:'lifespan.startup'})
		async def C():
			C=await B.stream_send.receive()
			if C is A:B.task.result()
			return C
		F=await C();assert F[E]in('lifespan.startup.complete',G)
		if F[E]==G:await C()
	async def wait_shutdown(B):
		G='lifespan.shutdown.failed'
		async def C():
			C=await B.stream_send.receive()
			if C is A:B.task.result()
			return C
		await B.stream_receive.send({E:'lifespan.shutdown'});F=await C();assert F[E]in('lifespan.shutdown.complete',G)
		if F[E]==G:await C()