T=isinstance
M=len
import functools as U
from collections.abc import Awaitable as D,Callable as V
from contextlib import AbstractAsyncContextManager as W,contextmanager as X
from typing import Any as B,Generic as Y,Protocol as O,TypeVar as F,overload as P
from F.V import Ñ
from asyncio import iscoroutinefunction as H
Q=True
J=F('T')
K=V[...,D[J]]
@P
def G(obj:K[J]):0
@P
def G(obj:B):0
def G(obj:B):
	A=obj
	while T(A,U.partial):A=A.func
	return H(A)or callable(A)and H(A.__call__)
L=F('T_co',covariant=True)
class R(D[L],W[L],O[L]):0
class Z(O):
	async def close(A):0
C=F('SupportsAsyncCloseType',bound=Z,covariant=False)
class S(Y[C]):
	__slots__='aw','entered'
	def __init__(A,aw:D[C]):A.aw=aw
	def __await__(A):return A.aw.__await__()
	async def __aenter__(A):A.entered=await A.aw;return A.entered
	async def __aexit__(A,*C:B):await A.entered.close()
@X
def E():
	try:yield
	except BaseException as A:
		if Q:
			while T(A,BaseExceptionGroup)and M(A.exceptions)==1:A=A.exceptions[0]
		raise A
def A(scope:Ñ):
	C=scope;A=C['path'];B=C.get('root_path','')
	if not B:return A
	if not A.startswith(B):return A
	if A==B:return''
	if A[M(B)]=='/':return A[M(B):]
	return A