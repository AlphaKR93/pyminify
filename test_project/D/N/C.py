Ç='bearer'
Æ='schema'
Ä='cookie'
Ã='header'
Â='string'
Á='email-validator not installed, email fields will be treated as str.\nTo install, run: pip install email-validator'
r='$ref'
f='allow'
a=float
Y=classmethod
V='type'
R=int
N=bool
L='SchemaOrBool'
D=str
C=None
from enum import Enum as g
from typing import Any as M,Callable as s,Dict as E,List as K,Optional as B,Set,Type,Union as G
from D.B import PYDANTIC_V2 as t,j,m,_model_rebuild as h,A
from D.L import I
from pydantic import AnyUrl as W,BaseModel as i,Field as F
from typing_extensions import Annotated as u,Literal as v,TypedDict as É
from typing_extensions import deprecated as Ê
try:import email_validator as Ë;assert Ë;from pydantic import EmailStr as w
except ImportError:
	class w(D):
		@Y
		def __get_validators__(cls):yield cls.validate
		@Y
		def validate(cls,v:M):I.warning(Á);return D(v)
		@Y
		def _validate(cls,__input_value:M,_:M):I.warning(Á);return D(__input_value)
		@Y
		def __get_pydantic_json_schema__(cls,core_schema:j,handler:m):return{V:Â,'format':'email'}
		@Y
		def __get_pydantic_core_schema__(cls,source:Type[M],handler:s[[M],j]):return A(cls._validate)
class H(i):
	if t:model_config={'extra':f}
	else:
		class Config:extra=f
class Ì(H):name:B[D]=C;url:B[W]=C;email:B[w]=C
class Í(H):name:D;identifier:B[D]=C;url:B[W]=C
class Ï(H):title:D;summary:B[D]=C;description:B[D]=C;termsOfService:B[D]=C;contact:B[Ì]=C;license:B[Í]=C;version:D
class Ð(H):enum:u[B[K[D]],F(min_length=1)]=C;default:D;description:B[D]=C
class b(H):url:G[W,D];description:B[D]=C;variables:B[E[D,Ð]]=C
class J(i):ref:D=F(alias=r)
class Ñ(i):propertyName:D;mapping:B[E[D,D]]=C
class Ò(H):name:B[D]=C;namespace:B[D]=C;prefix:B[D]=C;attribute:B[N]=C;wrapped:B[N]=C
class c(H):description:B[D]=C;url:W
x=v['array','boolean','integer','null','number','object',Â]
class X(H):schema_:B[D]=F(default=C,alias='$schema');vocabulary:B[D]=F(default=C,alias='$vocabulary');id:B[D]=F(default=C,alias='$id');anchor:B[D]=F(default=C,alias='$anchor');dynamicAnchor:B[D]=F(default=C,alias='$dynamicAnchor');ref:B[D]=F(default=C,alias=r);dynamicRef:B[D]=F(default=C,alias='$dynamicRef');defs:B[E[D,L]]=F(default=C,alias='$defs');comment:B[D]=F(default=C,alias='$comment');allOf:B[K[L]]=C;anyOf:B[K[L]]=C;oneOf:B[K[L]]=C;not_:B[L]=F(default=C,alias='not');if_:B[L]=F(default=C,alias='if');then:B[L]=C;else_:B[L]=F(default=C,alias='else');dependentSchemas:B[E[D,L]]=C;prefixItems:B[K[L]]=C;items:B[G[L,K[L]]]=C;contains:B[L]=C;properties:B[E[D,L]]=C;patternProperties:B[E[D,L]]=C;additionalProperties:B[L]=C;propertyNames:B[L]=C;unevaluatedItems:B[L]=C;unevaluatedProperties:B[L]=C;type:B[G[x,K[x]]]=C;enum:B[K[M]]=C;const:B[M]=C;multipleOf:B[a]=F(default=C,gt=0);maximum:B[a]=C;exclusiveMaximum:B[a]=C;minimum:B[a]=C;exclusiveMinimum:B[a]=C;maxLength:B[R]=F(default=C,ge=0);minLength:B[R]=F(default=C,ge=0);pattern:B[D]=C;maxItems:B[R]=F(default=C,ge=0);minItems:B[R]=F(default=C,ge=0);uniqueItems:B[N]=C;maxContains:B[R]=F(default=C,ge=0);minContains:B[R]=F(default=C,ge=0);maxProperties:B[R]=F(default=C,ge=0);minProperties:B[R]=F(default=C,ge=0);required:B[K[D]]=C;dependentRequired:B[E[D,Set[D]]]=C;format:B[D]=C;contentEncoding:B[D]=C;contentMediaType:B[D]=C;contentSchema:B[L]=C;title:B[D]=C;description:B[D]=C;default:B[M]=C;deprecated:B[N]=C;readOnly:B[N]=C;writeOnly:B[N]=C;examples:B[K[M]]=C;discriminator:B[Ñ]=C;xml:B[Ò]=C;externalDocs:B[c]=C;example:u[B[M],Ê('Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.')]=C
Ü=G[X,N]
class Å(É,total=False):
	summary:B[D];description:B[D];value:B[M];externalValue:B[W]
	if t:__pydantic_config__={'extra':f}
	else:
		class Config:extra=f
class Ó(g):query='query';header=Ã;path='path';cookie=Ä
class y(H):contentType:B[D]=C;headers:B[E[D,G['Header',J]]]=C;style:B[D]=C;explode:B[N]=C;allowReserved:B[N]=C
class k(H):schema_:B[G[X,J]]=F(default=C,alias=Æ);example:B[M]=C;examples:B[E[D,G[Å,J]]]=C;encoding:B[E[D,y]]=C
class z(H):description:B[D]=C;required:B[N]=C;deprecated:B[N]=C;style:B[D]=C;explode:B[N]=C;allowReserved:B[N]=C;schema_:B[G[X,J]]=F(default=C,alias=Æ);example:B[M]=C;examples:B[E[D,G[Å,J]]]=C;content:B[E[D,k]]=C
class n(z):name:D;in_:Ó=F(alias='in')
class ª(z):0
class µ(H):description:B[D]=C;content:E[D,k];required:B[N]=C
class º(H):operationRef:B[D]=C;operationId:B[D]=C;parameters:B[E[D,G[M,D]]]=C;requestBody:B[G[M,D]]=C;description:B[D]=C;server:B[b]=C
class À(H):description:D;headers:B[E[D,G[ª,J]]]=C;content:B[E[D,k]]=C;links:B[E[D,G[º,J]]]=C
class O(H):tags:B[K[D]]=C;summary:B[D]=C;description:B[D]=C;externalDocs:B[c]=C;operationId:B[D]=C;parameters:B[K[G[n,J]]]=C;requestBody:B[G[µ,J]]=C;responses:B[E[D,G[À,M]]]=C;callbacks:B[E[D,G[E[D,'PathItem'],J]]]=C;deprecated:B[N]=C;security:B[K[E[D,K[D]]]]=C;servers:B[K[b]]=C
class d(H):ref:B[D]=F(default=C,alias=r);summary:B[D]=C;description:B[D]=C;get:B[O]=C;put:B[O]=C;post:B[O]=C;delete:B[O]=C;options:B[O]=C;head:B[O]=C;patch:B[O]=C;trace:B[O]=C;servers:B[K[b]]=C;parameters:B[K[G[n,J]]]=C
class P(g):apiKey='apiKey';http='http';oauth2='oauth2';openIdConnect='openIdConnect'
class T(H):type_:P=F(alias=V);description:B[D]=C
class Z(g):query='query';header=Ã;cookie=Ä
class Q(T):type_:P=F(default=P.apiKey,alias=V);in_:Z=F(alias='in');name:D
class U(T):type_:P=F(default=P.http,alias=V);scheme:D
class o(U):scheme:v[Ç]=Ç;bearerFormat:B[D]=C
class e(H):refreshUrl:B[D]=C;scopes:E[D,D]={}
class Ô(e):authorizationUrl:D
class Õ(e):tokenUrl:D
class Ö(e):tokenUrl:D
class Ø(e):authorizationUrl:D;tokenUrl:D
class S(H):implicit:B[Ô]=C;password:B[Õ]=C;clientCredentials:B[Ö]=C;authorizationCode:B[Ø]=C
class p(T):type_:P=F(default=P.oauth2,alias=V);flows:S
class q(T):type_:P=F(default=P.openIdConnect,alias=V);openIdConnectUrl:D
Ù=G[Q,U,p,q,o]
class Ú(H):schemas:B[E[D,G[X,J]]]=C;responses:B[E[D,G[À,J]]]=C;parameters:B[E[D,G[n,J]]]=C;examples:B[E[D,G[Å,J]]]=C;requestBodies:B[E[D,G[µ,J]]]=C;headers:B[E[D,G[ª,J]]]=C;securitySchemes:B[E[D,G[Ù,J]]]=C;links:B[E[D,G[º,J]]]=C;callbacks:B[E[D,G[E[D,d],J,M]]]=C;pathItems:B[E[D,G[d,J]]]=C
class Û(H):name:D;description:B[D]=C;externalDocs:B[c]=C
class Î(H):openapi:D;info:Ï;jsonSchemaDialect:B[D]=C;servers:B[K[b]]=C;paths:B[E[D,G[d,M]]]=C;webhooks:B[E[D,G[d,J]]]=C;components:B[Ú]=C;security:B[K[E[D,K[D]]]]=C;tags:B[K[Û]]=C;externalDocs:B[c]=C
h(X)
h(O)
h(y)