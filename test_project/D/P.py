k='regex'
j='pattern'
i='json_schema_extra'
h='strict'
f='serialization_alias'
e='validation_alias'
d='alias_priority'
c='annotation'
b='deprecated'
a='`regex` has been deprecated, please use `pattern` instead'
Z='examples'
Y='`example` has been deprecated, please use `examples` instead'
U=DeprecationWarning
R='Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.'
Q='Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead.'
N=True
I=bool
H=float
G=int
D=str
A=None
import warnings as S
from dataclasses import dataclass as W
from enum import Enum
from typing import Any as F,Callable as O,Dict as K,List as P,Optional as B,Sequence as l,Union as C
from D.N.C import Å
from pydantic.fields import FieldInfo as X
from typing_extensions import Annotated as L,Literal as m,deprecated as J
from.B import x,u,Ă
E=Ă
class g(Enum):query='query';header='header';path='path';cookie='cookie'
class T(X):
	in_:g
	def __init__(C,default:F=Ă,*,default_factory:C[O[[],F],A]=E,annotation:B[F]=A,alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(Q)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[P[F]]=A,example:L[B[F],J(R)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=N,json_schema_extra:C[K[D,F],A]=A,**K:F):
		J=deprecated;I=example;H=examples;G=pattern;D=regex
		if I is not E:S.warn(Y,category=U,stacklevel=4)
		C.example=I;C.include_in_schema=include_in_schema;C.openapi_examples=openapi_examples;B=dict(default=default,default_factory=default_factory,alias=alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,discriminator=discriminator,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,**K)
		if H is not A:B[Z]=H
		if D is not A:S.warn(a,category=U,stacklevel=4)
		L=json_schema_extra or K
		if u<(2,7):C.deprecated=J
		else:B[b]=J
		if x:B.update({c:annotation,d:alias_priority,e:validation_alias,f:serialization_alias,h:strict,i:L});B[j]=G or D
		else:B[k]=G or D;B.update(**L)
		M={B:A for(B,A)in B.items()if A is not E};super().__init__(**M)
	def __repr__(A):return f"{A.__class__.__name__}({A.default})"
class o(T):
	in_=g.path
	def __init__(A,default:F=...,*,default_factory:C[O[[],F],A]=E,annotation:B[F]=A,alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(Q)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[P[F]]=A,example:L[B[F],J(R)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=N,json_schema_extra:C[K[D,F],A]=A,**C:F):B=default;assert B is...,'Path parameters cannot have a default value';A.in_=A.in_;super().__init__(default=B,default_factory=default_factory,annotation=annotation,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**C)
class p(T):
	in_=g.query
	def __init__(B,default:F=Ă,*,default_factory:C[O[[],F],A]=E,annotation:B[F]=A,alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(Q)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[P[F]]=A,example:L[B[F],J(R)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=N,json_schema_extra:C[K[D,F],A]=A,**A:F):super().__init__(default=default,default_factory=default_factory,annotation=annotation,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**A)
class q(T):
	in_=g.header
	def __init__(A,default:F=Ă,*,default_factory:C[O[[],F],A]=E,annotation:B[F]=A,alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,convert_underscores:I=N,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(Q)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[P[F]]=A,example:L[B[F],J(R)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=N,json_schema_extra:C[K[D,F],A]=A,**B:F):A.convert_underscores=convert_underscores;super().__init__(default=default,default_factory=default_factory,annotation=annotation,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**B)
class r(T):
	in_=g.cookie
	def __init__(B,default:F=Ă,*,default_factory:C[O[[],F],A]=E,annotation:B[F]=A,alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(Q)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[P[F]]=A,example:L[B[F],J(R)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=N,json_schema_extra:C[K[D,F],A]=A,**A:F):super().__init__(default=default,default_factory=default_factory,annotation=annotation,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**A)
class V(X):
	def __init__(C,default:F=Ă,*,default_factory:C[O[[],F],A]=E,annotation:B[F]=A,embed:C[I,A]=A,media_type:D='application/json',alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(Q)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[P[F]]=A,example:L[B[F],J(R)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=N,json_schema_extra:C[K[D,F],A]=A,**K:F):
		J=deprecated;I=example;H=examples;G=pattern;D=regex;C.embed=embed;C.media_type=media_type
		if I is not E:S.warn(Y,category=U,stacklevel=4)
		C.example=I;C.include_in_schema=include_in_schema;C.openapi_examples=openapi_examples;B=dict(default=default,default_factory=default_factory,alias=alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,discriminator=discriminator,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,**K)
		if H is not A:B[Z]=H
		if D is not A:S.warn(a,category=U,stacklevel=4)
		L=json_schema_extra or K
		if u<(2,7):C.deprecated=J
		else:B[b]=J
		if x:B.update({c:annotation,d:alias_priority,e:validation_alias,f:serialization_alias,h:strict,i:L});B[j]=G or D
		else:B[k]=G or D;B.update(**L)
		M={B:A for(B,A)in B.items()if A is not E};super().__init__(**M)
	def __repr__(A):return f"{A.__class__.__name__}({A.default})"
class n(V):
	def __init__(B,default:F=Ă,*,default_factory:C[O[[],F],A]=E,annotation:B[F]=A,media_type:D='application/x-www-form-urlencoded',alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(Q)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[P[F]]=A,example:L[B[F],J(R)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=N,json_schema_extra:C[K[D,F],A]=A,**A:F):super().__init__(default=default,default_factory=default_factory,annotation=annotation,media_type=media_type,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**A)
class s(n):
	def __init__(B,default:F=Ă,*,default_factory:C[O[[],F],A]=E,annotation:B[F]=A,media_type:D='multipart/form-data',alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(Q)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[P[F]]=A,example:L[B[F],J(R)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=N,json_schema_extra:C[K[D,F],A]=A,**A:F):super().__init__(default=default,default_factory=default_factory,annotation=annotation,media_type=media_type,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**A)
@W(frozen=N)
class M:dependency:B[O[...,F]]=A;use_cache:I=N;scope:C[m['function','request'],A]=A
@W(frozen=N)
class t(M):scopes:B[l[D]]=A