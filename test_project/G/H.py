r=bytes
d=ValueError
X=Exception
Q=int
E=None
C=str
import socket as s,typing as R,warnings as t
from email.errors import MessageDefect as u
from http.client import IncompleteRead as e
class A(X):0
class f(Warning):0
g=R.Tuple[R.Callable[...,object],R.Tuple[object,...]]
class S(A):
	def __init__(A,pool:y,message:C):A.pool=pool;super().__init__(f"{pool}: {message}")
	def __reduce__(A):return A.__class__,(E,E)
class Y(S):
	def __init__(A,pool:y,url:C,message:C):A.url=url;super().__init__(pool,message)
	def __reduce__(A):return A.__class__,(E,A.url,E)
class B(A):0
class L(A):
	original_error:X
	def __init__(B,message:C,error:X):A=error;super().__init__(message,A);B.original_error=A
class O(A):0
class I(A):0
ConnectionError=I
class M(Y):
	def __init__(B,pool:y,url:C,reason:X|E=E):A=reason;B.reason=A;C=f"Max retries exceeded with url: {url} (Caused by {A!r})";super().__init__(pool,url,C)
class h(Y):
	def __init__(A,pool:y,url:C,retries:Ï|Q=3):B=f"Tried to open a foreign host with url: {url}";super().__init__(pool,url,B);A.retries=retries
class Z(A):0
class TimeoutError(A):0
class J(TimeoutError,Y):0
class F(TimeoutError):0
class K(F,A):
	def __init__(A,conn:Ì,message:C):A.conn=conn;super().__init__(f"{conn}: {message}")
	@property
	def pool(self):t.warn("The 'pool' property is deprecated and will be removed in urllib3 v2.1.0. Use 'conn' instead.",DeprecationWarning,stacklevel=2);return self.conn
class i(K):
	def __init__(B,host:C,conn:Ì,reason:s.gaierror):A=f"Failed to resolve '{host}' ({reason})";super().__init__(conn,A)
class a(S):0
class j(S):0
class P(S):0
class N(d,A):0
class D(N):
	def __init__(B,location:C):A=location;C=f"Failed to parse: {A}";super().__init__(C);B.location=A
class b(N):
	def __init__(B,scheme:C):A=scheme;C=f"Not supported URL scheme {A}";super().__init__(C);B.scheme=A
class G(A):GENERIC_ERROR='too many error responses';SPECIFIC_ERROR='too many {status_code} error responses'
class T(f):0
class k(T):0
class v(T):0
class l(T):0
class w(T):0
class U(f):0
class m(I,d):0
class n(A):0
class o(A,e):
	def __init__(A,partial:Q,expected:Q):A.partial=partial;A.expected=expected
	def __repr__(A):return'IncompleteRead(%i bytes read, %i more expected)'%(A.partial,A.expected)
class p(A,e):
	def __init__(A,response:x,length:r):B=response;A.partial=B.tell();A.expected=B.length_remaining;A.response=B;A.length=length
	def __repr__(A):return'InvalidChunkLength(got length %r, %i bytes read)'%(A.length,A.partial)
class H(A):0
class q(AssertionError,b):
	def __init__(C,scheme:C|E):
		A=scheme
		if A=='localhost':A=E
		if A is E:B='Proxy URL had no scheme, should start with http:// or https://'
		else:B=f"Proxy URL had unsupported scheme {A}, should use http:// or https://"
		super().__init__(B)
class V(d):0
class W(A):
	def __init__(B,defects:list[u],unparsed_data:r|C|E):A=f"{defects or"Unknown"}, unparsed data: {unparsed_data!r}";super().__init__(A)
class c(A):0