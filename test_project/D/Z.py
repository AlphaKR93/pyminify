f='\\W'
e='auto'
d='validation'
c='default'
b=RuntimeError
V='1'
U=list
F=isinstance
A=str
C=None
import re,warnings as g
from dataclasses import is_dataclass as h
from typing import Any as B,Dict as Q,MutableMapping as W,Optional as L,Type as G,Union as H,cast
from weakref import WeakKeyDictionary as j
import D as R
from D.B import x,n,ă,o,Ă,p,q,r,Ą,may_v1 as S
from D.G import J,E
from pydantic import BaseModel as P
from pydantic.fields import FieldInfo as X
from typing_extensions import Literal as Y
k=j()
def I(status_code:H[int,A,C]):
	A=status_code
	if A is C:return True
	if A in{c,'1XX','2XX','3XX','4XX','5XX'}:return True
	B=int(A);return not(B<200 or B in{204,205,304})
def a(path:A):return set(re.findall('{(.*?)}',path))
T='Invalid args for response field! Hint: check that {type_} is a valid Pydantic field type. If you are using a return type annotation that is not a valid Pydantic field (e.g. Union[Response, dict, None]) you can disable generating the response model from the type annotation with the path operation decorator parameter response_model=None. Read more: https://fastapi.tiangolo.com/tutorial/response-model/'
def K(name:A,type_:B,class_validators:L[Q[A,q]]=C,default:L[B]=Ă,required:H[bool,p]=Ă,model_config:H[G[n],C]=C,field_info:L[X]=C,alias:L[A]=C,mode:Y[d,'serialization']=d,version:Y[V,e]=e):
	J='field_info';I='name';G=alias;E=default;D=class_validators;B=type_;A=field_info;D=D or{};K=S.BaseConfig;L=A or S.FieldInfo();H={I:name,J:L,'type_':B,'class_validators':D,c:E,'required':required,'model_config':K,'alias':G}
	if r(B)or F(A,S.FieldInfo)or version==V:
		from D.B import v1
		try:return v1.ModelField(**H)
		except b:raise R.exceptions.FastAPIError(T)from C
	elif x:
		from.B import v2;A=A or X(annotation=B,default=E,alias=G);M={'mode':mode,I:name,J:A}
		try:return v2.ModelField(**M)
		except o:raise R.exceptions.FastAPIError(T)from C
	from D.B import v1
	try:return v1.ModelField(**H)
	except b:raise R.exceptions.FastAPIError(T)from C
def N(field:ă,*,cloned_types:L[W[G[P],G[P]]]=C):
	E=cloned_types;A=field
	if x:
		from.B import v2
		if F(A,v2.ModelField):return A
	from D.B import v1
	if E is C:E=k
	D=A.type_
	if h(D)and hasattr(D,'__pydantic_model__'):D=D.__pydantic_model__
	H=D
	if Ą(D,v1.BaseModel):
		D=D;H=E.get(D)
		if H is C:
			H=v1.create_model(D.__name__,__base__=D);E[D]=H
			for I in D.__fields__.values():H.__fields__[I.name]=N(I,cloned_types=E)
	B=K(name=A.name,type_=H,version=V);B.has_alias=A.has_alias;B.alias=A.alias;B.class_validators=A.class_validators;B.default=A.default;B.default_factory=A.default_factory;B.required=A.required;B.model_config=A.model_config;B.field_info=A.field_info;B.allow_none=A.allow_none;B.validate_always=A.validate_always
	if A.sub_fields:B.sub_fields=[N(A,cloned_types=E)for A in A.sub_fields]
	if A.key_field:B.key_field=N(A.key_field,cloned_types=E)
	B.validators=A.validators;B.pre_validators=A.pre_validators;B.post_validators=A.post_validators;B.parse_json=A.parse_json;B.shape=A.shape;B.populate_validators();return B
def Z(*,name:A,path:A,method:A):g.warn('fastapi.utils.generate_operation_id_for_path() was deprecated, it is not used internally, and will be removed soon',DeprecationWarning,stacklevel=2);A=f"{name}{path}";A=re.sub(f,'_',A);A=f"{A}_{method.lower()}";return A
def D(route):B=route;A=f"{B.name}{B.path_format}";A=re.sub(f,'_',A);assert B.methods;A=f"{A}_{U(B.methods)[0].lower()}";return A
def M(main_dict:Q[B,B],update_dict:Q[B,B]):
	C=update_dict;B=main_dict
	for(A,D)in C.items():
		if A in B and F(B[A],dict)and F(D,dict):M(B[A],D)
		elif A in B and F(B[A],U)and F(C[A],U):B[A]=B[A]+C[A]
		else:B[A]=D
def O(first_item:H[J,E],*C:H[J,E]):
	A=first_item;D=(A,)+C
	for B in D:
		if not F(B,J):return B
	return A