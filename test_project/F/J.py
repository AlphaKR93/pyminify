O='json'
N='HEAD'
M=getattr
J=RuntimeError
I='type'
F='bytes'
E=None
B='text'
import json as L
from typing import Any as H,Literal as Q
from F import status as D
from F.B import G
from F.F import Æ
from F.K import Ú
from F.N import Y
from F.O import K
from F.V import Ì,Ò,Ñ,Send
from F.W import Û
class R:
	def __init__(A,scope:Ñ,receive:Ò,send:Send):B=scope;assert B[I]=='http';A.scope=B;A.receive=receive;A.send=send;A._allowed_methods=[B for B in('GET',N,'POST','PUT','PATCH','DELETE','OPTIONS')if M(A,B.lower(),E)is not E]
	def __await__(A):return A.dispatch().__await__()
	async def dispatch(A):
		B=Y(A.scope,receive=A.receive);E='get'if B.method==N and not hasattr(A,'head')else B.method.lower();C=M(A,E,A.method_not_allowed);F=G(C)
		if F:D=await C(B)
		else:D=await Æ(C,B)
		await D(A.scope,A.receive,A.send)
	async def method_not_allowed(A,request:Y):
		B={'Allow':', '.join(A._allowed_methods)}
		if'app'in A.scope:raise Ú(status_code=405,headers=B)
		return K('Method Not Allowed',status_code=405,headers=B)
class S:
	encoding:Q[B,F,O]|E=E
	def __init__(A,scope:Ñ,receive:Ò,send:Send):B=scope;assert B[I]=='websocket';A.scope=B;A.receive=receive;A.send=send
	def __await__(A):return A.dispatch().__await__()
	async def dispatch(A):
		B=Û(A.scope,receive=A.receive,send=A.send);await A.on_connect(B);E=D.WS_1000_NORMAL_CLOSURE
		try:
			while True:
				C=await B.receive()
				if C[I]=='websocket.receive':F=await A.decode(B,C);await A.on_receive(B,F)
				elif C[I]=='websocket.disconnect':E=int(C.get('code')or D.WS_1000_NORMAL_CLOSURE);break
		except Exception as G:E=D.WS_1011_INTERNAL_ERROR;raise G
		finally:await A.on_disconnect(B,E)
	async def decode(C,websocket:Û,message:Ì):
		G=websocket;A=message
		if C.encoding==B:
			if B not in A:await G.close(code=D.WS_1003_UNSUPPORTED_DATA);raise J('Expected text websocket messages, but got bytes')
			return A[B]
		elif C.encoding==F:
			if F not in A:await G.close(code=D.WS_1003_UNSUPPORTED_DATA);raise J('Expected bytes websocket messages, but got text')
			return A[F]
		elif C.encoding==O:
			if A.get(B)is not E:H=A[B]
			else:H=A[F].decode('utf-8')
			try:return L.loads(H)
			except L.decoder.JSONDecodeError:await G.close(code=D.WS_1003_UNSUPPORTED_DATA);raise J('Malformed JSON data received.')
		assert C.encoding is E,f"Unsupported 'encoding' attribute {C.encoding}";return A[B]if A.get(B)else A[F]
	async def on_connect(A,websocket:Û):await websocket.accept()
	async def on_receive(A,websocket:Û,data:H):0
	async def on_disconnect(A,websocket:Û,close_code:int):0