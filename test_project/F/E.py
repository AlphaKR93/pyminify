from collections.abc import Callable as D,Sequence as E
from typing import Any,ParamSpec as F
from F.B import G
from F.F import Æ
C=F('P')
class A:
	def __init__(A,func:D[C,Any],*B:C.args,**D:C.kwargs):A.func=func;A.args=B;A.kwargs=D;A.is_async=G(func)
	async def __call__(A):
		if A.is_async:await A.func(*A.args,**A.kwargs)
		else:await Æ(A.func,*A.args,**A.kwargs)
class B(A):
	def __init__(B,tasks:E[A]|None=None):A=tasks;B.tasks=list(A)if A else[]
	def add_task(B,func:D[C,Any],*D:C.args,**E:C.kwargs):F=A(func,*D,**E);B.tasks.append(F)
	async def __call__(A):
		for B in A.tasks:await B()