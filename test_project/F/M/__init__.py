from __future__ import annotations
from collections.abc import Awaitable as C,Callable as D,Iterator as F
from typing import Any as B,ParamSpec as G,Protocol as H
A=G('P')
I=B
J=D[[],C[B]]
K=D[[B],C[None]]
E=D[[I,J,K],C[None]]
class X(H[A]):
	def __call__(B,C:E,*D:A.args,**E:A.kwargs):0
class Þ:
	def __init__(B,cls:X[A],*C:A.args,**D:A.kwargs):B.cls=cls;B.args=C;B.kwargs=D
	def __iter__(A):B=A.cls,A.args,A.kwargs;return iter(B)
	def __repr__(A):B=A.__class__.__name__;C=[f"{A!r}"for A in A.args];D=[f"{A}={B!r}"for(A,B)in A.kwargs.items()];E=getattr(A.cls,'__name__','');F=', '.join([E]+C+D);return f"{B}({F})"