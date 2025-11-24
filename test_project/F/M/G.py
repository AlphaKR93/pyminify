from F.I import W
from F.O import P
from F.V import Ê,Ò,Ñ,Send
class A:
	def __init__(A,app:Ê):A.app=app
	async def __call__(E,scope:Ñ,receive:Ò,send:Send):
		D=receive;C='http';B=scope
		if B['type']in(C,'websocket')and B['scheme']in(C,'ws'):A=W(scope=B);F={C:'https','ws':'wss'}[A.scheme];G=A.hostname if A.port in(80,443)else A.netloc;A=A.replace(scheme=F,netloc=G);H=P(A,status_code=307);await H(B,D,send)
		else:await E.app(B,D,send)