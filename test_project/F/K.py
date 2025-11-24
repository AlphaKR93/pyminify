C=Exception
B=None
A=str
import http
from collections.abc import Mapping as E
class Ú(C):
	def __init__(A,status_code:int,detail:A|B=B,headers:E[A,A]|B=B):
		D=status_code;C=detail
		if C is B:C=http.HTTPStatus(D).phrase
		A.status_code=D;A.detail=C;A.headers=headers
	def __str__(A):return f"{A.status_code}: {A.detail}"
	def __repr__(A):B=A.__class__.__name__;return f"{B}(status_code={A.status_code!r}, detail={A.detail!r})"
class D(C):
	def __init__(A,code:int,reason:A|B=B):A.code=code;A.reason=reason or''
	def __str__(A):return f"{A.code}: {A.reason}"
	def __repr__(A):B=A.__class__.__name__;return f"{B}(code={A.code!r}, reason={A.reason!r})"