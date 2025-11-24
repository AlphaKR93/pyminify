H=None
G=isinstance
F=Exception
from collections.abc import Mapping as I
from typing import Any
from F.A import Ý
from F.K import Ú,D
from F.N import Y
from F.O import K,C
from F.V import Ê,A,Ò,Ñ,Send
from F.W import Û
class W:
	def __init__(A,app:Ê,handlers:I[Any,A]|H=H,debug:bool=False):
		C=handlers;A.app=app;A.debug=debug;A._status_handlers={};A._exception_handlers={Ú:A.http_exception,D:A.websocket_exception}
		if C is not H:
			for(F,G)in C.items():A.add_exception_handler(F,G)
	def add_exception_handler(B,exc_class_or_status_code:int|type[F],handler:A):
		C=handler;A=exc_class_or_status_code
		if G(A,int):B._status_handlers[A]=C
		else:assert issubclass(A,F);B._exception_handlers[A]=C
	async def __call__(B,scope:Ñ,receive:Ò,send:Send):
		G='http';F='type';D=send;C=receive;A=scope
		if A[F]not in(G,'websocket'):await B.app(A,C,D);return
		A['starlette.exception_handlers']=B._exception_handlers,B._status_handlers
		if A[F]==G:E=Y(A,C,D)
		else:E=Û(A,C,D)
		await Ý(B.app,E)(A,C,D)
	async def http_exception(B,request:Y,exc:F):
		A=exc;assert G(A,Ú)
		if A.status_code in{204,304}:return C(status_code=A.status_code,headers=A.headers)
		return K(A.detail,status_code=A.status_code,headers=A.headers)
	async def websocket_exception(B,websocket:Û,exc:F):A=exc;assert G(A,D);await websocket.close(code=A.code,reason=A.reason)