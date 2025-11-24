g='http.disconnect'
f='_body'
d='query_string'
c='path'
b='http'
a=ModuleNotFoundError
U=True
T=False
Q='app'
P=float
O=RuntimeError
N=b''
L='type'
K=bytes
J=int
I=dict
G=hasattr
C=None
B=property
A=str
import json as h
from collections.abc import Mapping as k
from http import cookies as l
from typing import Any as F,cast
import anyio
from F.B import S
from F.I import W,e,H,D,Z,V
from F.K import Ú
from F.L import t,s,u
from F.V import Ì,Ò,Ñ,Send
try:
	try:from python_multipart.multipart import parse_options_header as M
	except a:from multipart.multipart import parse_options_header as M
except a:M=C
n={'accept','accept-encoding','accept-language','cache-control','user-agent'}
def o(cookie_string:A):
	E={}
	for D in cookie_string.split(';'):
		if'='in D:B,C=D.split('=',1)
		else:B,C='',D
		B,C=B.strip(),C.strip()
		if B or C:E[B]=l._unquote(C)
	return E
class Ð(Exception):0
class E(k[A,F]):
	def __init__(B,scope:Ñ,receive:Ò|C=C):A=scope;assert A[L]in(b,'websocket');B.scope=A
	def __getitem__(A,key:A):return A.scope[key]
	def __iter__(A):return iter(A.scope)
	def __len__(A):return len(A.scope)
	__eq__=object.__eq__;__hash__=object.__hash__
	@B
	def app(self):return self.scope[Q]
	@B
	def url(self):
		A=self
		if not G(A,'_url'):A._url=W(scope=A.scope)
		return A._url
	@B
	def base_url(self):
		E='root_path';B=self
		if not G(B,'_base_url'):
			A=I(B.scope);D=A.get('app_root_path',A.get(E,''));C=D
			if not C.endswith('/'):C+='/'
			A[c]=C;A[d]=N;A[E]=D;B._base_url=W(scope=A)
		return B._base_url
	@B
	def headers(self):
		A=self
		if not G(A,'_headers'):A._headers=D(scope=A.scope)
		return A._headers
	@B
	def query_params(self):
		A=self
		if not G(A,'_query_params'):A._query_params=Z(A.scope[d])
		return A._query_params
	@B
	def path_params(self):return self.scope.get('path_params',{})
	@B
	def cookies(self):
		B=self
		if not G(B,'_cookies'):
			C={};D=B.headers.getlist('cookie')
			for E in D:C.update(o(E))
			B._cookies=C
		return B._cookies
	@B
	def client(self):
		A=self.scope.get('client')
		if A is not C:return e(*A)
	@B
	def session(self):A='session';assert A in self.scope,'SessionMiddleware must be installed to access request.session';return self.scope[A]
	@B
	def auth(self):A='auth';assert A in self.scope,'AuthenticationMiddleware must be installed to access request.auth';return self.scope[A]
	@B
	def user(self):A='user';assert A in self.scope,'AuthenticationMiddleware must be installed to access request.user';return self.scope[A]
	@B
	def state(self):
		B='state';A=self
		if not G(A,'_state'):A.scope.setdefault(B,{});A._state=V(A.scope[B])
		return A._state
	def url_for(A,D:A,**E:F):
		B=A.scope.get('router')or A.scope.get(Q)
		if B is C:raise O('The `url_for` method can only be used inside a Starlette application or with a router.')
		G=B.url_path_for(D,**E);return G.make_absolute_url(base_url=A.base_url)
async def p():raise O('Receive channel has not been made available')
async def q(message:Ì):raise O('Send channel has not been made available')
class Y(E):
	_form:H|C
	def __init__(A,scope:Ñ,receive:Ò=p,send:Send=q):B=scope;super().__init__(B);assert B[L]==b;A._receive=receive;A._send=send;A._stream_consumed=T;A._is_disconnected=T;A._form=C
	@B
	def method(self):return self.scope['method']
	@B
	def receive(self):return self._receive
	async def stream(A):
		if G(A,f):yield A._body;yield N;return
		if A._stream_consumed:raise O('Stream consumed')
		while not A._stream_consumed:
			B=await A._receive()
			if B[L]=='http.request':
				C=B.get('body',N)
				if not B.get('more_body',T):A._stream_consumed=U
				if C:yield C
			elif B[L]==g:A._is_disconnected=U;raise Ð()
		yield N
	async def body(A):
		if not G(A,f):
			B=[]
			async for C in A.stream():B.append(C)
			A._body=N.join(B)
		return A._body
	async def json(A):
		if not G(A,'_json'):B=await A.body();A._json=h.loads(B)
		return A._json
	async def _get_form(A,*,max_files:J|P=1000,max_fields:J|P=1000,max_part_size:J=1024*1024):
		if A._form is C:
			assert M is not C,'The `python-multipart` library must be installed to use form parsing.';E=A.headers.get('Content-Type');B,I=M(E)
			if B==b'multipart/form-data':
				try:F=u(A.headers,A.stream(),max_files=max_files,max_fields=max_fields,max_part_size=max_part_size);A._form=await F.parse()
				except s as D:
					if Q in A.scope:raise Ú(status_code=400,detail=D.message)
					raise D
			elif B==b'application/x-www-form-urlencoded':G=t(A.headers,A.stream());A._form=await G.parse()
			else:A._form=H()
		return A._form
	def form(A,*,max_files:J|P=1000,max_fields:J|P=1000,max_part_size:J=1024*1024):return S(A._get_form(max_files=max_files,max_fields=max_fields,max_part_size=max_part_size))
	async def close(A):
		if A._form is not C:await A._form.close()
	async def is_disconnected(A):
		if not A._is_disconnected:
			B={}
			with anyio.CancelScope()as C:C.cancel();B=await A._receive()
			if B.get(L)==g:A._is_disconnected=U
		return A._is_disconnected
	async def send_push_promise(A,path:A):
		E='latin-1';D='http.response.push'
		if D in A.scope.get('extensions',{}):
			B=[]
			for C in n:
				for F in A.headers.getlist(C):B.append((C.encode(E),F.encode(E)))
			await A._send({L:D,c:path,'headers':B})