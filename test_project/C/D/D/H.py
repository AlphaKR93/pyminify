O='digest_size must be a positive integer'
N='digest_size must be an integer'
M=TypeError
L=isinstance
K=bytes
E=ValueError
D=None
C=property
A=int
import abc as B
from cryptography.hazmat.bindings._rust import openssl as Q
class V(metaclass=B.ABCMeta):
	@C
	@B.abstractmethod
	def name(self):0
	@C
	@B.abstractmethod
	def digest_size(self):0
	@C
	@B.abstractmethod
	def block_size(self):0
class I(metaclass=B.ABCMeta):
	@C
	@B.abstractmethod
	def algorithm(self):0
	@B.abstractmethod
	def update(self,data:K):0
	@B.abstractmethod
	def finalize(self):0
	@B.abstractmethod
	def copy(self):0
R=Q.hashes.Hash
I.register(R)
class J(metaclass=B.ABCMeta):0
class F(V):name='sha1';digest_size=20;block_size=64
class S(V):name='sha512-224';digest_size=28;block_size=128
class T(V):name='sha512-256';digest_size=32;block_size=128
class U(V):name='sha224';digest_size=28;block_size=64
class G(V):name='sha256';digest_size=32;block_size=64
class W(V):name='sha384';digest_size=48;block_size=128
class H(V):name='sha512';digest_size=64;block_size=128
class X(V):name='sha3-224';digest_size=28;block_size=D
class Y(V):name='sha3-256';digest_size=32;block_size=D
class Z(V):name='sha3-384';digest_size=48;block_size=D
class a(V):name='sha3-512';digest_size=64;block_size=D
class b(V,J):
	name='shake128';block_size=D
	def __init__(C,digest_size:A):
		B=digest_size
		if not L(B,A):raise M(N)
		if B<1:raise E(O)
		C._digest_size=B
	@C
	def digest_size(self):return self._digest_size
class c(V,J):
	name='shake256';block_size=D
	def __init__(C,digest_size:A):
		B=digest_size
		if not L(B,A):raise M(N)
		if B<1:raise E(O)
		C._digest_size=B
	@C
	def digest_size(self):return self._digest_size
class d(V):name='md5';digest_size=16;block_size=64
class e(V):
	name='blake2b';_max_digest_size=64;_min_digest_size=1;block_size=128
	def __init__(B,digest_size:A):
		A=digest_size
		if A!=64:raise E('Digest size must be 64')
		B._digest_size=A
	@C
	def digest_size(self):return self._digest_size
class f(V):
	name='blake2s';block_size=64;_max_digest_size=32;_min_digest_size=1
	def __init__(B,digest_size:A):
		A=digest_size
		if A!=32:raise E('Digest size must be 32')
		B._digest_size=A
	@C
	def digest_size(self):return self._digest_size
class g(V):name='sm3';digest_size=32;block_size=64