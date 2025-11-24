c=hasattr
Z=all
Y=frozenset
X=set
P=bytes
O=isinstance
N=list
K=None
J=tuple
F=False
E=True
D=bool
import types as Q,typing as a
from collections import deque as R
from dataclasses import is_dataclass as d
from typing import Any as A,Deque,FrozenSet as e,List,Mapping as f,Sequence as g,Set,Tuple as S,Type as I,Union as B
from D.B import may_v1 as T
from D.Y import L
from pydantic import BaseModel as h
from pydantic.version import VERSION as i
from F.I import G
from typing_extensions import Annotated as j,get_args as C,get_origin as H
U=a._GenericAlias,Q.GenericAlias,Q.UnionType
u=J(int(A)for A in i.split('.')[:2])
x=u[0]==2
l={g:N,List:N,N:N,S:J,J:J,Set:X,X:X,e:Y,Y:Y,Deque:R,R:R}
k=J(l.keys())
def Ą(cls:A,class_or_tuple:B[I[A],S[I[A],...],K]):
	A=cls
	try:return O(A,type)and issubclass(A,class_or_tuple)
	except TypeError:
		if O(A,U):return F
		raise
def V(annotation:B[I[A],K]):
	A=annotation
	if Ą(A,(str,P)):return F
	return Ą(A,k)
def M(annotation:B[I[A],K]):
	A=annotation;D=H(A)
	if D is B or D is L:
		for G in C(A):
			if M(G):return E
		return F
	return V(A)or V(H(A))
def w(value:A):A=value;return O(A,k)and not O(A,(str,P))
def b(annotation:B[I[A],K]):A=annotation;return Ą(A,(h,T.BaseModel,f,G))or V(A)or d(A)
def W(annotation:B[I[A],K]):
	D=annotation;A=H(D)
	if A is B or A is L:return any(W(A)for A in C(D))
	if A is j:return W(C(D)[0])
	return b(D)or b(A)or c(A,'__pydantic_core_schema__')or c(A,'__get_pydantic_core_schema__')
def s(annotation:A):A=annotation;return A is Ellipsis or not W(A)
def m(annotation:B[I[A],K]):
	A=annotation;D=H(A)
	if D is B or D is L:
		G=F
		for I in C(A):
			if m(I):G=E;continue
			elif not s(I):return F
		return G
	return M(A)and Z(s(A)for A in C(A))
def n(annotation:A):
	A=annotation
	if Ą(A,P):return E
	D=H(A)
	if D is B or D is L:
		for G in C(A):
			if Ą(G,P):return E
	return F
def t(annotation:A):
	A=annotation
	if Ą(A,G):return E
	D=H(A)
	if D is B or D is L:
		for I in C(A):
			if Ą(I,G):return E
	return F
def o(annotation:A):
	A=annotation;D=H(A)
	if D is B or D is L:
		G=F
		for I in C(A):
			if o(I):G=E;continue
		return G
	return M(A)and Z(n(A)for A in C(A))
def v(annotation:A):
	A=annotation;D=H(A)
	if D is B or D is L:
		G=F
		for I in C(A):
			if v(I):G=E;continue
		return G
	return M(A)and Z(t(A)for A in C(A))
def r(annotation:A):
	A=annotation
	if Ą(A,T.BaseModel):return E
	D=H(A)
	if D is B or D is L:
		for G in C(A):
			if Ą(G,T.BaseModel):return E
	if M(A):
		for I in C(A):
			if r(I):return E
	return F