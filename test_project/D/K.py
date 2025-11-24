H=str
B=None
from typing import Any as A,Dict,Optional as M,Sequence as G,Union
from annotated_doc import Doc as E
from pydantic import create_model as L
from F.K import Ú
from F.K import D
from typing_extensions import Annotated as F
class C(Ú):
	def __init__(A,status_code:F[int,E('\n                HTTP status code to send to the client.\n                ')],detail:F[A,E('\n                Any data to be sent to the client in the `detail` key of the JSON\n                response.\n                ')]=B,headers:F[M[Dict[H,H]],E('\n                Any headers to send to the client in the response.\n                ')]=B):super().__init__(status_code=status_code,detail=detail,headers=headers)
class O(D):
	def __init__(A,code:F[int,E('\n                A closing code from the\n                [valid codes defined in the specification](https://datatracker.ietf.org/doc/html/rfc6455#section-7.4.1).\n                ')],reason:F[Union[H,B],E('\n                The reason to close the WebSocket connection.\n\n                It is UTF-8-encoded data. The interpretation of the reason is up to the\n                application, it is not specified by the WebSocket specification.\n\n                It could contain text that could be human-readable or interpretable\n                by the client code, etc.\n                ')]=B):super().__init__(code=code,reason=reason)
P=L('Request')
Q=L('WebSocket')
class ý(RuntimeError):0
class N(ý):0
class I(Exception):
	def __init__(A,errors:G[A]):A._errors=errors
	def errors(A):return A._errors
class û(I):
	def __init__(A,errors:G[A],*,body:A=B):super().__init__(errors);A.body=body
class ü(I):0
class þ(I):
	def __init__(A,errors:G[A],*,body:A=B):super().__init__(errors);A.body=body
	def __str__(A):
		B=f"{len(A._errors)} validation errors:\n"
		for C in A._errors:B+=f"  {C}\n"
		return B