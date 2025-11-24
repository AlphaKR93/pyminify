O=Exception
N=bool
L=DeprecationWarning
K=list
F=str
D=None
import warnings as H
from collections.abc import Awaitable as P,Callable as E,Mapping as R,Sequence as J
from typing import Any as G,ParamSpec as S,TypeVar as T
from F.I import V
from F.M import Þ,X
from F.M.B import a
from F.M.D import Z
from F.M.E import W
from F.N import Y
from F.O import C
from F.P import U,v
from F.V import Ê,A,B,Ò,Ñ,Send
from F.W import Û
Q=T('AppType',bound='Starlette')
M=S('P')
class r:
	def __init__(A:Q,debug:N=False,routes:J[U]|D=D,middleware:J[Þ]|D=D,exception_handlers:R[G,A]|D=D,on_startup:J[E[[],G]]|D=D,on_shutdown:J[E[[],G]]|D=D,lifespan:B[Q]|D=D):G=lifespan;F=on_shutdown;E=on_startup;C=exception_handlers;B=middleware;assert G is D or E is D and F is D,"Use either 'lifespan' or 'on_startup'/'on_shutdown', not both.";A.debug=debug;A.state=V();A.router=v(routes,on_startup=E,on_shutdown=F,lifespan=G);A.exception_handlers={}if C is D else dict(C);A.user_middleware=[]if B is D else K(B);A.middleware_stack=D
	def build_middleware_stack(B):
		E=B.debug;F=D;H={}
		for(I,J)in B.exception_handlers.items():
			if I in(500,O):F=J
			else:H[I]=J
		K=[Þ(Z,handler=F,debug=E)]+B.user_middleware+[Þ(W,handlers=H,debug=E)];C=B.router
		for(L,M,N)in reversed(K):C=L(C,*M,**N)
		return C
	@property
	def routes(self):return self.router.routes
	def url_path_for(A,B:F,**C:G):return A.router.url_path_for(B,**C)
	async def __call__(A,scope:Ñ,receive:Ò,send:Send):
		B=scope;B['app']=A
		if A.middleware_stack is D:A.middleware_stack=A.build_middleware_stack()
		await A.middleware_stack(B,receive,send)
	def on_event(A,event_type:F):return A.router.on_event(event_type)
	def mount(A,path:F,app:Ê,name:F|D=D):A.router.mount(path,app=app,name=name)
	def host(A,host:F,app:Ê,name:F|D=D):A.router.host(host,app=app,name=name)
	def add_middleware(A,middleware_class:X[M],*B:M.args,**C:M.kwargs):
		if A.middleware_stack is not D:raise RuntimeError('Cannot add middleware after an application has started')
		A.user_middleware.insert(0,Þ(middleware_class,*B,**C))
	def add_exception_handler(A,exc_class_or_status_code:int|type[O],handler:A):A.exception_handlers[exc_class_or_status_code]=handler
	def add_event_handler(A,event_type:F,func:E):A.router.add_event_handler(event_type,func)
	def add_route(A,path:F,route:E[[Y],P[C]|C],methods:K[F]|D=D,name:F|D=D,include_in_schema:N=True):A.router.add_route(path,route,methods=methods,name=name,include_in_schema=include_in_schema)
	def add_websocket_route(A,path:F,route:E[[Û],P[D]],name:F|D=D):A.router.add_websocket_route(path,route,name=name)
	def exception_handler(A,exc_class_or_status_code:int|type[O]):
		H.warn('The `exception_handler` decorator is deprecated, and will be removed in version 1.0.0. Refer to https://starlette.dev/exceptions/ for the recommended approach.',L)
		def B(func:E):A.add_exception_handler(exc_class_or_status_code,func);return func
		return B
	def route(A,path:F,methods:K[F]|D=D,name:F|D=D,include_in_schema:N=True):
		H.warn('The `route` decorator is deprecated, and will be removed in version 1.0.0. Refer to https://starlette.dev/routing/ for the recommended approach.',L)
		def B(func:E):A.router.add_route(path,func,methods=methods,name=name,include_in_schema=include_in_schema);return func
		return B
	def websocket_route(A,path:F,name:F|D=D):
		H.warn('The `websocket_route` decorator is deprecated, and will be removed in version 1.0.0. Refer to https://starlette.dev/routing/#websocket-routing for the recommended approach.',L)
		def B(func:E):A.router.add_websocket_route(path,func,name=name);return func
		return B
	def middleware(A,middleware_type:F):
		H.warn('The `middleware` decorator is deprecated, and will be removed in version 1.0.0. Refer to https://starlette.dev/middleware/#using-middleware for recommended approach.',L);assert middleware_type=='http','Currently only middleware("http") is supported.'
		def B(func:E):A.add_middleware(a,dispatch=func);return func
		return B