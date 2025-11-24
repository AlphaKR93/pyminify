O='Expected instance of hashes.HashAlgorithm.'
L=TypeError
H=isinstance
B=int
import abc,typing as I
from C.D.D import hashes as A
from C.D.D.A import C
from C.D.D.D import rsa as J
class E(C):name='EMSA-PKCS1-v1_5'
class D:0
class F:0
class G:0
class K(C):
	MAX_LENGTH=D();AUTO=F();DIGEST_LENGTH=G();name='EMSA-PSS';_salt_length:I.Union[B,D,F,G]
	def __init__(C,mgf:M,salt_length:I.Union[B,D,F,G]):
		A=salt_length;C._mgf=mgf
		if not H(A,(B,D,F,G)):raise L('salt_length must be an integer, MAX_LENGTH, DIGEST_LENGTH, or AUTO')
		if H(A,B)and A<0:raise ValueError('salt_length must be zero or greater.')
		C._salt_length=A
class d(C):
	name='EME-OAEP'
	def __init__(B,mgf:M,algorithm:A.HashAlgorithm,label:I.Optional[bytes]):
		C=algorithm
		if not H(C,A.HashAlgorithm):raise L(O)
		B._mgf=mgf;B._algorithm=C;B._label=label
class M(metaclass=abc.ABCMeta):_algorithm:A.HashAlgorithm
class e(M):
	MAX_LENGTH=D()
	def __init__(C,algorithm:A.HashAlgorithm):
		B=algorithm
		if not H(B,A.HashAlgorithm):raise L(O)
		C._algorithm=B
def N(key:I.Union[J.RSAPrivateKey,J.RSAPublicKey],hash_algorithm:A.HashAlgorithm):
	if not H(key,(J.RSAPrivateKey,J.RSAPublicKey)):raise L('key must be an RSA public or private key')
	B=(key.key_size+6)//8;A=B-hash_algorithm.digest_size-2;assert A>=0;return A