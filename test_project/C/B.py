F=Exception
import typing as G
from cryptography.hazmat.bindings._rust import exceptions as K
B=K._Reasons
class A(F):
	def __init__(A,message:str,reason:G.Optional[B]=None):super().__init__(message);A._reason=reason
class C(F):0
class H(F):0
class I(F):0
class E(F):0
class T(F):0
class J(F):
	def __init__(A,msg:str,err_code:G.List[L.OpenSSLError]):super().__init__(msg);A.err_code=err_code
class D(F):0