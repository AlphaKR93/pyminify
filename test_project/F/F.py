import functools as D,warnings as F
from collections.abc import Callable as B,Coroutine as H,Iterable as I,Iterator as J
from typing import ParamSpec as K,TypeVar as L
import anyio.to_thread
C=K('P')
A=L('T')
async def M(*C:tuple[B,dict]):
	F.warn('run_until_first_complete is deprecated and will be removed in a future version.',DeprecationWarning)
	async with anyio.create_task_group()as A:
		async def E(func:B[[],H]):await func();A.cancel_scope.cancel()
		for(G,I)in C:A.start_soon(E,D.partial(G,**I))
async def Æ(func:B[C,A],*B:C.args,**E:C.kwargs):A=func;A=D.partial(A,*B,**E);return await anyio.to_thread.run_sync(A)
class E(Exception):0
def N(iterator:J[A]):
	try:return next(iterator)
	except StopIteration:raise E
async def Ï(iterator:I[A]):
	A=iter(iterator)
	while True:
		try:yield await anyio.to_thread.run_sync(N,A)
		except E:break