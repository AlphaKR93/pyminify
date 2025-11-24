a='utf-8'
Z='The "mode" argument should be "text" or "binary".'
Y='binary'
X=False
W='websocket.accept'
T=True
S='WebSocket is not connected. Need to call "accept" first.'
R='reason'
Q='code'
P='websocket.disconnect'
O=int
L='bytes'
K='websocket.send'
J='websocket.close'
I=bytes
H='text'
G=None
F=str
D=RuntimeError
B='type'
import enum,json as U
from collections.abc import Iterable as b
from typing import Any as N,cast as V
from F.N import E
from F.O import C
from F.V import Ì,Ò,Ñ,Send
class A(enum.Enum):CONNECTING=0;CONNECTED=1;DISCONNECTED=2;RESPONSE=3
class Ë(Exception):
	def __init__(A,code:O=1000,reason:F|G=G):A.code=code;A.reason=reason or''
class Û(E):
	def __init__(C,scope:Ñ,receive:Ò,send:Send):D=scope;super().__init__(D);assert D[B]=='websocket';C._receive=receive;C._send=send;C.client_state=A.CONNECTING;C.application_state=A.CONNECTING
	async def receive(C):
		if C.client_state==A.CONNECTING:
			F=await C._receive();E=F[B]
			if E!='websocket.connect':raise D(f'Expected ASGI message "websocket.connect", but got {E!r}')
			C.client_state=A.CONNECTED;return F
		elif C.client_state==A.CONNECTED:
			F=await C._receive();E=F[B]
			if E not in{'websocket.receive',P}:raise D(f'Expected ASGI message "websocket.receive" or "websocket.disconnect", but got {E!r}')
			if E==P:C.client_state=A.DISCONNECTED
			return F
		else:raise D('Cannot call "receive" once a disconnect message has been received.')
	async def send(C,message:Ì):
		G='websocket.http.response.start';F=message
		if C.application_state==A.CONNECTING:
			E=F[B]
			if E not in{W,J,G}:raise D(f'Expected ASGI message "websocket.accept", "websocket.close" or "websocket.http.response.start", but got {E!r}')
			if E==J:C.application_state=A.DISCONNECTED
			elif E==G:C.application_state=A.RESPONSE
			else:C.application_state=A.CONNECTED
			await C._send(F)
		elif C.application_state==A.CONNECTED:
			E=F[B]
			if E not in{K,J}:raise D(f'Expected ASGI message "websocket.send" or "websocket.close", but got {E!r}')
			if E==J:C.application_state=A.DISCONNECTED
			try:await C._send(F)
			except OSError:C.application_state=A.DISCONNECTED;raise Ë(code=1006)
		elif C.application_state==A.RESPONSE:
			E=F[B]
			if E!='websocket.http.response.body':raise D(f'Expected ASGI message "websocket.http.response.body", but got {E!r}')
			if not F.get('more_body',X):C.application_state=A.DISCONNECTED
			await C._send(F)
		else:raise D('Cannot call "send" once a close message has been sent.')
	async def accept(C,subprotocol:F|G=G,headers:b[tuple[I,I]]|G=G):
		D=headers;D=D or[]
		if C.client_state==A.CONNECTING:await C.receive()
		await C.send({B:W,'subprotocol':subprotocol,'headers':D})
	def _raise_on_disconnect(C,message:Ì):
		A=message
		if A[B]==P:raise Ë(A[Q],A.get(R))
	async def receive_text(B):
		if B.application_state!=A.CONNECTED:raise D(S)
		C=await B.receive();B._raise_on_disconnect(C);return C[H]
	async def receive_bytes(B):
		if B.application_state!=A.CONNECTED:raise D(S)
		C=await B.receive();B._raise_on_disconnect(C);return C[L]
	async def receive_json(B,mode:F=H):
		if mode not in{H,Y}:raise D(Z)
		if B.application_state!=A.CONNECTED:raise D(S)
		C=await B.receive();B._raise_on_disconnect(C)
		if mode==H:E=C[H]
		else:E=C[L].decode(a)
		return U.loads(E)
	async def iter_text(A):
		try:
			while T:yield await A.receive_text()
		except Ë:pass
	async def iter_bytes(A):
		try:
			while T:yield await A.receive_bytes()
		except Ë:pass
	async def iter_json(A):
		try:
			while T:yield await A.receive_json()
		except Ë:pass
	async def send_text(A,data:F):await A.send({B:K,H:data})
	async def send_bytes(A,data:I):await A.send({B:K,L:data})
	async def send_json(A,data:N,mode:F=H):
		if mode not in{H,Y}:raise D(Z)
		C=U.dumps(data,separators=(',',':'),ensure_ascii=X)
		if mode==H:await A.send({B:K,H:C})
		else:await A.send({B:K,L:C.encode(a)})
	async def close(A,code:O=1000,reason:F|G=G):await A.send({B:J,Q:code,R:reason or''})
	async def send_denial_response(A,response:C):
		if'websocket.http.response'in A.scope.get('extensions',{}):await response(A.scope,A.receive,A.send)
		else:raise D("The server doesn't support the Websocket Denial Response extension.")
class Ü:
	def __init__(A,code:O=1000,reason:F|G=G):A.code=code;A.reason=reason or''
	async def __call__(A,scope:Ñ,receive:Ò,send:Send):await send({B:J,Q:A.code,R:A.reason})