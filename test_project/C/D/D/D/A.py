S=ValueError
Q=NotImplemented
P=bytes
O=bool
I=None
H=TypeError
D=property
C=isinstance
A=int
import abc as B,typing as F
from cryptography.hazmat.bindings._rust import openssl as J
from C.D.D import _serialization as E
def T(generator:A,key_size:A,backend:F.Any=I):from C.D.B.A.B import Î;return Î.generate_dh_parameters(generator,key_size)
class K:
	def __init__(B,p:A,g:A,q:F.Optional[A]=I):
		if not C(p,A)or not C(g,A):raise H('p and g must be integers')
		if q is not I and not C(q,A):raise H('q must be integer or None')
		if g<2:raise S('DH generator must be 2 or greater')
		if p.bit_length()<J.dh.MIN_MODULUS_SIZE:raise S(f"p (modulus) must be at least {J.dh.MIN_MODULUS_SIZE}-bit")
		B._p=p;B._g=g;B._q=q
	def __eq__(B,other:object):
		A=other
		if not C(A,K):return Q
		return B._p==A._p and B._g==A._g and B._q==A._q
	def parameters(A,backend:F.Any=I):from C.D.B.A.B import Î;return Î.load_dh_parameter_numbers(A)
	@D
	def p(self):return self._p
	@D
	def g(self):return self._g
	@D
	def q(self):return self._q
class L:
	def __init__(B,y:A,parameter_numbers:K):
		D=parameter_numbers
		if not C(y,A):raise H('y must be an integer.')
		if not C(D,K):raise H('parameters must be an instance of DHParameterNumbers.')
		B._y=y;B._parameter_numbers=D
	def __eq__(B,other:object):
		A=other
		if not C(A,L):return Q
		return B._y==A._y and B._parameter_numbers==A._parameter_numbers
	def public_key(A,backend:F.Any=I):from C.D.B.A.B import Î;return Î.load_dh_public_numbers(A)
	@D
	def y(self):return self._y
	@D
	def parameter_numbers(self):return self._parameter_numbers
class R:
	def __init__(B,x:A,public_numbers:L):
		D=public_numbers
		if not C(x,A):raise H('x must be an integer.')
		if not C(D,L):raise H('public_numbers must be an instance of DHPublicNumbers.')
		B._x=x;B._public_numbers=D
	def __eq__(B,other:object):
		A=other
		if not C(A,R):return Q
		return B._x==A._x and B._public_numbers==A._public_numbers
	def private_key(A,backend:F.Any=I):from C.D.B.A.B import Î;return Î.load_dh_private_numbers(A)
	@D
	def public_numbers(self):return self._public_numbers
	@D
	def x(self):return self._x
class G(metaclass=B.ABCMeta):
	@B.abstractmethod
	def generate_private_key(self):0
	@B.abstractmethod
	def parameter_bytes(self,encoding:E.Encoding,format:E.ParameterFormat):0
	@B.abstractmethod
	def parameter_numbers(self):0
U=G
G.register(J.dh.DHParameters)
class M(metaclass=B.ABCMeta):
	@D
	@B.abstractmethod
	def key_size(self):0
	@B.abstractmethod
	def parameters(self):0
	@B.abstractmethod
	def public_numbers(self):0
	@B.abstractmethod
	def public_bytes(self,encoding:E.Encoding,format:E.PublicFormat):0
	@B.abstractmethod
	def __eq__(self,other:object):0
V=M
M.register(J.dh.DHPublicKey)
class N(metaclass=B.ABCMeta):
	@D
	@B.abstractmethod
	def key_size(self):0
	@B.abstractmethod
	def public_key(self):0
	@B.abstractmethod
	def parameters(self):0
	@B.abstractmethod
	def exchange(self,peer_public_key:M):0
	@B.abstractmethod
	def private_numbers(self):0
	@B.abstractmethod
	def private_bytes(self,encoding:E.Encoding,format:E.PrivateFormat,encryption_algorithm:E.KeySerializationEncryption):0
W=N
N.register(J.dh.DHPrivateKey)