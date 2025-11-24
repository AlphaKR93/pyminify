e='SEED'
d='IDEA'
c='CAST5'
b='Blowfish'
a=range
Z=ValueError
K='AES'
I=int
G=property
F=frozenset
B=len
A=bytes
from C import utils as H
from C.D.D.E import C,D
def E(algorithm:D,key:A):
	C=algorithm;A=key;H._check_byteslike('key',A)
	if B(A)*8 not in C.key_sizes:raise Z('Invalid key size ({}) for {}.'.format(B(A)*8,C.name))
	return A
class X(C):
	name=K;block_size=128;key_sizes=F([128,192,256,512])
	def __init__(A,key:A):A.key=E(A,key)
	@G
	def key_size(self):return B(self.key)*8
class L(C):
	name=K;block_size=128;key_sizes=F([128]);key_size=128
	def __init__(A,key:A):A.key=E(A,key)
class M(C):
	name=K;block_size=128;key_sizes=F([256]);key_size=256
	def __init__(A,key:A):A.key=E(A,key)
class N(C):
	name='camellia';block_size=128;key_sizes=F([128,192,256])
	def __init__(A,key:A):A.key=E(A,key)
	@G
	def key_size(self):return B(self.key)*8
class J(C):
	name='3DES';block_size=64;key_sizes=F([64,128,192])
	def __init__(C,key:A):
		A=key
		if B(A)==8:A+=A+A
		elif B(A)==16:A+=A[:8]
		C.key=E(C,A)
	@G
	def key_size(self):return B(self.key)*8
class O(C):
	name=b;block_size=64;key_sizes=F(a(32,449,8))
	def __init__(A,key:A):A.key=E(A,key)
	@G
	def key_size(self):return B(self.key)*8
P=O
H.deprecated(O,__name__,'Blowfish has been deprecated',H.DeprecatedIn37,name=b)
class Q(C):
	name=c;block_size=64;key_sizes=F(a(40,129,8))
	def __init__(A,key:A):A.key=E(A,key)
	@G
	def key_size(self):return B(self.key)*8
R=Q
H.deprecated(Q,__name__,'CAST5 has been deprecated',H.DeprecatedIn37,name=c)
class S(D):
	name='RC4';key_sizes=F([40,56,64,80,128,160,192,256])
	def __init__(A,key:A):A.key=E(A,key)
	@G
	def key_size(self):return B(self.key)*8
class T(C):
	name=d;block_size=64;key_sizes=F([128])
	def __init__(A,key:A):A.key=E(A,key)
	@G
	def key_size(self):return B(self.key)*8
U=T
H.deprecated(T,__name__,'IDEA has been deprecated',H.DeprecatedIn37,name=d)
class V(C):
	name=e;block_size=128;key_sizes=F([128])
	def __init__(A,key:A):A.key=E(A,key)
	@G
	def key_size(self):return B(self.key)*8
W=V
H.deprecated(V,__name__,'SEED has been deprecated',H.DeprecatedIn37,name=e)
class Y(D):
	name='ChaCha20';key_sizes=F([256])
	def __init__(A,key:A,nonce:A):
		C=nonce;A.key=E(A,key);H._check_byteslike('nonce',C)
		if B(C)!=16:raise Z('nonce must be 128-bits (16 bytes)')
		A._nonce=C
	@G
	def nonce(self):return self._nonce
	@G
	def key_size(self):return B(self.key)*8
class SM4(C):
	name='SM4';block_size=128;key_sizes=F([128])
	def __init__(A,key:A):A.key=E(A,key)
	@G
	def key_size(self):return B(self.key)*8