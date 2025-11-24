À='BaseModel'
º='python'
h=list
c='json'
b=set
a=property
V=False
U=True
T='serialization'
S=isinstance
P='$ref'
N='validation'
G=bool
F=None
C=str
import re,warnings as i
from copy import copy,deepcopy as Á
from dataclasses import dataclass as Â
from enum import Enum as d
from typing import Any as B,Dict as E,Sequence as W,Set,Tuple as H,Type as O,Union as L,cast as n
from D.B import may_v1,shared as M
from D.N.A import à
from D.Y import x,A
from pydantic import BaseModel as J,TypeAdapter as o,create_model as X
from pydantic import ValidationError as Q
from pydantic._internal._typing_extra import eval_type_lenient as Ã
from pydantic._internal._utils import lenient_issubclass as Y
from pydantic.fields import FieldInfo as j
from pydantic.json_schema import GenerateJsonSchema as Ä
from pydantic.json_schema import JsonSchemaValue as R
from pydantic_core import PydanticUndefined as q,PydanticUndefinedType as Å
from typing_extensions import Annotated as Æ,Literal as I,get_args as Ç,get_origin as s
try:0
except ImportError:pass
t=q
l=q
u=Å
v=Ã
w=B
class y:0
class Ï(Exception):0
@Â
class D:
	field_info:j;name:C;mode:I[N,T]=N
	@a
	def alias(self):A=self.field_info.alias;return A if A is not F else self.name
	@a
	def required(self):return self.field_info.is_required()
	@a
	def default(self):return self.get_default()
	@a
	def type_(self):return self.field_info.annotation
	def __post_init__(A):
		with i.catch_warnings():
			if M.PYDANTIC_VERSION_MINOR_TUPLE>=(2,12):from pydantic.warnings import UnsupportedFieldAttributeWarning as C;i.simplefilter('ignore',category=C)
			A._type_adapter=o(Æ[A.field_info.annotation,A.field_info])
	def get_default(A):
		if A.field_info.is_required():return l
		return A.field_info.get_default(call_default_factory=U)
	def validate(A,value:B,values:E[C,B]={},*,loc:H[L[int,C],...]=()):
		try:return A._type_adapter.validate_python(value,from_attributes=U),F
		except Q as B:return F,may_v1._regenerate_error_with_loc(errors=B.errors(include_url=V),loc_prefix=loc)
	def serialize(A,value:B,*,mode:I[c,º]=c,include:L[x,F]=F,exclude:L[x,F]=F,by_alias:G=U,exclude_unset:G=V,exclude_defaults:G=V,exclude_none:G=V):return A._type_adapter.dump_python(value,mode=mode,include=include,exclude=exclude,by_alias=by_alias,exclude_unset=exclude_unset,exclude_defaults=exclude_defaults,exclude_none=exclude_none)
	def __hash__(A):return id(A)
def Ð(annotation:B,field_info:j,field_name:C):return annotation
def Ñ(model:O[J]):model.model_rebuild()
def Ò(model:J,mode:I[c,º]=c,**A:B):return model.model_dump(mode=mode,**A)
def Ó(model:J):return model.model_config
def Ô(*,field:D,model_name_map:A,field_mapping:E[H[D,I[N,T]],R],separate_input_output_schemas:G=U):
	A=field;C=F if separate_input_output_schemas else N;B=field_mapping[A,C or A.mode]
	if P not in B:B['title']=A.field_info.title or A.alias.title().replace('_',' ')
	return B
def Õ(*,fields:W[D],model_name_map:A,separate_input_output_schemas:G=U):
	H='description';A=fields;K=Ä(ref_template=à);M=F if separate_input_output_schemas else N;O=[A for A in A if A.mode==N];P=[A for A in A if A.mode==T];Q=f(O,known_models=b());R=f(P,known_models=b());S=[D(field_info=j(annotation=A),name=A.__name__,mode=N)for A in Q];U=[D(field_info=j(annotation=A),name=A.__name__,mode=T)for A in R];V=S+U;W={A.type_ for A in A};X={A for A in V if A.type_ not in W};Y=[(A,M or A.mode,A._type_adapter.core_schema)for A in h(A)+h(X)];Z,J=K.generate_definitions(inputs=Y)
	for G in J.values():
		if H in G:a=G[H].split('\x0c')[0];G[H]=a
	c,d=È(model_name_map=model_name_map,definitions=J,field_mapping=Z);return c,d
def Z(*,schema:E[C,B],old_name_to_new_name_map:E[C,C]):
	E=schema;D=old_name_to_new_name_map;B=Á(E)
	for(F,A)in B.items():
		if F==P:
			A=E[P]
			if S(A,C):
				I=E[P].split('/')[-1]
				if I in D:J=D[I];B[P]=à.format(model=J)
			continue
		if S(A,dict):B[F]=Z(schema=A,old_name_to_new_name_map=D)
		elif S(A,h):
			G=[]
			for H in A:
				if S(H,dict):K=Z(schema=H,old_name_to_new_name_map=D);G.append(K)
				else:G.append(H)
			B[F]=G
	return B
def È(*,model_name_map:A,definitions:E[C,B],field_mapping:E[H[D,I[N,T]],R]):
	K=field_mapping;J=model_name_map;A={}
	for(B,C)in K.items():
		L=B[0].type_
		if L not in J:continue
		F=J[L];M=C[P].split('/')[-1]
		if M in{f"{F}-Input",f"{F}-Output"}:continue
		A[M]=F
	N={}
	for(B,C)in K.items():S=Z(schema=C,old_name_to_new_name_map=A);N[B]=S
	O={}
	for(G,T)in definitions.items():
		if G in A:Q=A[G]
		else:Q=G
		U=Z(schema=T,old_name_to_new_name_map=A);O[Q]=U
	return N,O
def Ö(field:D):A=field;from D import params as B;return M.field_annotation_is_scalar(A.field_info.annotation)and not S(A.field_info,B.Body)
def Ø(field:D):return M.field_annotation_is_sequence(field.field_info.annotation)
def Ù(field:D):return M.field_annotation_is_scalar_sequence(field.field_info.annotation)
def Ú(field:D):return M.is_bytes_or_nonable_bytes_annotation(field.type_)
def Û(field:D):return M.is_bytes_sequence_annotation(field.type_)
def Ü(*,field_info:j,annotation:B):B=field_info;D=type(B);C=D.from_annotation(annotation);A=copy(B);A.metadata=C.metadata;A.annotation=C.annotation;return A
def Ý(*,field:D,value:B):A=field;B=s(A.field_info.annotation)or A.field_info.annotation;assert issubclass(B,M.sequence_types);return M.sequence_annotation_to_type[B](value)
def ª(loc:H[C,...]):B='input';A=Q.from_exception_data('Field required',[{'type':'missing','loc':loc,B:{}}]).errors(include_url=V)[0];A[B]=F;return A
def Þ(*,fields:W[D],model_name:C):A={A.name:(A.field_info.annotation,A.field_info)for A in fields};B=X(model_name,**A);return B
def É(model:O[J]):return[D(field_info=B,name=A)for(A,B)in model.model_fields.items()]
e=L[O[À],O[d]]
K=Set[e]
def Ê(name:C):return re.sub('[^a-zA-Z0-9.\\-_]','_',name)
def ß(unique_models:K):
	A={};E=b()
	for D in unique_models:
		B=Ê(D.__name__)
		if B in E:B=g(D);A[B]=D
		elif B in A:E.add(B);F=A.pop(B);A[g(F)]=F;A[g(D)]=D
		else:A[B]=D
	return{B:A for(A,B)in A.items()}
def z(model:O[À],known_models:L[K,F]=F):A=known_models;A=A or b();B=É(model);f(B,known_models=A);return A
def µ(annotation:B,known_models:K):
	C=annotation;B=known_models;D=s(C)
	if D is not F:
		for A in Ç(C):
			if Y(A,(J,d))and A not in B:
				B.add(A)
				if Y(A,J):z(A,known_models=B)
			else:µ(A,known_models=B)
	return B
def Ë(field:D,known_models:K):
	A=known_models;B=field.type_
	if Y(B,J):
		if B in A:return A
		A.add(B);z(B,known_models=A)
	elif Y(B,d):A.add(B)
	else:µ(B,known_models=A)
	return A
def f(fields:W[D],known_models:K):
	A=known_models
	for B in fields:Ë(B,known_models=A)
	return A
def g(model:e):A=model;return f"{A.__module__}__{A.__qualname__}".replace('.','__')