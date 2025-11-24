r='Bearer'
q='WWW-Authenticate'
o='bearer'
n='scopes'
m='refreshUrl'
l='tokenUrl'
k='\n                The URL to refresh the token and obtain a new one.\n                '
j='\n                The OAuth2 scopes that would be required by the *path operations* that\n                use this dependency.\n                '
i="\n                If there's a `client_password` (and a `client_id`), they can be sent\n                as part of the form fields. But the OAuth2 specification recommends\n                sending the `client_id` and `client_secret` (if any) using HTTP Basic\n                auth.\n                "
h="\n                If there's a `client_id`, it can be sent as part of the form fields.\n                But the OAuth2 specification recommends sending the `client_id` and\n                `client_secret` (if any) using HTTP Basic auth.\n                "
g='\n                A single string with actually several scopes separated by spaces. Each\n                scope is also a string.\n\n                For example, a single string with:\n\n                ```python\n                "items:read items:write users:read profile openid"\n                ````\n\n                would represent the scopes:\n\n                * `items:read`\n                * `items:write`\n                * `users:read`\n                * `profile`\n                * `openid`\n                '
f='\n                `password` string. The OAuth2 spec requires the exact field name\n                `password`.\n                '
e='password'
d='format'
c='\n                `username` string. The OAuth2 spec requires the exact field name\n                `username`.\n                '
b='^password$'
X='Not authenticated'
W='Authorization'
V=True
T='\n                By default, if no HTTP Authorization header is provided, required for\n                OAuth2 authentication, it will automatically cancel the request and\n                send the client an error.\n\n                If `auto_error` is set to `False`, when the HTTP Authorization header\n                is not available, instead of erroring out, the dependency result will\n                be `None`.\n\n                This is useful when you want to have optional authentication.\n\n                It is also useful when you want to have authentication that can be\n                provided in one of multiple optional ways (for example, with OAuth2\n                or in a cookie).\n                '
Q='\n                Security scheme description.\n\n                It will be included in the generated OpenAPI (e.g. visible at `/docs`).\n                '
P='\n                Security scheme name.\n\n                It will be included in the generated OpenAPI (e.g. visible at `/docs`).\n                '
O=bool
H=None
E=str
from typing import Any as L,Dict as K,List as Z,Optional as I,Union as J,cast as M
from annotated_doc import Doc as F
from D.K import C
from D.N.C import p
from D.N.C import S
from D.O import N
from D.T.B import v
from D.T.F import D
from F.N import Y
from F.S import B,A
from typing_extensions import Annotated as G
class a:
	def __init__(A,*,grant_type:G[J[E,H],N(pattern=b),F('\n                The OAuth2 spec says it is required and MUST be the fixed string\n                "password". Nevertheless, this dependency class is permissive and\n                allows not passing it. If you want to enforce it, use instead the\n                `OAuth2PasswordRequestFormStrict` dependency.\n                ')]=H,username:G[E,N(),F(c)],password:G[E,N(json_schema_extra={d:e}),F(f)],scope:G[E,N(),F(g)]='',client_id:G[J[E,H],N(),F(h)]=H,client_secret:G[J[E,H],N(json_schema_extra={d:e}),F(i)]=H):A.grant_type=grant_type;A.username=username;A.password=password;A.scopes=scope.split();A.client_id=client_id;A.client_secret=client_secret
class s(a):
	def __init__(A,grant_type:G[E,N(pattern=b),F('\n                The OAuth2 spec says it is required and MUST be the fixed string\n                "password". This dependency is strict about it. If you want to be\n                permissive, use instead the `OAuth2PasswordRequestForm` dependency\n                class.\n                ')],username:G[E,N(),F(c)],password:G[E,N(),F(f)],scope:G[E,N(),F(g)]='',client_id:G[J[E,H],N(),F(h)]=H,client_secret:G[J[E,H],N(),F(i)]=H):super().__init__(grant_type=grant_type,username=username,password=password,scope=scope,client_id=client_id,client_secret=client_secret)
class R(v):
	def __init__(A,*,flows:G[J[S,K[E,K[E,L]]],F('\n                The dictionary of OAuth2 flows.\n                ')]=S(),scheme_name:G[I[E],F(P)]=H,description:G[I[E],F(Q)]=H,auto_error:G[O,F(T)]=V):A.model=p(flows=flows,description=description);A.scheme_name=scheme_name or A.__class__.__name__;A.auto_error=auto_error
	async def __call__(D,request:Y):
		B=request.headers.get(W)
		if not B:
			if D.auto_error:raise C(status_code=A,detail=X)
			else:return
		return B
class t(R):
	def __init__(C,tokenUrl:G[E,F('\n                The URL to obtain the OAuth2 token. This would be the *path operation*\n                that has `OAuth2PasswordRequestForm` as a dependency.\n                ')],scheme_name:G[I[E],F(P)]=H,scopes:G[I[K[E,E]],F(j)]=H,description:G[I[E],F(Q)]=H,auto_error:G[O,F(T)]=V,refreshUrl:G[I[E],F(k)]=H):
		A=scopes
		if not A:A={}
		B=S(password={l:tokenUrl,m:refreshUrl,n:A});super().__init__(flows=B,scheme_name=scheme_name,description=description,auto_error=auto_error)
	async def __call__(E,request:Y):
		A=request.headers.get(W);F,G=D(A)
		if not A or F.lower()!=o:
			if E.auto_error:raise C(status_code=B,detail=X,headers={q:r})
			else:return
		return G
class u(R):
	def __init__(C,authorizationUrl:E,tokenUrl:G[E,F('\n                The URL to obtain the OAuth2 token.\n                ')],refreshUrl:G[I[E],F(k)]=H,scheme_name:G[I[E],F(P)]=H,scopes:G[I[K[E,E]],F(j)]=H,description:G[I[E],F(Q)]=H,auto_error:G[O,F(T)]=V):
		A=scopes
		if not A:A={}
		B=S(authorizationCode={'authorizationUrl':authorizationUrl,l:tokenUrl,m:refreshUrl,n:A});super().__init__(flows=B,scheme_name=scheme_name,description=description,auto_error=auto_error)
	async def __call__(E,request:Y):
		A=request.headers.get(W);F,G=D(A)
		if not A or F.lower()!=o:
			if E.auto_error:raise C(status_code=B,detail=X,headers={q:r})
			else:return
		return G
class U:
	def __init__(A,scopes:G[I[Z[E]],F('\n                This will be filled by FastAPI.\n                ')]=H):A.scopes=scopes or[];A.scope_str=' '.join(A.scopes)