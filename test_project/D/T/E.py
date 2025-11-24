D=str
from typing import Optional as E
from annotated_doc import Doc as B
from D.N.C import q
from D.T.B import v
from F.K import Ú
from F.N import Y
from F.S import A
from typing_extensions import Annotated as C
class S(v):
	def __init__(A,*,openIdConnectUrl:C[D,B('\n            The OpenID Connect URL.\n            ')],scheme_name:C[E[D],B('\n                Security scheme name.\n\n                It will be included in the generated OpenAPI (e.g. visible at `/docs`).\n                ')]=None,description:C[E[D],B('\n                Security scheme description.\n\n                It will be included in the generated OpenAPI (e.g. visible at `/docs`).\n                ')]=None,auto_error:C[bool,B('\n                By default, if no HTTP Authorization header is provided, required for\n                OpenID Connect authentication, it will automatically cancel the request\n                and send the client an error.\n\n                If `auto_error` is set to `False`, when the HTTP Authorization header\n                is not available, instead of erroring out, the dependency result will\n                be `None`.\n\n                This is useful when you want to have optional authentication.\n\n                It is also useful when you want to have authentication that can be\n                provided in one of multiple optional ways (for example, with OpenID\n                Connect or in a cookie).\n                ')]=True):A.model=q(openIdConnectUrl=openIdConnectUrl,description=description);A.scheme_name=scheme_name or A.__class__.__name__;A.auto_error=auto_error
	async def __call__(C,request:Y):
		B=request.headers.get('Authorization')
		if not B:
			if C.auto_error:raise Ú(status_code=A,detail='Not authenticated')
			else:return
		return B