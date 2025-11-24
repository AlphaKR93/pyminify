z=tuple
Q=False
K=list
I=True
H=None
E=bool
C=str
from copy import copy
from dataclasses import dataclass as ª,is_dataclass as µ
from enum import Enum as k
from typing import Any as B,Callable as º,Dict as D,List as l,Sequence as m,Set,Tuple as J,Type as F,Union as R
from D.B import shared as S
from D.N.A import ß
from D.Y import A
from pydantic.version import VERSION as À
from typing_extensions import Literal as T
Á=z(int(A)for A in À.split('.')[:2])
Â=Á[0]==2
n=Ellipsis
if not Â:from pydantic import BaseModel as M,ValidationError as o,create_model as V;from pydantic.error_wrappers import ErrorWrapper as N;from pydantic.errors import MissingError as p;from pydantic.fields import SHAPE_FROZENSET as q,SHAPE_LIST as X,SHAPE_SEQUENCE as Y,SHAPE_SET as Z,SHAPE_SINGLETON as r,SHAPE_TUPLE as a,SHAPE_TUPLE_ELLIPSIS as b;from pydantic.fields import FieldInfo as i;from pydantic.fields import ModelField as L;from pydantic.networks import AnyUrl as P;from pydantic.schema import field_schema as s,model_process_schema as t;from pydantic.schema import get_flat_models_from_fields as u;from pydantic.utils import lenient_issubclass as G
else:from pydantic.v1 import BaseModel as M,ValidationError as o,create_model as V;from pydantic.v1.error_wrappers import ErrorWrapper as N;from pydantic.v1.errors import MissingError as p;from pydantic.v1.fields import SHAPE_FROZENSET as q,SHAPE_LIST as X,SHAPE_SEQUENCE as Y,SHAPE_SET as Z,SHAPE_SINGLETON as r,SHAPE_TUPLE as a,SHAPE_TUPLE_ELLIPSIS as b;from pydantic.v1.fields import FieldInfo as i;from pydantic.v1.fields import ModelField as L;from pydantic.v1.networks import AnyUrl as P;from pydantic.v1.schema import field_schema as s,model_process_schema as t;from pydantic.v1.schema import get_flat_models_from_fields as u;from pydantic.v1.utils import lenient_issubclass as G
v=B
O=D[C,B]
w=B
x=P
g={X,Z,q,a,Y,b}
É={X:K,Z:set,a:z,Y:K,b:K}
@ª
class Í:ref_template:C
class Î(Exception):0
Ê=V('Request')
def Ï(function:º[...,B],*,ref:R[C,H]=H,metadata:B=H,serialization:B=H):return{}
def Ë(*,flat_models:Set[R[F[M],F[k]]],model_name_map:D[R[F[M],F[k]],C]):
	G=model_name_map;F='description';E={}
	for H in flat_models:A,I,K=t(H,model_name_map=G,ref_prefix=ß);E.update(I);J=G[H];E[J]=A
	for A in E.values():
		if F in A:A[F]=A[F].split('\x0c')[0]
	return E
def j(field:L):
	A=field;from D import params as B;C=A.field_info
	if not(A.shape==r and not G(A.type_,M)and not G(A.type_,dict)and not S.field_annotation_is_sequence(A.type_)and not µ(A.type_)and not isinstance(C,B.Body)):return Q
	if A.sub_fields:
		if not all(j(A)for A in A.sub_fields):return Q
	return I
def Ì(field:L):
	A=field
	if A.shape in g and not G(A.type_,M):
		if A.sub_fields is not H:
			for B in A.sub_fields:
				if not j(B):return Q
		return I
	if S._annotation_is_sequence(A.type_):return I
	return Q
def Ð(model:F[M]):model.update_forward_refs()
def Ñ(model:M,mode:T['json','python']='json',**A:B):return model.dict(**A)
def Ò(model:M):return model.__config__
def Ó(*,field:L,model_name_map:A,field_mapping:D[J[L,T['validation','serialization']],O],separate_input_output_schemas:E=I):return s(field,model_name_map=model_name_map,ref_prefix=ß)[0]
def y(*,fields:l[L],model_name_map:A,separate_input_output_schemas:E=I):A=u(fields,known_models=set());return{},Ë(flat_models=A,model_name_map=model_name_map)
def Ô(field:L):return j(field)
def Õ(field:L):A=field;return A.shape in g or S._annotation_is_sequence(A.type_)
def Ö(field:L):return Ì(field)
def Ø(field:L):return G(field.type_,bytes)
def Ù(field:L):A=field;return A.shape in g and G(A.type_,bytes)
def Ú(*,field_info:i,annotation:B):return copy(field_info)
def Û(*,field:L,value:B):return É[field.shape](value)
def Ü(loc:J[C,...]):A=N(p(),loc=loc);B=o([A],Ê);return B.errors()[0]
def Ý(*,fields:m[L],model_name:C):
	A=V(model_name)
	for B in fields:A.__fields__[B.name]=B
	return A
def Þ(model:F[M]):return K(model.__fields__.values())