W=None
S=isinstance
N='initialization_vector'
K=len
J=ValueError
F=property
E=bytes
import abc as I,typing as U
from C import utils as L
from C.B import A,B
from C.D.D.B import C,D
from C.D.D.E import algorithms as X
class G(metaclass=I.ABCMeta):
	@F
	@I.abstractmethod
	def name(self):0
	@I.abstractmethod
	def validate_for_algorithm(self,algorithm:D):0
class M(G,metaclass=I.ABCMeta):
	@F
	@I.abstractmethod
	def initialization_vector(self):0
class Y(G,metaclass=I.ABCMeta):
	@F
	@I.abstractmethod
	def tweak(self):0
class a(G,metaclass=I.ABCMeta):
	@F
	@I.abstractmethod
	def nonce(self):0
class b(G,metaclass=I.ABCMeta):
	@F
	@I.abstractmethod
	def tag(self):0
def P(self:G,algorithm:D):
	A=algorithm
	if A.key_size>256 and A.name=='AES':raise J('Only 128, 192, and 256 bit keys are allowed for this AES mode')
def c(self:M,algorithm:C):
	A=self
	if K(A.initialization_vector)*8!=algorithm.block_size:raise J('Invalid IV size ({}) for {}.'.format(K(A.initialization_vector),A.name))
def d(nonce:E,name:str,algorithm:D):
	E=algorithm;D=nonce
	if not S(E,C):raise A(f"{name} requires a block cipher algorithm",B.UNSUPPORTED_CIPHER)
	if K(D)*8!=E.block_size:raise J(f"Invalid nonce size ({K(D)}) for {name}.")
def R(self:M,algorithm:D):
	E=algorithm;D=self
	if not S(E,C):raise A(f"{D} requires a block cipher algorithm",B.UNSUPPORTED_CIPHER)
	P(D,E);c(D,E)
class H(M):
	name='CBC'
	def __init__(B,initialization_vector:E):A=initialization_vector;L._check_byteslike(N,A);B._initialization_vector=A
	@F
	def initialization_vector(self):return self._initialization_vector
	validate_for_algorithm=R
class XTS(Y):
	name='XTS'
	def __init__(B,tweak:E):
		A=tweak;L._check_byteslike('tweak',A)
		if K(A)!=16:raise J('tweak must be 128-bits (16 bytes)')
		B._tweak=A
	@F
	def tweak(self):return self._tweak
	def validate_for_algorithm(B,algorithm:D):
		A=algorithm
		if S(A,(X.AES128,X.AES256)):raise TypeError('The AES128 and AES256 classes do not support XTS, please use the standard AES class instead.')
		if A.key_size not in(256,512):raise J('The XTS specification requires a 256-bit key for AES-128-XTS and 512-bit key for AES-256-XTS')
class Z(G):name='ECB';validate_for_algorithm=P
class O(M):
	name='OFB'
	def __init__(B,initialization_vector:E):A=initialization_vector;L._check_byteslike(N,A);B._initialization_vector=A
	@F
	def initialization_vector(self):return self._initialization_vector
	validate_for_algorithm=R
class Q(M):
	name='CFB'
	def __init__(B,initialization_vector:E):A=initialization_vector;L._check_byteslike(N,A);B._initialization_vector=A
	@F
	def initialization_vector(self):return self._initialization_vector
	validate_for_algorithm=R
class V(M):
	name='CFB8'
	def __init__(B,initialization_vector:E):A=initialization_vector;L._check_byteslike(N,A);B._initialization_vector=A
	@F
	def initialization_vector(self):return self._initialization_vector
	validate_for_algorithm=R
class T(a):
	name='CTR'
	def __init__(B,nonce:E):A=nonce;L._check_byteslike('nonce',A);B._nonce=A
	@F
	def nonce(self):return self._nonce
	def validate_for_algorithm(A,algorithm:D):B=algorithm;P(A,B);d(A.nonce,A.name,B)
class GCM(M,b):
	name='GCM';_MAX_ENCRYPTED_BYTES=(2**39-256)//8;_MAX_AAD_BYTES=2**64//8
	def __init__(D,initialization_vector:E,tag:U.Optional[E]=W,min_tag_length:int=16):
		C=min_tag_length;B=tag;A=initialization_vector;L._check_byteslike(N,A)
		if K(A)<8 or K(A)>128:raise J('initialization_vector must be between 8 and 128 bytes (64 and 1024 bits).')
		D._initialization_vector=A
		if B is not W:
			L._check_bytes('tag',B)
			if C<4:raise J('min_tag_length must be >= 4')
			if K(B)<C:raise J('Authentication tag must be {} bytes or longer.'.format(C))
		D._tag=B;D._min_tag_length=C
	@F
	def tag(self):return self._tag
	@F
	def initialization_vector(self):return self._initialization_vector
	def validate_for_algorithm(D,algorithm:D):
		E=algorithm;P(D,E)
		if not S(E,C):raise A('GCM requires a block cipher algorithm',B.UNSUPPORTED_CIPHER)
		F=E.block_size//8
		if D._tag is not W and K(D._tag)>F:raise J('Authentication tag cannot be more than {} bytes.'.format(F))