Y='regex'
X='deprecated'
W='`regex` has been deprecated, please use `pattern` instead'
V='examples'
U='`example` has been deprecated, please use `examples` instead'
T=DeprecationWarning
Q='Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.'
P='Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead.'
M=True
I=bool
H=float
G=int
D=str
A=None
import warnings as R
from typing import Any as F,Callable as N,Dict as K,List as O,Optional as B,Union as C
from D.N.C import Å
from D.P import g
from typing_extensions import Annotated as L,deprecated as J
from.B.B import i,h
from.B.D import u
E=h
class S(i):
	in_:g
	def __init__(C,default:F=h,*,default_factory:C[N[[],F],A]=E,annotation:B[F]=A,alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(P)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[O[F]]=A,example:L[B[F],J(Q)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=M,json_schema_extra:C[K[D,F],A]=A,**J:F):
		I=deprecated;H=example;G=examples;D=regex
		if H is not E:R.warn(U,category=T,stacklevel=4)
		C.example=H;C.include_in_schema=include_in_schema;C.openapi_examples=openapi_examples;B=dict(default=default,default_factory=default_factory,alias=alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,discriminator=discriminator,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,**J)
		if G is not A:B[V]=G
		if D is not A:R.warn(W,category=T,stacklevel=4)
		K=json_schema_extra or J
		if u<(2,7):C.deprecated=I
		else:B[X]=I
		B[Y]=pattern or D;B.update(**K);L={B:A for(B,A)in B.items()if A is not E};super().__init__(**L)
	def __repr__(A):return f"{A.__class__.__name__}({A.default})"
class b(S):
	in_=g.path
	def __init__(A,default:F=...,*,default_factory:C[N[[],F],A]=E,annotation:B[F]=A,alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(P)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[O[F]]=A,example:L[B[F],J(Q)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=M,json_schema_extra:C[K[D,F],A]=A,**C:F):B=default;assert B is...,'Path parameters cannot have a default value';A.in_=A.in_;super().__init__(default=B,default_factory=default_factory,annotation=annotation,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**C)
class c(S):
	in_=g.query
	def __init__(B,default:F=h,*,default_factory:C[N[[],F],A]=E,annotation:B[F]=A,alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(P)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[O[F]]=A,example:L[B[F],J(Q)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=M,json_schema_extra:C[K[D,F],A]=A,**A:F):super().__init__(default=default,default_factory=default_factory,annotation=annotation,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**A)
class d(S):
	in_=g.header
	def __init__(A,default:F=h,*,default_factory:C[N[[],F],A]=E,annotation:B[F]=A,alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,convert_underscores:I=M,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(P)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[O[F]]=A,example:L[B[F],J(Q)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=M,json_schema_extra:C[K[D,F],A]=A,**B:F):A.convert_underscores=convert_underscores;super().__init__(default=default,default_factory=default_factory,annotation=annotation,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**B)
class e(S):
	in_=g.cookie
	def __init__(B,default:F=h,*,default_factory:C[N[[],F],A]=E,annotation:B[F]=A,alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(P)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[O[F]]=A,example:L[B[F],J(Q)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=M,json_schema_extra:C[K[D,F],A]=A,**A:F):super().__init__(default=default,default_factory=default_factory,annotation=annotation,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**A)
class Z(i):
	def __init__(B,default:F=h,*,default_factory:C[N[[],F],A]=E,annotation:B[F]=A,embed:C[I,A]=A,media_type:D='application/json',alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(P)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[O[F]]=A,example:L[B[F],J(Q)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=M,json_schema_extra:C[K[D,F],A]=A,**J:F):
		I=deprecated;H=example;G=examples;D=regex;B.embed=embed;B.media_type=media_type
		if H is not E:R.warn(U,category=T,stacklevel=4)
		B.example=H;B.include_in_schema=include_in_schema;B.openapi_examples=openapi_examples;C=dict(default=default,default_factory=default_factory,alias=alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,discriminator=discriminator,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,**J)
		if G is not A:C[V]=G
		if D is not A:R.warn(W,category=T,stacklevel=4)
		K=json_schema_extra or J
		if u<(2,7):B.deprecated=I
		else:C[X]=I
		C[Y]=pattern or D;C.update(**K);L={B:A for(B,A)in C.items()if A is not E};super().__init__(**L)
	def __repr__(A):return f"{A.__class__.__name__}({A.default})"
class a(Z):
	def __init__(B,default:F=h,*,default_factory:C[N[[],F],A]=E,annotation:B[F]=A,media_type:D='application/x-www-form-urlencoded',alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(P)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[O[F]]=A,example:L[B[F],J(Q)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=M,json_schema_extra:C[K[D,F],A]=A,**A:F):super().__init__(default=default,default_factory=default_factory,annotation=annotation,media_type=media_type,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**A)
class f(a):
	def __init__(B,default:F=h,*,default_factory:C[N[[],F],A]=E,annotation:B[F]=A,media_type:D='multipart/form-data',alias:B[D]=A,alias_priority:C[G,A]=E,validation_alias:C[D,A]=A,serialization_alias:C[D,A]=A,title:B[D]=A,description:B[D]=A,gt:B[H]=A,ge:B[H]=A,lt:B[H]=A,le:B[H]=A,min_length:B[G]=A,max_length:B[G]=A,pattern:B[D]=A,regex:L[B[D],J(P)]=A,discriminator:C[D,A]=A,strict:C[I,A]=E,multiple_of:C[H,A]=E,allow_inf_nan:C[I,A]=E,max_digits:C[G,A]=E,decimal_places:C[G,A]=E,examples:B[O[F]]=A,example:L[B[F],J(Q)]=E,openapi_examples:B[K[D,Å]]=A,deprecated:C[J,D,I,A]=A,include_in_schema:I=M,json_schema_extra:C[K[D,F],A]=A,**A:F):super().__init__(default=default,default_factory=default_factory,annotation=annotation,media_type=media_type,alias=alias,alias_priority=alias_priority,validation_alias=validation_alias,serialization_alias=serialization_alias,title=title,description=description,gt=gt,ge=ge,lt=lt,le=le,min_length=min_length,max_length=max_length,pattern=pattern,regex=regex,discriminator=discriminator,strict=strict,multiple_of=multiple_of,allow_inf_nan=allow_inf_nan,max_digits=max_digits,decimal_places=decimal_places,deprecated=deprecated,example=example,examples=examples,openapi_examples=openapi_examples,include_in_schema=include_in_schema,json_schema_extra=json_schema_extra,**A)