from typing import Any,Callable as C
from annotated_doc import Doc
from F.E import B
from typing_extensions import Annotated as D,ParamSpec as E
A=E('P')
class F(B):
	def add_task(D,func:D[C[A,Any],Doc('\n                The function to call after the response is sent.\n\n                It can be a regular `def` function or an `async def` function.\n                ')],*B:A.args,**C:A.kwargs):return super().add_task(func,*B,**C)