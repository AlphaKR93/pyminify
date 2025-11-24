O='more_body'
N='headers'
M='http'
K='body'
H=b''
J=False
I='ascii'
F='type'
E=None
D=True
B=str
import io,math,sys,warnings as P
from collections.abc import Callable as G,MutableMapping as L
from typing import Any as A
import anyio as C
from anyio.abc import ObjectReceiveStream as Q,ObjectSendStream as R
from F.V import Ò,Ñ,Send
P.warn('starlette.middleware.wsgi is deprecated and will be removed in a future release. Please refer to https://github.com/abersheeran/a2wsgi as a replacement.',DeprecationWarning)
def S(scope:Ñ,body:bytes):
	P='client';O='utf8';H='latin1';A=scope;K=A.get('root_path','').encode(O).decode(H);G=A['path'].encode(O).decode(H)
	if G.startswith(K):G=G[len(K):]
	B={'REQUEST_METHOD':A['method'],'SCRIPT_NAME':K,'PATH_INFO':G,'QUERY_STRING':A['query_string'].decode(I),'SERVER_PROTOCOL':f"HTTP/{A["http_version"]}",'wsgi.version':(1,0),'wsgi.url_scheme':A.get('scheme',M),'wsgi.input':io.BytesIO(body),'wsgi.errors':sys.stdout,'wsgi.multithread':D,'wsgi.multiprocess':D,'wsgi.run_once':J};L=A.get('server')or('localhost',80);B['SERVER_NAME']=L[0];B['SERVER_PORT']=L[1]
	if A.get(P):B['REMOTE_ADDR']=A[P][0]
	for(C,E)in A.get(N,[]):
		C=C.decode(H)
		if C=='content-length':F='CONTENT_LENGTH'
		elif C=='content-type':F='CONTENT_TYPE'
		else:F=f"HTTP_{C}".upper().replace('-','_')
		E=E.decode(H)
		if F in B:E=B[F]+','+E
		B[F]=E
	return B
class T:
	def __init__(A,app:G[...,A]):A.app=app
	async def __call__(B,scope:Ñ,receive:Ò,send:Send):A=scope;assert A[F]==M;C=U(B.app,A);await C(receive,send)
class U:
	stream_send:R[L[B,A]];stream_receive:Q[L[B,A]]
	def __init__(B,app:G[...,A],scope:Ñ):B.app=app;B.scope=scope;B.status=E;B.response_headers=E;B.stream_send,B.stream_receive=C.create_memory_object_stream(math.inf);B.response_started=J;B.exc_info=E
	async def __call__(A,receive:Ò,send:Send):
		B=H;F=D
		while F:G=await receive();B+=G.get(K,H);F=G.get(O,J)
		I=S(A.scope,B)
		async with C.create_task_group()as L:
			L.start_soon(A.sender,send)
			async with A.stream_send:await C.to_thread.run_sync(A.wsgi,I,A.start_response)
		if A.exc_info is not E:raise A.exc_info[0].with_traceback(A.exc_info[1],A.exc_info[2])
	async def sender(A,send:Send):
		async with A.stream_receive:
			async for B in A.stream_receive:await send(B)
	def start_response(A,status:B,response_headers:list[tuple[B,B]],exc_info:A=E):
		A.exc_info=exc_info
		if not A.response_started:A.response_started=D;B,H=status.split(' ',1);E=int(B);G=[(A.strip().encode(I).lower(),B.strip().encode(I))for(A,B)in response_headers];C.from_thread.run(A.stream_send.send,{F:'http.response.start','status':E,N:G})
	def wsgi(A,environ:dict[B,A],start_response:G[...,A]):
		B='http.response.body'
		for E in A.app(environ,start_response):C.from_thread.run(A.stream_send.send,{F:B,K:E,O:D})
		C.from_thread.run(A.stream_send.send,{F:B,K:H})