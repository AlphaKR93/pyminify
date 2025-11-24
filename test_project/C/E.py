Q='_module'
P=property
K=None
J=setattr
I=getattr
H=TypeError
G=int
F=isinstance
E=bytes
A=str
import enum,sys,types as L,typing as B,warnings as M
class C(UserWarning):0
R=C
S=C
T=C
U=C
def V(name:A,value:E):
	if not F(value,E):raise H(f"{name} must be bytes")
def N(name:A,value:E):
	try:memoryview(value)
	except H:raise H(f"{name} must be bytes-like")
def W(integer:G,length:B.Optional[G]=K):A=integer;return A.to_bytes(length or(A.bit_length()+7)//8 or 1,'big')
def X(obj:B.Any):from cryptography.hazmat.bindings._rust import _openssl as A;B=A.ffi.from_buffer(obj);return B,G(B)
class Y(Exception):0
class D:
	def __init__(A,value:object,message:A,warning_class):A.value=value;A.message=message;A.warning_class=warning_class
class O(L.ModuleType):
	def __init__(B,module:L.ModuleType):A=module;super().__init__(A.__name__);B.__dict__[Q]=A
	def __getattr__(B,attr:A):
		A=I(B._module,attr)
		if F(A,D):M.warn(A.message,A.warning_class,stacklevel=2);A=A.value
		return A
	def __setattr__(A,attr:A,value:object):J(A._module,attr,value)
	def __delattr__(B,attr:A):
		A=I(B._module,attr)
		if F(A,D):M.warn(A.message,A.warning_class,stacklevel=2)
		delattr(B._module,attr)
	def __dir__(A):return[Q]+dir(A._module)
def Z(value:object,module_name:A,message:A,warning_class:B.Type[Warning],name:B.Optional[A]=K):
	B=module_name;A=sys.modules[B]
	if not F(A,O):sys.modules[B]=A=O(A)
	C=D(value,message,warning_class)
	if name is not K:J(A,name,C)
	return C
def a(func:B.Callable):
	B=f"_cached_{func}";C=object()
	def A(instance:object):
		A=instance;D=I(A,B,C)
		if D is not C:return D
		E=func(A);J(A,B,E);return E
	return P(A)
class b(enum.Enum):
	def __repr__(A):return f"<{A.__class__.__name__}.{A._name_}: {A._value_!r}>"
	def __str__(A):return f"{A.__class__.__name__}.{A._name_}"