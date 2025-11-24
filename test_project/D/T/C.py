W='digest'
V='basic'
S='Invalid authentication credentials'
R='\n                Security scheme description.\n\n                It will be included in the generated OpenAPI (e.g. visible at `/docs`).\n                '
Q='\n                Security scheme name.\n\n                It will be included in the generated OpenAPI (e.g. visible at `/docs`).\n                '
N='Not authenticated'
M='Authorization'
L=True
K=bool
I=None
G=str
import binascii as X
from base64 import b64decode as Z
from typing import Optional as H
from annotated_doc import Doc as E
from D.K import C
from D.N.C import U
from D.N.C import o
from D.T.B import v
from D.T.F import D
from pydantic import BaseModel as T
from F.N import Y
from F.S import B,A
from typing_extensions import Annotated as F
class P(T):username:F[G,E('The HTTP Basic username.')];password:F[G,E('The HTTP Basic password.')]
class J(T):scheme:F[G,E('\n            The HTTP authorization scheme extracted from the header value.\n            ')];credentials:F[G,E('\n            The HTTP authorization credentials extracted from the header value.\n            ')]
class O(v):
	def __init__(A,*,scheme:G,scheme_name:H[G]=I,description:H[G]=I,auto_error:K=L):A.model=U(scheme=scheme,description=description);A.scheme_name=scheme_name or A.__class__.__name__;A.auto_error=auto_error
	async def __call__(G,request:Y):
		B=request.headers.get(M);E,F=D(B)
		if not(B and E and F):
			if G.auto_error:raise C(status_code=A,detail=N)
			else:return
		return J(scheme=E,credentials=F)
class b(O):
	def __init__(A,*,scheme_name:F[H[G],E(Q)]=I,realm:F[H[G],E('\n                HTTP Basic authentication realm.\n                ')]=I,description:F[H[G],E(R)]=I,auto_error:F[K,E('\n                By default, if the HTTP Basic authentication is not provided (a\n                header), `HTTPBasic` will automatically cancel the request and send the\n                client an error.\n\n                If `auto_error` is set to `False`, when the HTTP Basic authentication\n                is not available, instead of erroring out, the dependency result will\n                be `None`.\n\n                This is useful when you want to have optional authentication.\n\n                It is also useful when you want to have authentication that can be\n                provided in one of multiple optional ways (for example, in HTTP Basic\n                authentication or in an HTTP Bearer token).\n                ')]=L):A.model=U(scheme=V,description=description);A.scheme_name=scheme_name or A.__class__.__name__;A.realm=realm;A.auto_error=auto_error
	async def __call__(A,request:Y):
		H='WWW-Authenticate';F=request.headers.get(M);I,J=D(F)
		if A.realm:E={H:f'Basic realm="{A.realm}"'}
		else:E={H:'Basic'}
		if not F or I.lower()!=V:
			if A.auto_error:raise C(status_code=B,detail=N,headers=E)
			else:return
		G=C(status_code=B,detail=S,headers=E)
		try:K=Z(J).decode('ascii')
		except(ValueError,UnicodeDecodeError,X.Error):raise G
		L,O,Q=K.partition(':')
		if not O:raise G
		return P(username=L,password=Q)
class c(O):
	def __init__(A,*,bearerFormat:F[H[G],E('Bearer token format.')]=I,scheme_name:F[H[G],E(Q)]=I,description:F[H[G],E(R)]=I,auto_error:F[K,E('\n                By default, if the HTTP Bearer token is not provided (in an\n                `Authorization` header), `HTTPBearer` will automatically cancel the\n                request and send the client an error.\n\n                If `auto_error` is set to `False`, when the HTTP Bearer token\n                is not available, instead of erroring out, the dependency result will\n                be `None`.\n\n                This is useful when you want to have optional authentication.\n\n                It is also useful when you want to have authentication that can be\n                provided in one of multiple optional ways (for example, in an HTTP\n                Bearer token or in a cookie).\n                ')]=L):A.model=o(bearerFormat=bearerFormat,description=description);A.scheme_name=scheme_name or A.__class__.__name__;A.auto_error=auto_error
	async def __call__(E,request:Y):
		F=request.headers.get(M);B,G=D(F)
		if not(F and B and G):
			if E.auto_error:raise C(status_code=A,detail=N)
			else:return
		if B.lower()!='bearer':
			if E.auto_error:raise C(status_code=A,detail=S)
			else:return
		return J(scheme=B,credentials=G)
class d(O):
	def __init__(A,*,scheme_name:F[H[G],E(Q)]=I,description:F[H[G],E(R)]=I,auto_error:F[K,E('\n                By default, if the HTTP Digest is not provided, `HTTPDigest` will\n                automatically cancel the request and send the client an error.\n\n                If `auto_error` is set to `False`, when the HTTP Digest is not\n                available, instead of erroring out, the dependency result will\n                be `None`.\n\n                This is useful when you want to have optional authentication.\n\n                It is also useful when you want to have authentication that can be\n                provided in one of multiple optional ways (for example, in HTTP\n                Digest or in a cookie).\n                ')]=L):A.model=U(scheme=W,description=description);A.scheme_name=scheme_name or A.__class__.__name__;A.auto_error=auto_error
	async def __call__(E,request:Y):
		F=request.headers.get(M);B,G=D(F)
		if not(F and B and G):
			if E.auto_error:raise C(status_code=A,detail=N)
			else:return
		if B.lower()!=W:
			if E.auto_error:raise C(status_code=A,detail=S)
			else:return
		return J(scheme=B,credentials=G)