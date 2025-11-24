L='in'
K=True
J='\n                Security scheme description.\n\n                It will be included in the generated OpenAPI (e.g. visible at `/docs`).\n                '
I='\n                Security scheme name.\n\n                It will be included in the generated OpenAPI (e.g. visible at `/docs`).\n                '
G=bool
F=None
B=str
from typing import Optional as E
from annotated_doc import Doc as C
from D.N.C import Q,Z
from D.T.B import v
from F.K import Ú
from F.N import Y
from F.S import A
from typing_extensions import Annotated as D
class H(v):
	@staticmethod
	def check_api_key(api_key:E[B],auto_error:G):
		B=api_key
		if not B:
			if auto_error:raise Ú(status_code=A,detail='Not authenticated')
			return
		return B
class M(H):
	def __init__(A,*,name:D[B,C('Query parameter name.')],scheme_name:D[E[B],C(I)]=F,description:D[E[B],C(J)]=F,auto_error:D[G,C('\n                By default, if the query parameter is not provided, `APIKeyQuery` will\n                automatically cancel the request and send the client an error.\n\n                If `auto_error` is set to `False`, when the query parameter is not\n                available, instead of erroring out, the dependency result will be\n                `None`.\n\n                This is useful when you want to have optional authentication.\n\n                It is also useful when you want to have authentication that can be\n                provided in one of multiple optional ways (for example, in a query\n                parameter or in an HTTP Bearer token).\n                ')]=K):A.model=Q(**{L:Z.query},name=name,description=description);A.scheme_name=scheme_name or A.__class__.__name__;A.auto_error=auto_error
	async def __call__(A,request:Y):B=request.query_params.get(A.model.name);return A.check_api_key(B,A.auto_error)
class N(H):
	def __init__(A,*,name:D[B,C('Header name.')],scheme_name:D[E[B],C(I)]=F,description:D[E[B],C(J)]=F,auto_error:D[G,C('\n                By default, if the header is not provided, `APIKeyHeader` will\n                automatically cancel the request and send the client an error.\n\n                If `auto_error` is set to `False`, when the header is not available,\n                instead of erroring out, the dependency result will be `None`.\n\n                This is useful when you want to have optional authentication.\n\n                It is also useful when you want to have authentication that can be\n                provided in one of multiple optional ways (for example, in a header or\n                in an HTTP Bearer token).\n                ')]=K):A.model=Q(**{L:Z.header},name=name,description=description);A.scheme_name=scheme_name or A.__class__.__name__;A.auto_error=auto_error
	async def __call__(A,request:Y):B=request.headers.get(A.model.name);return A.check_api_key(B,A.auto_error)
class O(H):
	def __init__(A,*,name:D[B,C('Cookie name.')],scheme_name:D[E[B],C(I)]=F,description:D[E[B],C(J)]=F,auto_error:D[G,C('\n                By default, if the cookie is not provided, `APIKeyCookie` will\n                automatically cancel the request and send the client an error.\n\n                If `auto_error` is set to `False`, when the cookie is not available,\n                instead of erroring out, the dependency result will be `None`.\n\n                This is useful when you want to have optional authentication.\n\n                It is also useful when you want to have authentication that can be\n                provided in one of multiple optional ways (for example, in a cookie or\n                in an HTTP Bearer token).\n                ')]=K):A.model=Q(**{L:Z.cookie},name=name,description=description);A.scheme_name=scheme_name or A.__class__.__name__;A.auto_error=auto_error
	async def __call__(A,request:Y):B=request.cookies.get(A.model.name);return A.check_api_key(B,A.auto_error)