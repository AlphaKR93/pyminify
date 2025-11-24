R='rdns'
Q='password'
P='username'
N='proxy_port'
M='proxy_host'
L='socks_version'
G=ImportError
B=str
A=None
try:import socks as D
except G:import warnings as S;from..H import U;S.warn('SOCKS support in urllib3 requires the installation of optional dependencies: specifically, PySocks.  For more information, see https://urllib3.readthedocs.io/en/latest/contrib.html#socks-proxies',U);raise
import typing as E
from socket import timeout as H
from..E import Ì,º
from..F import Ë,w
from..H import F,K
from..K import O
from..M.J import Ä
try:0
except G:ssl=A
try:
	from typing import TypedDict as T
	class I(T):socks_version:int;proxy_host:B|A;proxy_port:B|A;username:B|A;password:B|A;rdns:bool
except G:I=E.Dict[B,E.Any]
class J(Ì):
	def __init__(A,_socks_options:I,*B:E.Any,**C:E.Any):A._socks_options=_socks_options;super().__init__(*B,**C)
	def _new_conn(A):
		G={}
		if A.source_address:G['source_address']=A.source_address
		if A.socket_options:G['socket_options']=A.socket_options
		try:J=D.create_connection((A.host,A.port),proxy_type=A._socks_options[L],proxy_addr=A._socks_options[M],proxy_port=A._socks_options[N],proxy_username=A._socks_options[P],proxy_password=A._socks_options[Q],proxy_rdns=A._socks_options[R],timeout=A.timeout,**G)
		except H as C:raise F(A,f"Connection to {A.host} timed out. (connect timeout={A.timeout})")from C
		except D.ProxyError as C:
			if C.socket_err:
				I=C.socket_err
				if isinstance(I,H):raise F(A,f"Connection to {A.host} timed out. (connect timeout={A.timeout})")from C
				else:raise K(A,f"Failed to establish a new connection: {I}")
			else:raise K(A,f"Failed to establish a new connection: {C}")from C
		except OSError as C:raise K(A,f"Failed to establish a new connection: {C}")from C
		return J
class V(J,º):0
class W(Ë):ConnectionCls=J
class X(w):ConnectionCls=V
class C(O):
	pool_classes_by_scheme={'http':W,'https':X}
	def __init__(K,proxy_url:B,username:B|A=A,password:B|A=A,num_pools:int=10,headers:E.Mapping[B,B]|A=A,**O:E.Any):
		T=False;J=password;I=username;H=proxy_url;B=Ä(H)
		if I is A and J is A and B.auth is not A:
			S=B.auth.split(':')
			if len(S)==2:I,J=S
		if B.scheme=='socks5':F=D.PROXY_TYPE_SOCKS5;G=T
		elif B.scheme=='socks5h':F=D.PROXY_TYPE_SOCKS5;G=True
		elif B.scheme=='socks4':F=D.PROXY_TYPE_SOCKS4;G=T
		elif B.scheme=='socks4a':F=D.PROXY_TYPE_SOCKS4;G=True
		else:raise ValueError(f"Unable to determine SOCKS version from {H}")
		K.proxy_url=H;U={L:F,M:B.host,N:B.port,P:I,Q:J,R:G};O['_socks_options']=U;super().__init__(num_pools,headers,**O);K.pool_classes_by_scheme=C.pool_classes_by_scheme