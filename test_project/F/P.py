Ë='routes'
É='method'
È='Not Found'
Ç=property
Â='app'
Á="Routed paths must start with '/'"
À=BaseException
º=NotImplementedError
µ=getattr
z='endpoint'
y=reversed
x=len
t=True
s=':'
r=set
j='websocket'
i='http'
h=tuple
g=DeprecationWarning
f=list
c='path_params'
b=''
a=isinstance
T=bool
S='path'
R='/'
Q=dict
O='type'
J=str
H=None
import contextlib as Ì,functools as m,inspect as d,re as n,traceback as Í,types,warnings as V
from collections.abc import Awaitable as o,Callable as N,Collection as ª,Generator as Î,Sequence as X
from contextlib import AbstractAsyncContextManager as Ã,AbstractContextManager as Ï,asynccontextmanager as Ð
from enum import Enum
from typing import Any as L,TypeVar
from F.A import Ý
from F.B import A,G
from F.F import Æ
from F.H import F,E
from F.I import W,D,I
from F.K import Ú
from F.M import Þ
from F.N import Y
from F.O import K,P,C
from F.V import Ê,B,Ò,Ñ,Send
from F.W import Û,Ü
class Z(Exception):
	def __init__(B,name:J,path_params:Q[J,L]):A=', '.join(f(path_params.keys()));super().__init__(f'No route exists for name "{name}" and params "{A}".')
class M(Enum):NONE=0;PARTIAL=1;FULL=2
def Ù(obj:L):
	A=obj;V.warn('iscoroutinefunction_or_partial is deprecated, and will be removed in a future release.',g)
	while a(A,m.partial):A=A.func
	return d.iscoroutinefunction(A)
def Ó(func:N[[Y],o[C]|C]):
	A=func;D=A if G(A)else m.partial(Æ,A)
	async def B(scope:Ñ,receive:Ò,send:Send):
		B=receive;A=scope;C=Y(A,B,send)
		async def E(scope:Ñ,receive:Ò,send:Send):A=await D(C);await A(scope,receive,send)
		await Ý(E,C)(A,B,send)
	return B
def Ô(func:N[[Û],o[H]]):
	async def A(scope:Ñ,receive:Ò,send:Send):
		B=receive;A=scope;C=Û(A,receive=B,send=send)
		async def D(scope:Ñ,receive:Ò,send:Send):await func(C)
		await Ý(D,C)(A,B,send)
	return A
def p(endpoint:N[...,L]):A=endpoint;return µ(A,'__name__',A.__class__.__name__)
def k(path:J,param_convertors:Q[J,E[L]],path_params:Q[J,J]):
	C=path_params;A=path
	for(B,D)in f(C.items()):
		if'{'+B+'}'in A:E=param_convertors[B];D=E.to_string(D);A=A.replace('{'+B+'}',D);C.pop(B)
	return A,C
Õ=n.compile('{([a-zA-Z_][a-zA-Z0-9_]*)(:[a-zA-Z_][a-zA-Z0-9_]*)?}')
def e(path:J):
	A=path;L=not A.startswith(R);C='^';G=b;H=r();B=0;J={}
	for I in Õ.finditer(A):
		D,E=I.groups('str');E=E.lstrip(s);assert E in F,f"Unknown path convertor '{E}'";K=F[E];C+=n.escape(A[B:I.start()]);C+=f"(?P<{D}>{K.regex})";G+=A[B:I.start()];G+='{%s}'%D
		if D in J:H.add(D)
		J[D]=K;B=I.end()
	if H:M=', '.join(sorted(H));N='s'if x(H)>1 else b;raise ValueError(f"Duplicated param name{N} {M} at path {A}")
	if L:O=A[B:].split(s)[0];C+=n.escape(O)+'$'
	else:C+=n.escape(A[B:])+'$'
	G+=A[B:];return n.compile(C),G,J
class U:
	def matches(A,scope:Ñ):raise º
	def url_path_for(A,B:J,**C:L):raise º
	async def handle(A,scope:Ñ,receive:Ò,send:Send):raise º
	async def __call__(D,scope:Ñ,receive:Ò,send:Send):
		C=send;B=receive;A=scope;E,F=D.matches(A)
		if E==M.NONE:
			if A[O]==i:G=K(È,status_code=404);await G(A,B,C)
			elif A[O]==j:H=Ü();await H(A,B,C)
			return
		A.update(F);await D.handle(A,B,C)
class u(U):
	def __init__(A,path:J,endpoint:N[...,L],*,methods:ª[J]|H=H,name:J|H=H,include_in_schema:T=t,middleware:X[Þ]|H=H):
		G='GET';F=middleware;E=path;D=methods;B=endpoint;assert E.startswith(R),Á;A.path=E;A.endpoint=B;A.name=p(B)if name is H else name;A.include_in_schema=include_in_schema;C=B
		while a(C,m.partial):C=C.func
		if d.isfunction(C)or d.ismethod(C):
			A.app=Ó(B)
			if D is H:D=[G]
		else:A.app=B
		if F is not H:
			for(I,J,K)in y(F):A.app=I(A.app,*J,**K)
		if D is H:A.methods=H
		else:
			A.methods={A.upper()for A in D}
			if G in A.methods:A.methods.add('HEAD')
		A.path_regex,A.path_format,A.param_convertors=e(E)
	def matches(B,scope:Ñ):
		C=scope
		if C[O]==i:
			I=A(C);F=B.path_regex.match(I)
			if F:
				E=F.groupdict()
				for(G,K)in E.items():E[G]=B.param_convertors[G].convert(K)
				D=Q(C.get(c,{}));D.update(E);H={z:B.endpoint,c:D}
				if B.methods and C[É]not in B.methods:return M.PARTIAL,H
				else:return M.FULL,H
		return M.NONE,{}
	def url_path_for(A,C:J,**B:L):
		D=r(B.keys());E=r(A.param_convertors.keys())
		if C!=A.name or D!=E:raise Z(C,B)
		F,G=k(A.path_format,A.param_convertors,B);assert not G;return I(path=F,protocol=i)
	async def handle(A,scope:Ñ,receive:Ò,send:Send):
		C=receive;B=scope
		if A.methods and B[É]not in A.methods:
			D={'Allow':', '.join(A.methods)}
			if Â in B:raise Ú(status_code=405,headers=D)
			else:E=K('Method Not Allowed',status_code=405,headers=D)
			await E(B,C,send)
		else:await A.app(B,C,send)
	def __eq__(B,other:L):A=other;return a(A,u)and B.path==A.path and B.endpoint==A.endpoint and B.methods==A.methods
	def __repr__(A):B=A.__class__.__name__;C=sorted(A.methods or[]);D,E=A.path,A.name;return f"{B}(path={D!r}, name={E!r}, methods={C!r})"
class Ä(U):
	def __init__(A,path:J,endpoint:N[...,L],*,name:J|H=H,middleware:X[Þ]|H=H):
		E=middleware;D=path;B=endpoint;assert D.startswith(R),Á;A.path=D;A.endpoint=B;A.name=p(B)if name is H else name;C=B
		while a(C,m.partial):C=C.func
		if d.isfunction(C)or d.ismethod(C):A.app=Ô(B)
		else:A.app=B
		if E is not H:
			for(F,G,I)in y(E):A.app=F(A.app,*G,**I)
		A.path_regex,A.path_format,A.param_convertors=e(D)
	def matches(B,scope:Ñ):
		C=scope
		if C[O]==j:
			H=A(C);F=B.path_regex.match(H)
			if F:
				E=F.groupdict()
				for(G,I)in E.items():E[G]=B.param_convertors[G].convert(I)
				D=Q(C.get(c,{}));D.update(E);K={z:B.endpoint,c:D};return M.FULL,K
		return M.NONE,{}
	def url_path_for(A,C:J,**B:L):
		D=r(B.keys());E=r(A.param_convertors.keys())
		if C!=A.name or D!=E:raise Z(C,B)
		F,G=k(A.path_format,A.param_convertors,B);assert not G;return I(path=F,protocol=j)
	async def handle(A,scope:Ñ,receive:Ò,send:Send):await A.app(scope,receive,send)
	def __eq__(B,other:L):A=other;return a(A,Ä)and B.path==A.path and B.endpoint==A.endpoint
	def __repr__(A):return f"{A.__class__.__name__}(path={A.path!r}, name={A.name!r})"
class l(U):
	def __init__(A,path:J,app:Ê|H=H,routes:X[U]|H=H,name:J|H=H,*,middleware:X[Þ]|H=H):
		E=middleware;D=routes;C=app;B=path;assert B==b or B.startswith(R),Á;assert C is not H or D is not H,"Either 'app=...', or 'routes=' must be specified";A.path=B.rstrip(R)
		if C is not H:A._base_app=C
		else:A._base_app=v(routes=D)
		A.app=A._base_app
		if E is not H:
			for(F,G,I)in y(E):A.app=F(A.app,*G,**I)
		A.name=name;A.path_regex,A.path_format,A.param_convertors=e(A.path+'/{path:path}')
	@Ç
	def routes(self):return µ(self._base_app,Ë,[])
	def matches(D,scope:Ñ):
		N='app_root_path';K='root_path';B=scope
		if B[O]in(i,j):
			F=B.get(K,b);G=A(B);H=D.path_regex.match(G)
			if H:
				C=H.groupdict()
				for(I,P)in C.items():C[I]=D.param_convertors[I].convert(P)
				T=R+C.pop(S);U=G[:-x(T)];E=Q(B.get(c,{}));E.update(C);V={c:E,N:B.get(N,F),K:F+U,z:D.app};return M.FULL,V
		return M.NONE,{}
	def url_path_for(A,C:J,**B:L):
		if A.name is not H and C==A.name and S in B:
			B[S]=B[S].lstrip(R);K,D=k(A.path_format,A.param_convertors,B)
			if not D:return I(path=K)
		elif A.name is H or C.startswith(A.name+s):
			if A.name is H:E=C
			else:E=C[x(A.name)+1:]
			F=B.get(S);B[S]=b;M,D=k(A.path_format,A.param_convertors,B)
			if F is not H:D[S]=F
			for N in A.routes or[]:
				try:G=N.url_path_for(E,**D);return I(path=M.rstrip(R)+J(G),protocol=G.protocol)
				except Z:pass
		raise Z(C,B)
	async def handle(A,scope:Ñ,receive:Ò,send:Send):await A.app(scope,receive,send)
	def __eq__(B,other:L):A=other;return a(A,l)and B.path==A.path and B.app==A.app
	def __repr__(A):B=A.__class__.__name__;C=A.name or b;return f"{B}(path={A.path!r}, name={C!r}, app={A.app!r})"
class w(U):
	def __init__(A,host:J,app:Ê,name:J|H=H):B=host;assert not B.startswith(R),"Host must not start with '/'";A.host=B;A.app=app;A.name=name;A.host_regex,A.host_format,A.param_convertors=e(B)
	@Ç
	def routes(self):return µ(self.app,Ë,[])
	def matches(A,scope:Ñ):
		B=scope
		if B[O]in(i,j):
			H=D(scope=B);I=H.get('host',b).split(s)[0];E=A.host_regex.match(I)
			if E:
				C=E.groupdict()
				for(F,J)in C.items():C[F]=A.param_convertors[F].convert(J)
				G=Q(B.get(c,{}));G.update(C);K={c:G,z:A.app};return M.FULL,K
		return M.NONE,{}
	def url_path_for(A,B:J,**C:L):
		if A.name is not H and B==A.name and S in C:
			K=C.pop(S);D,E=k(A.host_format,A.param_convertors,C)
			if not E:return I(path=K,host=D)
		elif A.name is H or B.startswith(A.name+s):
			if A.name is H:F=B
			else:F=B[x(A.name)+1:]
			D,E=k(A.host_format,A.param_convertors,C)
			for M in A.routes or[]:
				try:G=M.url_path_for(F,**E);return I(path=J(G),protocol=G.protocol,host=D)
				except Z:pass
		raise Z(B,C)
	async def handle(A,scope:Ñ,receive:Ò,send:Send):await A.app(scope,receive,send)
	def __eq__(B,other:L):A=other;return a(A,w)and B.host==A.host and B.app==A.app
	def __repr__(A):B=A.__class__.__name__;C=A.name or b;return f"{B}(host={A.host!r}, name={C!r}, app={A.app!r})"
q=TypeVar('_T')
class Å(Ã[q]):
	def __init__(A,cm:Ï[q]):A._cm=cm
	async def __aenter__(A):return A._cm.__enter__()
	async def __aexit__(A,exc_type:type[À]|H,exc_value:À|H,traceback:types.TracebackType|H):return A._cm.__exit__(exc_type,exc_value,traceback)
def Ö(lifespan_context:N[[L],Î[L,L,L]]):
	A=Ì.contextmanager(lifespan_context)
	@m.wraps(A)
	def B(app:L):return Å(A(app))
	return B
class Ø:
	def __init__(A,router:v):A._router=router
	async def __aenter__(A):await A._router.startup()
	async def __aexit__(A,*B:object):await A._router.shutdown()
	def __call__(A:q,app:object):return A
class v:
	def __init__(A,routes:X[U]|H=H,redirect_slashes:T=t,default:Ê|H=H,on_startup:X[N[[],L]]|H=H,on_shutdown:X[N[[],L]]|H=H,lifespan:B[L]|H=H,*,middleware:X[Þ]|H=H):
		I=middleware;G=default;F=routes;E=on_shutdown;D=on_startup;C=lifespan;A.routes=[]if F is H else f(F);A.redirect_slashes=redirect_slashes;A.default=A.not_found if G is H else G;A.on_startup=[]if D is H else f(D);A.on_shutdown=[]if E is H else f(E)
		if D or E:
			V.warn('The on_startup and on_shutdown parameters are deprecated, and they will be removed on version 1.0. Use the lifespan parameter instead. See more about it on https://starlette.dev/lifespan/.',g)
			if C:V.warn('The `lifespan` parameter cannot be used with `on_startup` or `on_shutdown`. Both `on_startup` and `on_shutdown` will be ignored.')
		if C is H:A.lifespan_context=Ø(A)
		elif d.isasyncgenfunction(C):V.warn('async generator function lifespans are deprecated, use an @contextlib.asynccontextmanager function instead',g);A.lifespan_context=Ð(C)
		elif d.isgeneratorfunction(C):V.warn('generator function lifespans are deprecated, use an @contextlib.asynccontextmanager function instead',g);A.lifespan_context=Ö(C)
		else:A.lifespan_context=C
		A.middleware_stack=A.app
		if I:
			for(J,K,M)in y(I):A.middleware_stack=J(A.middleware_stack,*K,**M)
	async def not_found(E,scope:Ñ,receive:Ò,send:Send):
		B=receive;A=scope
		if A[O]==j:C=Ü();await C(A,B,send);return
		if Â in A:raise Ú(status_code=404)
		else:D=K(È,status_code=404)
		await D(A,B,send)
	def url_path_for(C,A:J,**B:L):
		for D in C.routes:
			try:return D.url_path_for(A,**B)
			except Z:pass
		raise Z(A,B)
	async def startup(B):
		for A in B.on_startup:
			if G(A):await A()
			else:A()
	async def shutdown(B):
		for A in B.on_shutdown:
			if G(A):await A()
			else:A()
	async def lifespan(J,scope:Ñ,receive:Ò,send:Send):
		I='message';G='state';C=receive;B=scope;A=send;D=False;K=B.get(Â);await C()
		try:
			async with J.lifespan_context(K)as E:
				if E is not H:
					if G not in B:raise RuntimeError('The server does not support "state" in the lifespan scope.')
					B[G].update(E)
				await A({O:'lifespan.startup.complete'});D=t;await C()
		except À:
			F=Í.format_exc()
			if D:await A({O:'lifespan.shutdown.failed',I:F})
			else:await A({O:'lifespan.startup.failed',I:F})
			raise
		else:await A({O:'lifespan.shutdown.complete'})
	async def __call__(A,scope:Ñ,receive:Ò,send:Send):await A.middleware_stack(scope,receive,send)
	async def app(C,scope:Ñ,receive:Ò,send:Send):
		U='router';T='lifespan';F=send;E=receive;B=scope;assert B[O]in(i,j,T)
		if U not in B:B[U]=C
		if B[O]==T:await C.lifespan(B,E,F);return
		I=H
		for G in C.routes:
			K,L=G.matches(B)
			if K==M.FULL:B.update(L);await G.handle(B,E,F);return
			elif K==M.PARTIAL and I is H:I=G;V=L
		if I is not H:B.update(V);await I.handle(B,E,F);return
		N=A(B)
		if B[O]==i and C.redirect_slashes and N!=R:
			D=Q(B)
			if N.endswith(R):D[S]=D[S].rstrip(R)
			else:D[S]=D[S]+R
			for G in C.routes:
				K,L=G.matches(D)
				if K!=M.NONE:X=W(scope=D);Y=P(url=J(X));await Y(B,E,F);return
		await C.default(B,E,F)
	def __eq__(B,other:L):A=other;return a(A,v)and B.routes==A.routes
	def mount(A,path:J,app:Ê,name:J|H=H):B=l(path,app=app,name=name);A.routes.append(B)
	def host(A,host:J,app:Ê,name:J|H=H):B=w(host,app=app,name=name);A.routes.append(B)
	def add_route(A,path:J,endpoint:N[[Y],o[C]|C],methods:ª[J]|H=H,name:J|H=H,include_in_schema:T=t):B=u(path,endpoint=endpoint,methods=methods,name=name,include_in_schema=include_in_schema);A.routes.append(B)
	def add_websocket_route(A,path:J,endpoint:N[[Û],o[H]],name:J|H=H):B=Ä(path,endpoint=endpoint,name=name);A.routes.append(B)
	def route(A,path:J,methods:ª[J]|H=H,name:J|H=H,include_in_schema:T=t):
		V.warn('The `route` decorator is deprecated, and will be removed in version 1.0.0.Refer to https://starlette.dev/routing/#http-routing for the recommended approach.',g)
		def B(func:N):A.add_route(path,func,methods=methods,name=name,include_in_schema=include_in_schema);return func
		return B
	def websocket_route(A,path:J,name:J|H=H):
		V.warn('The `websocket_route` decorator is deprecated, and will be removed in version 1.0.0. Refer to https://starlette.dev/routing/#websocket-routing for the recommended approach.',g)
		def B(func:N):A.add_websocket_route(path,func,name=name);return func
		return B
	def add_event_handler(A,event_type:J,func:N[[],L]):
		C='startup';B=event_type;assert B in(C,'shutdown')
		if B==C:A.on_startup.append(func)
		else:A.on_shutdown.append(func)
	def on_event(A,event_type:J):
		V.warn('The `on_event` decorator is deprecated, and will be removed in version 1.0.0. Refer to https://starlette.dev/lifespan/ for recommended approach.',g)
		def B(func:N):A.add_event_handler(event_type,func);return func
		return B