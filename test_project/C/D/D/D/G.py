T=False
S=NotImplemented
R=divmod
P=None
O=TypeError
M=bool
G=isinstance
F=property
E=bytes
B=ValueError
A=int
import abc as D,typing as I
from math import gcd
from C.D.D import _serialization as K,hashes as N
from C.D.D.A import C
from C.D.D.D import utils as Q
class J(metaclass=D.ABCMeta):
	@D.abstractmethod
	def decrypt(self,ciphertext:E,padding:C):0
	@F
	@D.abstractmethod
	def key_size(self):0
	@D.abstractmethod
	def public_key(self):0
	@D.abstractmethod
	def sign(self,data:E,padding:C,algorithm:I.Union[Q.Prehashed,N.HashAlgorithm]):0
	@D.abstractmethod
	def private_numbers(self):0
	@D.abstractmethod
	def private_bytes(self,encoding:K.Encoding,format:K.PrivateFormat,encryption_algorithm:K.KeySerializationEncryption):0
X=J
class ó(metaclass=D.ABCMeta):
	@D.abstractmethod
	def encrypt(self,plaintext:E,padding:C):0
	@F
	@D.abstractmethod
	def key_size(self):0
	@D.abstractmethod
	def public_numbers(self):0
	@D.abstractmethod
	def public_bytes(self,encoding:K.Encoding,format:K.PublicFormat):0
	@D.abstractmethod
	def verify(self,signature:E,data:E,padding:C,algorithm:I.Union[Q.Prehashed,N.HashAlgorithm]):0
	@D.abstractmethod
	def recover_data_from_signature(self,signature:E,padding:C,algorithm:I.Optional[N.HashAlgorithm]):0
	@D.abstractmethod
	def __eq__(self,other:object):0
Y=ó
def Z(public_exponent:A,key_size:A,backend:I.Any=P):B=key_size;A=public_exponent;from C.D.B.A.B import Î;U(A,B);return Î.generate_rsa_private_key(A,B)
def U(public_exponent:A,key_size:A):
	if public_exponent not in(3,65537):raise B('public_exponent must be either 3 (for legacy compatibility) or 65537. Almost everyone should choose 65537 here!')
	if key_size<512:raise B('key_size must be at least 512-bits.')
def a(p:A,q:A,private_exponent:A,dmp1:A,dmq1:A,iqmp:A,public_exponent:A,modulus:A):
	C=public_exponent;A=modulus
	if A<3:raise B('modulus must be >= 3.')
	if p>=A:raise B('p must be < modulus.')
	if q>=A:raise B('q must be < modulus.')
	if dmp1>=A:raise B('dmp1 must be < modulus.')
	if dmq1>=A:raise B('dmq1 must be < modulus.')
	if iqmp>=A:raise B('iqmp must be < modulus.')
	if private_exponent>=A:raise B('private_exponent must be < modulus.')
	if C<3 or C>=A:raise B('public_exponent must be >= 3 and < modulus.')
	if C&1==0:raise B('public_exponent must be odd.')
	if dmp1&1==0:raise B('dmp1 must be odd.')
	if dmq1&1==0:raise B('dmq1 must be odd.')
	if p*q!=A:raise B('p*q must equal modulus.')
def b(e:A,n:A):
	if n<3:raise B('n must be >= 3.')
	if e<3 or e>=n:raise B('e must be >= 3 and < n.')
	if e&1==0:raise B('e must be odd.')
def V(e:A,m:A):
	B,C=1,0;D,A=e,m
	while A>0:E,F=R(D,A);G=B-E*C;D,A,B,C=A,F,C,G
	return B%m
def c(p:A,q:A):return V(q,p)
def d(private_exponent:A,p:A):return private_exponent%(p-1)
def e(private_exponent:A,q:A):return private_exponent%(q-1)
W=1000
def f(n:A,e:A,d:A):
	I=d*e-1;A=I
	while A%2==0:A=A//2
	E=T;F=2
	while not E and F<W:
		G=A
		while G<I:
			C=pow(F,G,n)
			if C!=1 and C!=n-1 and pow(C,2,n)==1:D=gcd(C+1,n);E=True;break
			G*=2
		F+=2
	if not E:raise B('Unable to compute factors p and q from exponent d.')
	H,J=R(n,D);assert J==0;D,H=sorted((D,H),reverse=True);return D,H
class L:
	def __init__(B,p:A,q:A,d:A,dmp1:A,dmq1:A,iqmp:A,public_numbers:H):
		C=public_numbers
		if not G(p,A)or not G(q,A)or not G(d,A)or not G(dmp1,A)or not G(dmq1,A)or not G(iqmp,A):raise O('RSAPrivateNumbers p, q, d, dmp1, dmq1, iqmp arguments must all be an integers.')
		if not G(C,H):raise O('RSAPrivateNumbers public_numbers must be an RSAPublicNumbers instance.')
		B._p=p;B._q=q;B._d=d;B._dmp1=dmp1;B._dmq1=dmq1;B._iqmp=iqmp;B._public_numbers=C
	@F
	def p(self):return self._p
	@F
	def q(self):return self._q
	@F
	def d(self):return self._d
	@F
	def dmp1(self):return self._dmp1
	@F
	def dmq1(self):return self._dmq1
	@F
	def iqmp(self):return self._iqmp
	@F
	def public_numbers(self):return self._public_numbers
	def private_key(A,backend:I.Any=P,*,unsafe_skip_rsa_key_validation:M=T):from C.D.B.A.B import Î;return Î.load_rsa_private_numbers(A,unsafe_skip_rsa_key_validation)
	def __eq__(B,other:object):
		A=other
		if not G(A,L):return S
		return B.p==A.p and B.q==A.q and B.d==A.d and B.dmp1==A.dmp1 and B.dmq1==A.dmq1 and B.iqmp==A.iqmp and B.public_numbers==A.public_numbers
	def __hash__(A):return hash((A.p,A.q,A.d,A.dmp1,A.dmq1,A.iqmp,A.public_numbers))
class H:
	def __init__(B,e:A,n:A):
		if not G(e,A)or not G(n,A):raise O('RSAPublicNumbers arguments must be integers.')
		B._e=e;B._n=n
	@F
	def e(self):return self._e
	@F
	def n(self):return self._n
	def public_key(A,backend:I.Any=P):from C.D.B.A.B import Î;return Î.load_rsa_public_numbers(A)
	def __repr__(A):return'<RSAPublicNumbers(e={0.e}, n={0.n})>'.format(A)
	def __eq__(B,other:object):
		A=other
		if not G(A,H):return S
		return B.e==A.e and B.n==A.n
	def __hash__(A):return hash((A.e,A.n))