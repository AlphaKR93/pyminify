V=ValueError
S=DeprecationWarning
R=list
Q=int
J='context'
H=dict
G='request'
F=len
C=str
B=None
import warnings as M
from collections.abc import Callable as N,Mapping as O,Sequence as P
from os import PathLike as I
from typing import Any as D,cast,overload as K
from F.E import A
from F.N import Y
from F.O import X
from F.V import Ò,Ñ,Send
try:
	import jinja2 as E
	if hasattr(E,'pass_context'):T=E.pass_context
	else:T=E.contextfunction
except ModuleNotFoundError:E=B
class L(X):
	def __init__(A,template:D,context:H[C,D],status_code:Q=200,headers:O[C,C]|B=B,media_type:C|B=B,background:A|B=B):C=context;B=template;A.template=B;A.context=C;D=B.render(C);super().__init__(D,status_code,headers,media_type,background)
	async def __call__(A,scope:Ñ,receive:Ò,send:Send):
		B='http.response.debug';C=A.context.get(G,{});D=C.get('extensions',{})
		if B in D:await send({'type':B,'info':{'template':A.template,J:A.context}})
		await super().__call__(scope,receive,send)
class U:
	@K
	def __init__(self,directory:C|I[C]|P[C|I[C]],*,context_processors:R[N[[Y],H[C,D]]]|B=B,**A:D):0
	@K
	def __init__(self,*,env:E.Environment,context_processors:R[N[[Y],H[C,D]]]|B=B):0
	def __init__(A,directory:C|I[C]|P[C|I[C]]|B=B,*,context_processors:R[N[[Y],H[C,D]]]|B=B,env:E.Environment|B=B,**G:D):
		F=env;C=directory
		if G:M.warn('Extra environment options are deprecated. Use a preconfigured jinja2.Environment instead.',S)
		assert E is not B,'jinja2 must be installed to use Jinja2Templates';assert bool(C)^bool(F),"either 'directory' or 'env' arguments must be passed";A.context_processors=context_processors or[]
		if C is not B:A.env=A._create_env(C,**G)
		elif F is not B:A.env=F
		A._setup_env_defaults(A.env)
	def _create_env(C,directory:C|I[C]|P[C|I[C]],**A:D):B=E.FileSystemLoader(directory);A.setdefault('loader',B);A.setdefault('autoescape',True);return E.Environment(**A)
	def _setup_env_defaults(B,env:E.Environment):
		@T
		def A(A:H[C,D],B:C,**C:D):E=A[G];return E.url_for(B,**C)
		env.globals.setdefault('url_for',A)
	def get_template(A,name:C):return A.env.get_template(name)
	@K
	def TemplateResponse(self,request:Y,name:C,context:H[C,D]|B=B,status_code:Q=200,headers:O[C,C]|B=B,media_type:C|B=B,background:A|B=B):0
	@K
	def TemplateResponse(self,name:C,context:H[C,D]|B=B,status_code:Q=200,headers:O[C,C]|B=B,media_type:C|B=B,background:A|B=B):0
	def TemplateResponse(W,*A:D,**B:D):
		Y='name';X='context must include a "request" key';U='background';T='media_type';R='headers';Q='status_code'
		if A:
			if isinstance(A[0],C):
				M.warn('The `name` is not the first parameter anymore. The first parameter should be the `Request` instance.\nReplace `TemplateResponse(name, {"request": request})` by `TemplateResponse(request, name)`.',S);I=A[0];E=A[1]if F(A)>1 else B.get(J,{});K=A[2]if F(A)>2 else B.get(Q,200);N=A[3]if F(A)>3 else B.get(R);O=A[4]if F(A)>4 else B.get(T);P=A[5]if F(A)>5 else B.get(U)
				if G not in E:raise V(X)
				H=E[G]
			else:H=A[0];I=A[1]if F(A)>1 else B[Y];E=A[2]if F(A)>2 else B.get(J,{});K=A[3]if F(A)>3 else B.get(Q,200);N=A[4]if F(A)>4 else B.get(R);O=A[5]if F(A)>5 else B.get(T);P=A[6]if F(A)>6 else B.get(U)
		else:
			if G not in B:
				M.warn('The `TemplateResponse` now requires the `request` argument.\nReplace `TemplateResponse(name, {"context": context})` by `TemplateResponse(request, name)`.',S)
				if G not in B.get(J,{}):raise V(X)
			E=B.get(J,{});H=B.get(G,E.get(G));I=B[Y];K=B.get(Q,200);N=B.get(R);O=B.get(T);P=B.get(U)
		E.setdefault(G,H)
		for Z in W.context_processors:E.update(Z(H))
		a=W.get_template(I);return L(a,E,status_code=K,headers=N,media_type=O,background=P)