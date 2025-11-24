R='request'
O='__call__'
N=True
L=getattr
J=bool
F=list
C=str
A=None
import inspect as G
from dataclasses import dataclass as P,field as E
from functools import cached_property as H
from typing import Any,Callable as S,List as D,Optional as B,Sequence as T,Union as Q
from D.B import ModelField as I
from D.T.B import v
from typing_extensions import Literal as U
from asyncio import iscoroutinefunction as K
@P
class ö:security_scheme:v;scopes:B[T[C]]=A
@P
class Č:
	path_params:D[I]=E(default_factory=F);query_params:D[I]=E(default_factory=F);header_params:D[I]=E(default_factory=F);cookie_params:D[I]=E(default_factory=F);body_params:D[I]=E(default_factory=F);dependencies:D['Dependant']=E(default_factory=F);security_requirements:D[ö]=E(default_factory=F);name:B[C]=A;call:B[S[...,Any]]=A;request_param_name:B[C]=A;websocket_param_name:B[C]=A;http_connection_param_name:B[C]=A;response_param_name:B[C]=A;background_tasks_param_name:B[C]=A;security_scopes_param_name:B[C]=A;security_scopes:B[D[C]]=A;use_cache:J=N;path:B[C]=A;scope:Q[U['function',R],A]=A
	@H
	def cache_key(self):A=self;return A.call,tuple(sorted(set(A.security_scopes or[]))),A.computed_scope or''
	@H
	def is_gen_callable(self):
		if G.isgeneratorfunction(self.call):return N
		B=L(self.call,O,A);return G.isgeneratorfunction(B)
	@H
	def is_async_gen_callable(self):
		if G.isasyncgenfunction(self.call):return N
		B=L(self.call,O,A);return G.isasyncgenfunction(B)
	@H
	def is_coroutine_callable(self):
		B=self
		if G.isroutine(B.call):return K(B.call)
		if G.isclass(B.call):return False
		C=L(B.call,O,A);return K(C)
	@H
	def computed_scope(self):
		A=self
		if A.scope:return A.scope
		if A.is_gen_callable or A.is_async_gen_callable:return R