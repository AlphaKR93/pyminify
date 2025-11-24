À='summary'
º='examples'
µ='include_in_schema'
ª='DEFAULT'
z='object'
y='properties'
t='deprecated'
s='example'
r='in'
q='name'
p='serialization'
o='validation'
n='HTTPValidationError'
f='content'
e='string'
d='ValidationError'
c='required'
b=list
a=bool
X='schema'
T='title'
S=isinstance
R='description'
Q=getattr
K='type'
G=True
E=None
B=str
import http.client,inspect,warnings as u
from typing import Any as D,Dict as C,List as N,Optional as F,Sequence as h,Set as i,Tuple as W,Union as j,cast
from D import routing as P
from D.B import l,ModelField as O,Ă,get_compat_model_name_map as Á,get_definitions as Â,get_schema_from_model_field as Y,lenient_issubclass as v
from D.G import J
from D.H.A import Č
from D.H.B import Ï,ą,Ý
from D.I import L
from D.N.A import Ü,ß
from D.N.C import Î
from D.P import V,g
from D.Y import A
from D.Z import M,Z,I
from pydantic import BaseModel as Ã
from F.O import H
from F.P import U
from typing_extensions import Literal as k
from..B import _is_model_field as w
Æ={T:d,K:z,y:{'loc':{T:'Location',K:'array','items':{'anyOf':[{K:e},{K:'integer'}]}},'msg':{T:'Message',K:e},K:{T:'Error Type',K:e}},c:['loc','msg',K]}
Ç={T:n,K:z,y:{'detail':{T:'Detail',K:'array','items':{'$ref':ß+d}}}}
È={'1XX':'Information','2XX':'Success','3XX':'Redirection','4XX':'Client Error','5XX':'Server Error',ª:'Default Response'}
def É(flat_dependant:Č):
	B={};C=[]
	for A in flat_dependant.security_requirements:E=L(A.security_scheme.model,by_alias=G,exclude_none=G);D=A.security_scheme.scheme_name;B[D]=E;C.append({D:A.scopes})
	return B,C
def Ê(*,dependant:Č,model_name_map:A,field_mapping:C[W[O,k[o,p]],l],separate_input_output_schemas:a=G):
	O='convert_underscores';F=[];B=ą(dependant,skip_repeats=G);P=Ï(B.path_params);S=Ï(B.query_params);T=Ï(B.header_params);U=Ï(B.cookie_params);V=[(g.path,P),(g.query,S),(g.header,T),(g.cookie,U)];H=G
	if len(B.header_params)==1:
		I=B.header_params[0]
		if v(I.type_,Ã):H=Q(I.field_info,O,G)
	for(J,W)in V:
		for A in W:
			C=A.field_info
			if not Q(C,µ,G):continue
			Z=Y(field=A,model_name_map=model_name_map,field_mapping=field_mapping,separate_input_output_schemas=separate_input_output_schemas);K=A.alias;a=Q(A.field_info,O,H)
			if J==g.header and A.alias==A.name and a:K=A.name.replace('_','-')
			D={q:K,r:J.value,c:A.required,X:Z}
			if C.description:D[R]=C.description
			M=Q(C,'openapi_examples',E);N=Q(C,s,E)
			if M:D[º]=L(M)
			elif N!=Ă:D[s]=L(N)
			if Q(C,t,E):D[t]=G
			F.append(D)
	return F
def Ë(*,body_field:F[O],model_name_map:A,field_mapping:C[W[O,k[o,p]],l],separate_input_output_schemas:a=G):
	A=body_field
	if not A:return
	assert w(A);I=Y(field=A,model_name_map=model_name_map,field_mapping=field_mapping,separate_input_output_schemas=separate_input_output_schemas);E=A.field_info;J=E.media_type;H=A.required;F={}
	if H:F[c]=H
	G={X:I}
	if E.openapi_examples:G[º]=L(E.openapi_examples)
	elif E.example!=Ă:G[s]=L(E.example)
	F[f]={J:G};return F
def Í(*,route:P.APIRoute,method:B):
	A=route;u.warn('fastapi.openapi.utils.generate_operation_id() was deprecated, it is not used internally, and will be removed soon',DeprecationWarning,stacklevel=2)
	if A.operation_id:return A.operation_id
	C=A.path_format;return Z(name=A.name,path=C,method=method)
def Ä(*,route:P.APIRoute,method:B):
	A=route
	if A.summary:return A.summary
	return A.name.replace('_',' ').title()
def Ì(*,route:P.APIRoute,method:B,operation_ids:i[B]):
	G=operation_ids;A=route;E={}
	if A.tags:E['tags']=A.tags
	E[À]=Ä(route=A,method=method)
	if A.description:E[R]=A.description
	F=A.operation_id or A.unique_id
	if F in G:
		H=f"Duplicate Operation ID {F} for function "+f"{A.endpoint.__name__}";I=Q(A.endpoint,'__globals__',{}).get('__file__')
		if I:H+=f" at {I}"
		u.warn(H,stacklevel=1)
	G.add(F);E['operationId']=F
	if A.deprecated:E[t]=A.deprecated
	return E
def m(*,route:P.APIRoute,operation_ids:i[B],model_name_map:A,field_mapping:C[W[O,k[o,p]],l],separate_input_output_schemas:a=G):
	Ä='application/json';Ã='default';t=operation_ids;W='responses';T=separate_input_output_schemas;Q=field_mapping;O=model_name_map;A=route;u={};w={};h={};assert A.methods is not E,'Methods must be a list'
	if S(A.response_class,J):U=A.response_class.value
	else:U=A.response_class
	assert U,'A response class is needed to generate OpenAPI';i=U.media_type
	if A.include_in_schema:
		for j in A.methods:
			L=Ì(route=A,method=j,operation_ids=t);Z=[];Í=ą(A.dependant,skip_repeats=G);x,y=É(flat_dependant=Í)
			if y:L.setdefault('security',[]).extend(y)
			if x:w.update(x)
			Î=Ê(dependant=A.dependant,model_name_map=O,field_mapping=Q,separate_input_output_schemas=T);Z.extend(Î)
			if Z:z={(A[r],A[q]):A for A in Z};Ï={(A[r],A[q]):A for A in Z if A.get(c)};z.update(Ï);L['parameters']=b(z.values())
			if j in Ü:
				µ=Ë(body_field=A.body_field,model_name_map=O,field_mapping=Q,separate_input_output_schemas=T)
				if µ:L['requestBody']=µ
			if A.callbacks:
				º={}
				for a in A.callbacks:
					if S(a,P.APIRoute):Ð,Ú,Û=m(route=a,operation_ids=t,model_name_map=O,field_mapping=Q,separate_input_output_schemas=T);º[a.name]={a.path:Ð}
				L['callbacks']=º
			if A.status_code is not E:k=B(A.status_code)
			else:
				Ñ=inspect.signature(U.__init__);l=Ñ.parameters.get('status_code')
				if l is not E:
					if S(l.default,int):k=B(l.default)
			L.setdefault(W,{}).setdefault(k,{})[R]=A.response_description
			if i and I(A.status_code):
				o={K:e}
				if v(U,H):
					if A.response_field:o=Y(field=A.response_field,model_name_map=O,field_mapping=Q,separate_input_output_schemas=T)
					else:o={}
				L.setdefault(W,{}).setdefault(k,{}).setdefault(f,{}).setdefault(i,{})[X]=o
			if A.responses:
				Ò=L.setdefault(W,{})
				for(g,Ó)in A.responses.items():
					V=Ó.copy();V.pop('model',E);p=B(g).upper()
					if p==ª:p=Ã
					s=Ò.setdefault(p,{});assert S(V,dict),'An additional response must be a dict';À=A.response_fields.get(g);Á=E
					if À:Á=Y(field=À,model_name_map=O,field_mapping=Q,separate_input_output_schemas=T);Ô=i or Ä;Õ=V.setdefault(f,{}).setdefault(Ô,{}).setdefault(X,{});M(Õ,Á)
					Ö=È.get(B(g).upper())or http.client.responses.get(int(g));Ø=V.get(R)or s.get(R)or Ö or'Additional Response';M(s,V);s[R]=Ø
			Â='422';Ù=Ý(A.dependant)
			if(Ù or A.body_field)and not any(A in L[W]for A in[Â,'4XX',Ã]):
				L[W][Â]={R:'Validation Error',f:{Ä:{X:{'$ref':ß+n}}}}
				if d not in h:h.update({d:Æ,n:Ç})
			if A.openapi_extra:M(L,A.openapi_extra)
			u[j.lower()]=L
	return u,w,h
def x(routes:h[U]):
	C=[];B=[];D=[];F=[]
	for A in routes:
		if Q(A,µ,E)and S(A,P.APIRoute):
			if A.body_field:assert w(A.body_field),'A request body must be a Pydantic Field';C.append(A.body_field)
			if A.response_field:B.append(A.response_field)
			if A.response_fields:B.extend(A.response_fields.values())
			if A.callbacks:F.extend(x(A.callbacks))
			G=Ý(A.dependant);D.extend(G)
	H=F+b(C+B+D);return H
def Ö(*,title:B,version:B,openapi_version:B='3.1.0',summary:F[B]=E,description:F[B]=E,routes:h[U],webhooks:F[h[U]]=E,tags:F[N[C[B,D]]]=E,servers:F[N[C[B,j[B,D]]]]=E,terms_of_service:F[B]=E,contact:F[C[B,j[B,D]]]=E,license_info:F[C[B,j[B,D]]]=E,separate_input_output_schemas:a=G,external_docs:F[C[B,D]]=E):
	l='securitySchemes';f=external_docs;e=license_info;d=contact;c=terms_of_service;a=servers;Z=webhooks;Y=routes;X=description;W=summary;N=separate_input_output_schemas;E={T:title,'version':version}
	if W:E[À]=W
	if X:E[R]=X
	if c:E['termsOfService']=c
	if d:E['contact']=d
	if e:E['license']=e
	A={'openapi':openapi_version,'info':E}
	if a:A['servers']=a
	F={};g={};O={};h=set();j=x(b(Y or[])+b(Z or[]));Q=Á(j);k,H=Â(fields=j,model_name_map=Q,separate_input_output_schemas=N)
	for U in Y or[]:
		if S(U,P.APIRoute):
			I=m(route=U,operation_ids=h,model_name_map=Q,field_mapping=k,separate_input_output_schemas=N)
			if I:
				J,K,M=I
				if J:g.setdefault(U.path_format,{}).update(J)
				if K:F.setdefault(l,{}).update(K)
				if M:H.update(M)
	for V in Z or[]:
		if S(V,P.APIRoute):
			I=m(route=V,operation_ids=h,model_name_map=Q,field_mapping=k,separate_input_output_schemas=N)
			if I:
				J,K,M=I
				if J:O.setdefault(V.path_format,{}).update(J)
				if K:F.setdefault(l,{}).update(K)
				if M:H.update(M)
	if H:F['schemas']={A:H[A]for A in sorted(H)}
	if F:A['components']=F
	A['paths']=g
	if O:A['webhooks']=O
	if tags:A['tags']=tags
	if f:A['externalDocs']=f
	return L(Î(**A),by_alias=G,exclude_none=G)