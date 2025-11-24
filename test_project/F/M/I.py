G=True
E=None
A='*'
from collections.abc import Sequence as B
from F.I import W,D
from F.O import K,P
from F.V import Ê,Ò,Ñ,Send
F="Domain wildcard patterns must be like '*.example.com'."
class H:
	def __init__(C,app:Ê,allowed_hosts:B[str]|E=E,www_redirect:bool=G):
		B=allowed_hosts
		if B is E:B=[A]
		for D in B:
			assert A not in D[1:],F
			if D.startswith(A)and D!=A:assert D.startswith('*.'),F
		C.app=app;C.allowed_hosts=list(B);C.allow_any=A in B;C.www_redirect=www_redirect
	async def __call__(E,scope:Ñ,receive:Ò,send:Send):
		R='www.';Q=False;I=send;H=receive;B=scope
		if E.allow_any or B['type']not in('http','websocket'):await E.app(B,H,I);return
		S=D(scope=B);J=S.get('host','').split(':')[0];M=Q;N=Q
		for F in E.allowed_hosts:
			if J==F or F.startswith(A)and J.endswith(F[1:]):M=G;break
			elif R+J==F:N=G
		if M:await E.app(B,H,I)
		else:
			if N and E.www_redirect:O=W(scope=B);T=O.replace(netloc=R+O.netloc);L=P(url=str(T))
			else:L=K('Invalid host header',status_code=400)
			await L(B,H,I)