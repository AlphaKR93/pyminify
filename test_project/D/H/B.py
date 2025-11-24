Ô='request'
Ó='__globals__'
Ò=RuntimeError
Ã='convert_underscores'
Â='function'
Á=ImportError
y='body'
x=any
s=False
q=len
m=bool
j=getattr
g=True
c=str
X=isinstance
V=None
import dataclasses as Õ,inspect as k
from contextlib import AsyncExitStack as z,contextmanager as Ö
from copy import copy,deepcopy as Ä
from dataclasses import dataclass as Å
from typing import Any as W,Callable as t,Coroutine as Ø,Dict as e,ForwardRef as Ù,List as f,Mapping as Ç,Optional as h,Sequence as Ú,Tuple as p,Union as l,cast
import anyio
from D import params as b
from D.B import PYDANTIC_V2 as Ü,ModelField as i,O,Ă,_is_error_wrapper as Þ,_is_model_class as u,copy_field_info as ß,create_body_model as à,Q,field_annotation_is_scalar as á,get_annotation_from_field_info as â,get_cached_model_fields as º,P,is_bytes_field as ã,is_bytes_sequence_field as ä,is_scalar_field as È,is_scalar_sequence_field as å,is_sequence_field as É,is_uploadfile_or_nonable_uploadfile_annotation as æ,is_uploadfile_sequence_annotation as ç,lenient_issubclass as n,may_v1 as o,sequence_types as è,serialize_sequence_value as é,value_is_sequence as ê
from D.B.D import r
from D.D import F
from D.F import A,J
from D.H.A import Č,ö
from D.K import N
from D.L import I
from D.T.B import v
from D.T.D import R,U
from D.T.E import S
from D.Y import M
from D.Z import K,a
from pydantic import BaseModel as ë
from pydantic.fields import FieldInfo as w
from F.E import B
from F.F import Æ
from F.I import H,D,T,Z,G
from F.N import E,Y
from F.O import C
from F.W import Û
from typing_extensions import Annotated as ì,Literal,get_args as Ê,get_origin as Ë
from..import temp_pydantic_v1_params as d
Ì='Form data requires "python-multipart" to be installed. \nYou can install "python-multipart" with: \n\npip install python-multipart\n'
Í='Form data requires "python-multipart" to be installed. It seems you installed "multipart" instead. \nYou can remove "multipart" with: \n\npip uninstall multipart\n\nAnd then install "python-multipart" with: \n\npip install python-multipart\n'
def í():
	try:from python_multipart import __version__;assert __version__>'0.0.12'
	except(Á,AssertionError):
		try:
			from multipart import __version__;assert __version__
			try:from multipart.multipart import parse_options_header as A;assert A
			except Á:I.error(Í);raise Ò(Í)from V
		except Á:I.error(Ì);raise Ò(Ì)from V
def Ĉ(*,depends:b.Depends,path:c):
	A=depends;assert callable(A.dependency),'A parameter-less dependency must have a callable dependency';B=[]
	if X(A,b.Security)and A.scopes:B.extend(A.scopes)
	return Ć(path=path,call=A.dependency,scope=A.scope,security_scopes=B)
def ą(dependant:Č,*,skip_repeats:m=s,visited:h[f[M]]=V):
	E=skip_repeats;D=visited;A=dependant
	if D is V:D=[]
	D.append(A.cache_key);B=Č(path_params=A.path_params.copy(),query_params=A.query_params.copy(),header_params=A.header_params.copy(),cookie_params=A.cookie_params.copy(),body_params=A.body_params.copy(),security_requirements=A.security_requirements.copy(),use_cache=A.use_cache,path=A.path)
	for F in A.dependencies:
		if E and F.cache_key in D:continue
		C=ą(F,skip_repeats=E,visited=D);B.path_params.extend(C.path_params);B.query_params.extend(C.query_params);B.header_params.extend(C.header_params);B.cookie_params.extend(C.cookie_params);B.body_params.extend(C.body_params);B.security_requirements.extend(C.security_requirements)
	return B
def Ï(fields:f[i]):
	A=fields
	if not A:return A
	B=A[0]
	if q(A)==1 and u(B.type_):C=º(B.type_);return C
	return A
def Ý(dependant:Č):A=ą(dependant,skip_repeats=g);B=Ï(A.path_params);C=Ï(A.query_params);D=Ï(A.header_params);E=Ï(A.cookie_params);return B+C+D+E
def î(call:t[...,W]):A=k.signature(call);B=j(call,Ó,{});C=[k.Parameter(name=A.name,kind=A.kind,default=A.default,annotation=Î(A.annotation,B))for A in A.parameters.values()];D=k.Signature(C);return D
def Î(annotation:W,globalns:e[c,W]):
	B=globalns;A=annotation
	if X(A,c):
		A=Ù(A);A=Q(A,B,B)
		if A is type(V):return
	return A
def Ċ(call:t[...,W]):
	B=k.signature(call);A=B.return_annotation
	if A is k.Signature.empty:return
	C=j(call,Ó,{});return Î(A,C)
def Ć(*,path:c,call:t[...,W],name:h[c]=V,security_scopes:h[f[c]]=V,use_cache:m=g,scope:l[Literal[Â,Ô],V]=V):
	F=security_scopes;E=path;C=call;B=Č(call=C,name=name,path=E,security_scopes=F,use_cache=use_cache,scope=scope);J=a(E);K=î(C);L=K.parameters
	if X(C,v):
		G=[]
		if X(C,(R,S)):G=F or G
		M=ö(security_scheme=C,scopes=G);B.security_requirements.append(M)
	for(D,H)in L.items():
		O=D in J;A=ð(param_name=D,annotation=H.annotation,value=H.default,is_path_param=O)
		if A.depends is not V:
			assert A.depends.dependency
			if(B.is_gen_callable or B.is_async_gen_callable)and B.computed_scope==Ô and A.depends.scope==Â:assert B.call;raise N(f'The dependency "{B.call.__name__}" has a scope of "request", it cannot depend on dependencies with scope "function".')
			I=F or[]
			if X(A.depends,b.Security):
				if A.depends.scopes:I.extend(A.depends.scopes)
			P=Ć(path=E,call=A.depends.dependency,name=D,security_scopes=I,use_cache=A.depends.use_cache,scope=A.depends.scope);B.dependencies.append(P);continue
		if ï(param_name=D,type_annotation=A.type_annotation,dependant=B):assert A.field is V,f"Cannot specify multiple FastAPI annotations for {D!r}";continue
		assert A.field is not V
		if X(A.field.field_info,(b.Body,d.Body)):B.body_params.append(A.field)
		else:ñ(field=A.field,dependant=B)
	return B
def ï(*,param_name:c,type_annotation:W,dependant:Č):
	F=dependant;D=type_annotation;A=param_name
	if n(D,Y):F.request_param_name=A;return g
	elif n(D,Û):F.websocket_param_name=A;return g
	elif n(D,E):F.http_connection_param_name=A;return g
	elif n(D,C):F.response_param_name=A;return g
	elif n(D,B):F.background_tasks_param_name=A;return g
	elif n(D,U):F.security_scopes_param_name=A;return g
@Å
class Ð:type_annotation:W;depends:h[b.Depends];field:h[i]
def ð(*,param_name:c,annotation:W,value:W,is_path_param:m):
	N=is_path_param;M=annotation;I=value;H=param_name;A=V;D=V;F=W;G=W
	if M is not k.Signature.empty:G=M;F=M
	if Ë(G)is ì:
		R=Ê(M);F=R[0];T=[A for A in R[1:]if X(A,(w,o.FieldInfo,b.Depends))];S=[A for A in T if X(A,(b.Param,d.Param,b.Body,d.Body,b.Depends))]
		if S:L=S[-1]
		else:L=V
		if X(L,(w,o.FieldInfo)):
			A=ß(field_info=L,annotation=G);assert A.default in{Ă,o.Undefined}or A.default in{O,o.RequiredParam},f"`{A.__class__.__name__}` default value cannot be set in `Annotated` for {H!r}. Set the default value with `=` instead."
			if I is not k.Signature.empty:assert not N,'Path parameters cannot have default values';A.default=I
			else:A.default=O
		elif X(L,b.Depends):D=L
	if X(I,b.Depends):assert D is V,f"Cannot specify `Depends` in `Annotated` and default value together for {H!r}";assert A is V,f"Cannot specify a FastAPI annotation in `Annotated` and `Depends` as a default value together for {H!r}";D=I
	elif X(I,(w,o.FieldInfo)):
		assert A is V,f"Cannot specify FastAPI annotations in `Annotated` and default value together for {H!r}";A=I
		if Ü:
			if X(A,w):A.annotation=F
	if D is not V and D.dependency is V:D=copy(D);D=Õ.replace(D,dependency=F)
	if n(F,(Y,Û,E,C,B,U)):assert D is V,f"Cannot specify `Depends` for type {F!r}";assert A is V,f"Cannot specify FastAPI annotation for type {F!r}"
	elif A is V and D is V:
		P=I if I is not k.Signature.empty else O
		if N:A=b.Path(annotation=G)
		elif æ(F)or ç(F):A=b.File(annotation=G,default=P)
		elif not á(annotation=F):
			if r(G):A=d.Body(annotation=G,default=P)
			else:A=b.Body(annotation=G,default=P)
		else:A=b.Query(annotation=G,default=P)
	J=V
	if A is not V:
		if N:assert X(A,(b.Path,d.Path)),f"Cannot use `{A.__class__.__name__}` for path param {H!r}"
		elif X(A,(b.Param,d.Param))and j(A,'in_',V)is V:A.in_=b.ParamTypes.query
		Z=â(G,A,H)
		if X(A,(b.Form,d.Form)):í()
		if not A.alias and j(A,Ã,V):Q=H.replace('_','-')
		else:Q=A.alias or H
		A.alias=Q;J=K(name=H,type_=Z,default=A.default,alias=Q,required=A.default in(O,o.RequiredParam,Ă),field_info=A)
		if N:assert È(field=J),'Path params must be of one of the supported types'
		elif X(A,(b.Query,d.Query)):assert È(J)or å(J)or u(J.type_)and j(J,'shape',1)==1
	return Ð(type_annotation=F,depends=D,field=J)
def ñ(*,field:i,dependant:Č):
	B=dependant;A=field;D=A.field_info;C=j(D,'in_',V)
	if C==b.ParamTypes.path:B.path_params.append(A)
	elif C==b.ParamTypes.query:B.query_params.append(A)
	elif C==b.ParamTypes.header:B.header_params.append(A)
	else:assert C==b.ParamTypes.cookie,f"non-body parameters must be in path, query, header or cookie: {A.name}";B.cookie_params.append(A)
async def ò(*,dependant:Č,stack:z,sub_values:e[c,W]):
	C=sub_values;B=dependant;assert B.call
	if B.is_gen_callable:D=J(Ö(B.call)(**C))
	elif B.is_async_gen_callable:D=A(B.call)(**C)
	return await stack.enter_async_context(D)
@Å
class Ñ:values:e[c,W];errors:f[W];background_tasks:h[B];response:C;dependency_cache:e[M,W]
async def ć(*,request:l[Y,Û],dependant:Č,body:h[l[e[c,W],H]]=V,background_tasks:h[B]=V,response:h[C]=V,dependency_overrides_provider:h[W]=V,dependency_cache:h[e[M,W]]=V,async_exit_stack:z,embed_body_fields:m):
	P=embed_body_fields;M=dependency_overrides_provider;I=background_tasks;H=response;G=dependency_cache;E=request;A=dependant;Q=E.scope.get('fastapi_inner_astack');assert X(Q,z),'fastapi_inner_astack not found in request scope';R=E.scope.get('fastapi_function_astack');assert X(R,z),'fastapi_function_astack not found in request scope';D={};N=[]
	if H is V:H=C();del H.headers['content-length'];H.status_code=V
	if G is V:G={}
	for B in A.dependencies:
		B.call=B.call;O=B.call;J=B
		if M and M.dependency_overrides:S=B.call;O=j(M,'dependency_overrides',{}).get(S,S);Z=B.path;J=Ć(path=Z,call=O,name=B.name,security_scopes=B.security_scopes,scope=B.scope)
		K=await ć(request=E,dependant=J,body=body,background_tasks=I,response=H,dependency_overrides_provider=M,dependency_cache=G,async_exit_stack=async_exit_stack,embed_body_fields=P);I=K.background_tasks
		if K.errors:N.extend(K.errors);continue
		if B.use_cache and B.cache_key in G:L=G[B.cache_key]
		elif J.is_gen_callable or J.is_async_gen_callable:
			T=Q
			if B.scope==Â:T=R
			L=await ò(dependant=J,stack=T,sub_values=K.values)
		elif J.is_coroutine_callable:L=await O(**K.values)
		else:L=await Æ(O,**K.values)
		if B.name is not V:D[B.name]=L
		if B.cache_key not in G:G[B.cache_key]=L
	a,b=µ(A.path_params,E.path_params);d,g=µ(A.query_params,E.query_params);h,i=µ(A.header_params,E.headers);k,l=µ(A.cookie_params,E.cookies);D.update(a);D.update(d);D.update(h);D.update(k);N+=b+g+i+l
	if A.body_params:m,n=await õ(body_fields=A.body_params,received_body=body,embed_body_fields=P);D.update(m);N.extend(n)
	if A.http_connection_param_name:D[A.http_connection_param_name]=E
	if A.request_param_name and X(E,Y):D[A.request_param_name]=E
	elif A.websocket_param_name and X(E,Û):D[A.websocket_param_name]=E
	if A.background_tasks_param_name:
		if I is V:I=F()
		D[A.background_tasks_param_name]=I
	if A.response_param_name:D[A.response_param_name]=H
	if A.security_scopes_param_name:D[A.security_scopes_param_name]=U(scopes=A.security_scopes)
	return Ñ(values=D,errors=N,background_tasks=I,response=H,dependency_cache=G)
def ª(*,field:i,value:W,values:e[c,W],loc:p[c,...]):
	C=value;B=field
	if C is V:
		if B.required:return V,[P(loc=loc)]
		else:return Ä(B.default),[]
	D,A=B.validate(C,values,loc=loc)
	if Þ(A):return V,[A]
	elif X(A,list):E=o._regenerate_error_with_loc(errors=A,loc_prefix=());return V,E
	else:return D,[]
def À(field:i,values:Ç[c,W],alias:l[c,V]=V):
	E=values;C=alias;A=field;C=C or A.alias
	if É(A)and X(E,(T,D)):B=E.getlist(C)
	else:B=E.get(C,V)
	if B is V or X(A.field_info,(b.Form,d.Form))and X(B,c)and B==''or É(A)and q(B)==0:
		if A.required:return
		else:return Ä(A.default)
	return B
def µ(fields:Ú[i],received_params:l[Ç[c,W],Z,D]):
	T='Params must be subclasses of Param';H=received_params;E=fields;F={};J=[]
	if not E:return F,J
	B=E[0];P=E;Q=s;R=g
	if q(E)==1 and n(B.type_,ë):P=º(B.type_);Q=g;R=j(B.field_info,Ã,g)
	K={};L=set()
	for A in P:
		M=V
		if X(H,D):
			U=j(A.field_info,Ã,R)
			if U:M=A.alias if A.alias!=A.name else A.name.replace('_','-')
		C=À(A,H,alias=M)
		if C is not V:K[A.name]=C
		L.add(M or A.alias);L.add(A.name)
	for(S,C)in H.items():
		if S not in L:K[S]=C
	if Q:G=B.field_info;assert X(G,(b.Param,d.Param)),T;N=G.in_.value,;O,I=ª(field=B,value=K,values=F,loc=N);return{B.name:O},I
	for A in E:
		C=À(A,H);G=A.field_info;assert X(G,(b.Param,d.Param)),T;N=G.in_.value,A.alias;O,I=ª(field=A,value=C,values=F,loc=N)
		if I:J.extend(I)
		else:F[A.name]=O
	return F,J
def ó(field_type:W):
	A=field_type;from D.Y import L;B=Ë(A)
	if B is not l and B is not L:return s
	C=Ê(A)
	for D in C:
		if not u(D):return s
	return g
def ĉ(fields:f[i]):
	B=fields
	if not B:return s
	C={A.name for A in B}
	if q(C)>1:return g
	A=B[0]
	if j(A.field_info,'embed',V):return g
	if X(A.field_info,(b.Form,d.Form))and not u(A.type_)and not ó(A.type_):return g
	return s
async def ô(body_fields:f[i],received_body:H):
	D=received_body;C={}
	for B in body_fields:
		A=À(B,D);E=B.field_info
		if X(E,(b.File,d.File))and ã(B)and X(A,G):A=await A.read()
		elif ä(B)and X(E,(b.File,d.File))and ê(A):
			assert X(A,è);F=[]
			async def I(fn:t[[],Ø[W,W,W]]):A=await fn();F.append(A)
			async with anyio.create_task_group()as J:
				for K in A:J.start_soon(I,K.read)
			A=é(field=B,value=F)
		if A is not V:C[B.alias]=A
	for(H,A)in D.items():
		if H not in C:C[H]=A
	return C
async def õ(body_fields:f[i],received_body:h[l[e[c,W],H]],embed_body_fields:m):
	B=received_body;A=body_fields;C={};J=[];assert A,'request_body_to_args() should be called with fields';L=q(A)==1 and not embed_body_fields;D=A[0];E=B;M=A
	if L and u(D.type_)and X(B,H):M=º(D.type_)
	if X(B,H):E=await ô(M,B)
	if L:F=y,;K,G=ª(field=D,value=E,values=C,loc=F);return{D.name:K},G
	for I in A:
		F=y,I.alias;N=V
		if E is not V:
			try:N=E.get(I.alias)
			except AttributeError:J.append(P(F));continue
		K,G=ª(field=I,value=N,values=C,loc=F)
		if G:J.extend(G)
		else:C[I.name]=K
	return C,J
def ċ(*,flat_dependant:Č,name:c,embed_body_fields:m):
	A=flat_dependant
	if not A.body_params:return
	G=A.body_params[0]
	if not embed_body_fields:return G
	H='Body_'+name;C=à(fields=A.body_params,model_name=H);E=x(g for A in A.body_params if A.required);D={'annotation':C,'alias':y}
	if not E:D['default']=V
	if x(X(A.field_info,b.File)for A in A.body_params):B=b.File
	elif x(X(A.field_info,d.File)for A in A.body_params):B=d.File
	elif x(X(A.field_info,b.Form)for A in A.body_params):B=b.Form
	elif x(X(A.field_info,d.Form)for A in A.body_params):B=d.Form
	else:
		if r(C):B=d.Body
		else:B=b.Body
		F=[A.field_info.media_type for A in A.body_params if X(A.field_info,(b.Body,d.Body))]
		if q(set(F))==1:D['media_type']=F[0]
	I=K(name=y,type_=C,required=E,alias=y,field_info=B(**D));return I