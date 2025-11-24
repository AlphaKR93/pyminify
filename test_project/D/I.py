j=tuple
i=frozenset
Q=False
b=Exception
a=float
Z=int
U=dict
K=bool
S=list
O=type
I=None
H=set
D=isinstance
B=str
import dataclasses as e,datetime as F
from collections import defaultdict as W,deque as f
from decimal import Decimal as R
from enum import Enum as g
from ipaddress import IPv4Address as X,IPv4Interface as c,IPv4Network as d,IPv6Address as k,IPv6Interface as l,IPv6Network as m
from pathlib import Path,PurePath as p
from re import Pattern as n
from types import GeneratorType as h
from typing import Any as C,Callable as G,Dict as N,Optional as M,Union as V
from uuid import UUID
from annotated_doc import Doc as A
from D.B import may_v1 as J
from D.Y import x
from pydantic import BaseModel as q
from pydantic.color import Color
from pydantic.networks import AnyUrl as o,NameEmail as r
from pydantic.types import SecretBytes as s,SecretStr as t
from typing_extensions import Annotated as E
from.B import Url,z,Ā
def P(o:V[F.date,F.time]):return o.isoformat()
def u(dec_value:R):
	A=dec_value
	if A.as_tuple().exponent>=0:return Z(A)
	else:return a(A)
Y={bytes:lambda o:o.decode(),Color:B,J.Color:B,F.date:P,F.datetime:P,F.time:P,F.timedelta:lambda td:td.total_seconds(),R:u,g:lambda o:o.value,i:S,f:S,h:S,X:B,c:B,d:B,k:B,l:B,m:B,r:B,J.NameEmail:B,Path:B,n:lambda o:o.pattern,s:B,J.SecretBytes:B,t:B,J.SecretStr:B,H:S,UUID:B,Url:B,J.Url:B,o:B,J.AnyUrl:B}
def v(type_encoder_map:N[C,G[[C],C]]):
	A=W(j)
	for(B,D)in type_encoder_map.items():A[D]+=B,
	return A
w=v(Y)
def L(obj:E[C,A('\n            The input object to convert to JSON.\n            ')],include:E[M[x],A("\n            Pydantic's `include` parameter, passed to Pydantic models to set the\n            fields to include.\n            ")]=I,exclude:E[M[x],A("\n            Pydantic's `exclude` parameter, passed to Pydantic models to set the\n            fields to exclude.\n            ")]=I,by_alias:E[K,A("\n            Pydantic's `by_alias` parameter, passed to Pydantic models to define if\n            the output should use the alias names (when provided) or the Python\n            attribute names. In an API, if you set an alias, it's probably because you\n            want to use it in the result, so you probably want to leave this set to\n            `True`.\n            ")]=True,exclude_unset:E[K,A("\n            Pydantic's `exclude_unset` parameter, passed to Pydantic models to define\n            if it should exclude from the output the fields that were not explicitly\n            set (and that only had their default values).\n            ")]=Q,exclude_defaults:E[K,A("\n            Pydantic's `exclude_defaults` parameter, passed to Pydantic models to define\n            if it should exclude from the output the fields that had the same default\n            value, even when they were explicitly set.\n            ")]=Q,exclude_none:E[K,A("\n            Pydantic's `exclude_none` parameter, passed to Pydantic models to define\n            if it should exclude from the output any fields that have a `None` value.\n            ")]=Q,custom_encoder:E[M[N[C,G[[C],C]]],A("\n            Pydantic's `custom_encoder` parameter, passed to Pydantic models to define\n            a custom encoder.\n            ")]=I,sqlalchemy_safe:E[K,A("\n            Exclude from the output any fields that start with the name `_sa`.\n\n            This is mainly a hack for compatibility with SQLAlchemy objects, they\n            store internal SQLAlchemy-specific state in attributes named with `_sa`,\n            and those objects can't (and shouldn't be) serialized to JSON.\n            ")]=True):
	o='__root__';T=exclude_defaults;Q=exclude_unset;P=by_alias;M=sqlalchemy_safe;K=exclude_none;G=exclude;F=include;E=custom_encoder;A=obj;E=E or{}
	if E:
		if O(A)in E:return E[O(A)](A)
		else:
			for(r,s)in E.items():
				if D(A,r):return s(A)
	if F is not I and not D(F,(H,U)):F=H(F)
	if G is not I and not D(G,(H,U)):G=H(G)
	if D(A,(q,J.BaseModel)):
		V={}
		if D(A,J.BaseModel):
			V=getattr(A.__config__,'json_encoders',{})
			if E:V={**V,**E}
		R=Ā(A,mode='json',include=F,exclude=G,by_alias=P,exclude_unset=Q,exclude_none=K,exclude_defaults=T)
		if o in R:R=R[o]
		return L(R,exclude_none=K,exclude_defaults=T,custom_encoder=V,sqlalchemy_safe=M)
	if e.is_dataclass(A):assert not D(A,O);R=e.asdict(A);return L(R,include=F,exclude=G,by_alias=P,exclude_unset=Q,exclude_defaults=T,exclude_none=K,custom_encoder=E,sqlalchemy_safe=M)
	if D(A,g):return A.value
	if D(A,p):return B(A)
	if D(A,(B,Z,a,O(I))):return A
	if z(A):return
	if D(A,U):
		k={};c=H(A.keys())
		if F is not I:c&=H(F)
		if G is not I:c-=H(G)
		for(W,l)in A.items():
			if(not M or not D(W,B)or not W.startswith('_sa'))and(l is not I or not K)and W in c:t=L(W,by_alias=P,exclude_unset=Q,exclude_none=K,custom_encoder=E,sqlalchemy_safe=M);u=L(l,by_alias=P,exclude_unset=Q,exclude_none=K,custom_encoder=E,sqlalchemy_safe=M);k[t]=u
		return k
	if D(A,(S,H,i,h,j,f)):
		m=[]
		for v in A:m.append(L(v,include=F,exclude=G,by_alias=P,exclude_unset=Q,exclude_defaults=T,exclude_none=K,custom_encoder=E,sqlalchemy_safe=M))
		return m
	if O(A)in Y:return Y[O(A)](A)
	for(x,y)in w.items():
		if D(A,y):return x(A)
	try:n=U(A)
	except b as X:
		d=[];d.append(X)
		try:n=vars(A)
		except b as X:d.append(X);raise ValueError(d)from X
	return L(n,include=F,exclude=G,by_alias=P,exclude_unset=Q,exclude_defaults=T,exclude_none=K,custom_encoder=E,sqlalchemy_safe=M)