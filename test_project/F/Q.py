I=None
H=list
G=isinstance
D=dict
A=str
import inspect as J,re
from collections.abc import Callable as K
from typing import Any as B,NamedTuple as L
from F.N import Y
from F.O import C
from F.P import U,w,l,u
try:import yaml as E
except ModuleNotFoundError:E=I
class M(C):
	media_type='application/vnd.oai.openapi'
	def render(B,content:B):A=content;assert E is not I,'`pyyaml` must be installed to use OpenAPIResponse.';assert G(A,D),'The schema passed to OpenAPIResponse should be a dictionary.';return E.dump(A,default_flow_style=False).encode('utf-8')
class F(L):path:A;http_method:A;func:K[...,B]
N=re.compile(':\\w+}')
class O:
	def get_schema(A,routes:H[U]):raise NotImplementedError
	def get_endpoints(D,routes:H[U]):
		"\n        Given the routes, yields the following information:\n\n        - path\n            eg: /users/\n        - http_method\n            one of 'get', 'post', 'put', 'patch', 'delete', 'options'\n        - func\n            method ready to extract the docstring\n        ";I=routes;E=[]
		for A in I:
			if G(A,l|w):
				I=A.routes or[]
				if G(A,l):B=D._remove_converter(A.path)
				else:B=''
				K=[F(path=''.join((B,A.path)),http_method=A.http_method,func=A.func)for A in D.get_endpoints(I)];E.extend(K)
			elif not G(A,u)or not A.include_in_schema:continue
			elif J.isfunction(A.endpoint)or J.ismethod(A.endpoint):
				B=D._remove_converter(A.path)
				for C in A.methods or['GET']:
					if C=='HEAD':continue
					E.append(F(B,C.lower(),A.endpoint))
			else:
				B=D._remove_converter(A.path)
				for C in['get','post','put','patch','delete','options']:
					if not hasattr(A.endpoint,C):continue
					L=getattr(A.endpoint,C);E.append(F(B,C.lower(),L))
		return E
	def _remove_converter(A,path:A):'\n        Remove the converter from the path.\n        For example, a route like this:\n            Route("/users/{id:int}", endpoint=get_user, methods=["GET"])\n        Should be represented as `/users/{id}` in the OpenAPI schema.\n        ';return N.sub('}',path)
	def parse_docstring(C,func_or_method:K[...,B]):
		'\n        Given a function, parse the docstring as YAML and return a dictionary of info.\n        ';A=func_or_method.__doc__
		if not A:return{}
		assert E is not I,'`pyyaml` must be installed to use parse_docstring.';A=A.split('---')[-1];B=E.safe_load(A)
		if not G(B,D):return{}
		return B
	def OpenAPIResponse(A,request:Y):B=request.app.routes;C=A.get_schema(routes=B);return M(C)
class P(O):
	def __init__(A,base_schema:D[A,B]):A.base_schema=base_schema
	def get_schema(E,routes:H[U]):
		C='paths';A=D(E.base_schema);A.setdefault(C,{});G=E.get_endpoints(routes)
		for B in G:
			F=E.parse_docstring(B.func)
			if not F:continue
			if B.path not in A[C]:A[C][B.path]={}
			A[C][B.path][B.http_method]=F
		return A