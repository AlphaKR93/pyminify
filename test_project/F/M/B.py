e='headers'
d='status'
c='http.response.start'
b='http.response.debug'
Z='info'
X=Exception
W=RuntimeError
T=bytes
R='http.response.body'
Q=b''
K='more_body'
J='body'
I='http.disconnect'
G=str
F=True
D=False
B='type'
A=None
from collections.abc import AsyncGenerator as U,AsyncIterable as f,Awaitable as O,Callable as P,Mapping as M,MutableMapping as N
from typing import Any as L,TypeVar as g
import anyio as H
from F.B import E
from F.N import Ð,Y
from F.O import C
from F.V import Ê,Ì,Ò,Ñ,Send
S=P[[Y],O[C]]
h=P[[Y,S],O[C]]
i=U[T|N[G,L],A]
j=f[G|T|memoryview|N[G,L]]
V=g('T')
class k(Y):
	def __init__(A,scope:Ñ,receive:Ò):super().__init__(scope,receive);A._wrapped_rcv_disconnected=D;A._wrapped_rcv_consumed=D;A._wrapped_rc_stream=A.stream()
	async def wrapped_receive(C):
		G='http.request'
		if C._wrapped_rcv_disconnected:return{B:I}
		if C._wrapped_rcv_consumed:
			if C._is_disconnected:C._wrapped_rcv_disconnected=F;return{B:I}
			E=await C.receive()
			if E[B]!=I:raise W(f"Unexpected message received: {E[B]}")
			C._wrapped_rcv_disconnected=F;return E
		if getattr(C,'_body',A)is not A:C._wrapped_rcv_consumed=F;return{B:G,J:C._body,K:D}
		elif C._stream_consumed:C._wrapped_rcv_consumed=F;return{B:G,J:Q,K:D}
		else:
			try:H=C.stream();L=await H.__anext__();C._wrapped_rcv_consumed=C._stream_consumed;return{B:G,J:L,K:not C._stream_consumed}
			except Ð:C._wrapped_rcv_disconnected=F;return{B:I}
class a:
	def __init__(B,app:Ê,dispatch:h|A=A):C=dispatch;B.app=app;B.dispatch_func=B.dispatch if C is A else C
	async def __call__(S,scope:Ñ,receive:Ò,send:Send):
		a=receive;L=scope
		if L[B]!='http':await S.app(L,a,send);return
		f=k(L,a);g=f.wrapped_receive;N=H.Event();G=A;T=D
		async def h(request:Y):
			async def a():
				if N.is_set():return{B:I}
				async with H.create_task_group()as A:
					async def C(func:P[[],O[V]]):B=await func();A.cancel_scope.cancel();return B
					A.start_soon(C,N.wait);D=await C(g)
				if N.is_set():return{B:I}
				return D
			async def f(message:Ì):
				try:await U.send(message)
				except H.BrokenResourceError:return
			async def h():
				nonlocal G
				with U:
					try:await S.app(L,a,f)
					except X as A:G=A
			m.start_soon(h)
			try:
				C=await M.receive();E=C.get(Z,A)
				if C[B]==b and E is not A:C=await M.receive()
			except H.EndOfStream:
				if G is not A:nonlocal T;T=F;raise G from G.__cause__ or G.__context__
				raise W('No response returned.')
			assert C[B]==c
			async def j():
				async for A in M:
					if A[B]=='http.response.pathsend':yield A;break
					assert A[B]==R,f"Unexpected message: {A}";C=A.get(J,Q)
					if C:yield C
					if not A.get(K,D):break
			Y=l(status_code=C[d],content=j(),info=E);Y.raw_headers=C[e];return Y
		j=H.create_memory_object_stream();U,M=j
		with M,U,E():
			async with H.create_task_group()as m:n=await S.dispatch_func(f,h);await n(L,g,send);N.set();M.close()
		if G is not A and not T:raise G
	async def dispatch(A,request:Y,call_next:S):raise NotImplementedError
class l(C):
	def __init__(B,content:j,status_code:int=200,headers:M[G,G]|A=A,media_type:G|A=A,info:M[G,L]|A=A):B.info=info;B.body_iterator=content;B.status_code=status_code;B.media_type=media_type;B.init_headers(headers);B.background=A
	async def __call__(C,scope:Ñ,receive:Ò,send:Send):
		E=send
		if C.info is not A:await E({B:b,Z:C.info})
		await E({B:c,d:C.status_code,e:C.raw_headers});H=F
		async for G in C.body_iterator:
			if isinstance(G,dict):H=D;await E(G);continue
			await E({B:R,J:G,K:F})
		if H:await E({B:R,J:Q,K:D})
		if C.background:await C.background()