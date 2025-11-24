Q='json'
O=set
J=False
I=str
F=True
E=bool
C=isinstance
from functools import lru_cache as R
from typing import Any as D,Dict as G,List as K,Sequence as P,Tuple as L,Type as M
from D.B import may_v1 as B
from D.B.D import x,Ą
from D.Y import A
from pydantic import BaseModel as H
from typing_extensions import Literal as N
from.C import ă
if x:from.F import j
else:from.E import FieldInfo as j
@R
def S(model:M[H]):
	A=model
	if Ą(A,B.BaseModel):from D.B import v1;return v1.get_model_fields(A)
	else:from.import v2;return v2.get_model_fields(A)
def z(value:object):
	A=value
	if C(A,B.UndefinedType):return F
	elif x:from.import v2;return C(A,v2.UndefinedType)
	return J
def ā(model:H):
	A=model
	if C(A,B.BaseModel):from D.B import v1;return v1._get_model_config(A)
	elif x:from.import v2;return v2._get_model_config(A)
def Ā(model:H,mode:N[Q,'python']=Q,**E:D):
	A=model
	if C(A,B.BaseModel):from D.B import v1;return v1._model_dump(A,mode=mode,**E)
	elif x:from.import v2;return v2._model_dump(A,mode=mode,**E)
def T(exc:Exception):
	if C(exc,B.ErrorWrapper):return F
	elif x:from.import v2;return C(exc,v2.ErrorWrapper)
	return J
def U(*,field_info:j,annotation:D):
	D=annotation;A=field_info
	if C(A,B.FieldInfo):from D.B import v1;return v1.copy_field_info(field_info=A,annotation=D)
	else:assert x;from.import v2;return v2.copy_field_info(field_info=A,annotation=D)
def V(*,fields:P[ă],model_name:I):
	D=model_name;A=fields
	if A and C(A[0],B.ModelField):from D.B import v1;return v1.create_body_model(fields=A,model_name=D)
	else:assert x;from.import v2;return v2.create_body_model(fields=A,model_name=D)
def W(annotation:D,field_info:j,field_name:I):
	E=field_name;D=annotation;A=field_info
	if C(A,B.FieldInfo):from D.B import v1;return v1.get_annotation_from_field_info(annotation=D,field_info=A,field_name=E)
	else:assert x;from.import v2;return v2.get_annotation_from_field_info(annotation=D,field_info=A,field_name=E)
def X(field:ă):
	A=field
	if C(A,B.ModelField):from D.B import v1;return v1.is_bytes_field(A)
	else:assert x;from.import v2;return v2.is_bytes_field(A)
def Y(field:ă):
	A=field
	if C(A,B.ModelField):from D.B import v1;return v1.is_bytes_sequence_field(A)
	else:assert x;from.import v2;return v2.is_bytes_sequence_field(A)
def Z(field:ă):
	A=field
	if C(A,B.ModelField):from D.B import v1;return v1.is_scalar_field(A)
	else:assert x;from.import v2;return v2.is_scalar_field(A)
def a(field:ă):
	A=field
	if C(A,B.ModelField):from D.B import v1;return v1.is_scalar_sequence_field(A)
	else:assert x;from.import v2;return v2.is_scalar_sequence_field(A)
def b(field:ă):
	A=field
	if C(A,B.ModelField):from D.B import v1;return v1.is_sequence_field(A)
	else:assert x;from.import v2;return v2.is_sequence_field(A)
def c(*,field:ă,value:D):
	D=value;A=field
	if C(A,B.ModelField):from D.B import v1;return v1.serialize_sequence_value(field=A,value=D)
	else:assert x;from.import v2;return v2.serialize_sequence_value(field=A,value=D)
def d(model:M[H]):
	A=model
	if Ą(A,B.BaseModel):from D.B import v1;v1._model_rebuild(A)
	elif x:from.import v2;v2._model_rebuild(A)
def e(fields:K[ă]):
	E=fields;F=[A for A in E if C(A,B.ModelField)]
	if F:from D.B import v1;G=v1.get_flat_models_from_fields(F,known_models=O());A=G
	else:A=O()
	if x:from.import v2;H=[A for A in E if C(A,v2.ModelField)];I=v2.get_flat_models_from_fields(H,known_models=O());A=A.union(I);D=v2.get_model_name_map(A);return D
	from D.B import v1;D=v1.get_model_name_map(A);return D
def f(*,fields:K[ă],model_name_map:A,separate_input_output_schemas:E=F):
	E=separate_input_output_schemas;D=model_name_map;A=fields;K=[A for A in A if C(A,B.ModelField)];I,J=B.get_definitions(fields=K,model_name_map=D,separate_input_output_schemas=E)
	if not x:return I,J
	else:from.import v2;F=[A for A in A if C(A,v2.ModelField)];G,H=v2.get_definitions(fields=F,model_name_map=D,separate_input_output_schemas=E);L={**J,**H};M={**I,**G};return M,L
def g(*,field:ă,model_name_map:A,field_mapping:G[L[ă,N['validation','serialization']],B.JsonSchemaValue],separate_input_output_schemas:E=F):
	F=separate_input_output_schemas;E=field_mapping;D=model_name_map;A=field
	if C(A,B.ModelField):from D.B import v1;return v1.get_schema_from_model_field(field=A,model_name_map=D,field_mapping=E,separate_input_output_schemas=F)
	else:assert x;from.import v2;return v2.get_schema_from_model_field(field=A,model_name_map=D,field_mapping=E,separate_input_output_schemas=F)
def h(value:D):
	A=value
	if C(A,B.ModelField):return F
	elif x:from.import v2;return C(A,v2.ModelField)
	return J
def i(value:D):
	A=value
	if Ą(A,B.BaseModel):return F
	elif x:from.import v2;return Ą(A,v2.BaseModel)
	return J