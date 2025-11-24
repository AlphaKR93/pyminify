S='Password must be 1 or more bytes.'
R='Raw'
Q='OpenSSH'
P=TypeError
O=isinstance
M=int
J=bytes
G=None
D=ValueError
import abc,typing as E
from C import utils as H
from C.D.D.H import V
class K(H.Enum):PBESv1SHA1And3KeyTripleDESCBC='PBESv1 using SHA1 and 3-Key TripleDES';PBESv2SHA256AndAES256CBC='PBESv2 using SHA256 PBKDF2 and AES256 CBC'
class F(H.Enum):PEM='PEM';DER='DER';OpenSSH=Q;Raw=R;X962='ANSI X9.62';SMIME='S/MIME'
class B(H.Enum):
	PKCS8='PKCS8';TraditionalOpenSSL='TraditionalOpenSSL';Raw=R;OpenSSH=Q;PKCS12='PKCS12'
	def encryption_builder(C):
		if C not in(B.OpenSSH,B.PKCS12):raise D('encryption_builder only supported with PrivateFormat.OpenSSH and PrivateFormat.PKCS12')
		return A(C)
class I(H.Enum):SubjectPublicKeyInfo='X.509 subjectPublicKeyInfo with PKCS#1';PKCS1='Raw PKCS#1';OpenSSH=Q;Raw=R;CompressedPoint='X9.62 Compressed Point';UncompressedPoint='X9.62 Uncompressed Point'
class T(H.Enum):PKCS3='PKCS3'
class C(metaclass=abc.ABCMeta):0
class U(C):
	def __init__(B,password:J):
		A=password
		if not O(A,J)or len(A)==0:raise D(S)
		B.password=A
class N(C):0
class A:
	def __init__(A,format:B,*,_kdf_rounds:E.Optional[M]=G,_hmac_hash:E.Optional[V]=G,_key_cert_algorithm:E.Optional[K]=G):A._format=format;A._kdf_rounds=_kdf_rounds;A._hmac_hash=_hmac_hash;A._key_cert_algorithm=_key_cert_algorithm
	def kdf_rounds(B,rounds:M):
		C=rounds
		if B._kdf_rounds is not G:raise D('kdf_rounds already set')
		if not O(C,M):raise P('kdf_rounds must be an integer')
		if C<1:raise D('kdf_rounds must be a positive integer')
		return A(B._format,_kdf_rounds=C,_hmac_hash=B._hmac_hash,_key_cert_algorithm=B._key_cert_algorithm)
	def hmac_hash(C,algorithm:V):
		if C._format is not B.PKCS12:raise P('hmac_hash only supported with PrivateFormat.PKCS12')
		if C._hmac_hash is not G:raise D('hmac_hash already set')
		return A(C._format,_kdf_rounds=C._kdf_rounds,_hmac_hash=algorithm,_key_cert_algorithm=C._key_cert_algorithm)
	def key_cert_algorithm(C,algorithm:K):
		if C._format is not B.PKCS12:raise P('key_cert_algorithm only supported with PrivateFormat.PKCS12')
		if C._key_cert_algorithm is not G:raise D('key_cert_algorithm already set')
		return A(C._format,_kdf_rounds=C._kdf_rounds,_hmac_hash=C._hmac_hash,_key_cert_algorithm=algorithm)
	def build(A,password:J):
		B=password
		if not O(B,J)or len(B)==0:raise D(S)
		return L(A._format,B,kdf_rounds=A._kdf_rounds,hmac_hash=A._hmac_hash,key_cert_algorithm=A._key_cert_algorithm)
class L(C):
	def __init__(A,format:B,password:J,*,kdf_rounds:E.Optional[M],hmac_hash:E.Optional[V],key_cert_algorithm:E.Optional[K]):A._format=format;A.password=password;A._kdf_rounds=kdf_rounds;A._hmac_hash=hmac_hash;A._key_cert_algorithm=key_cert_algorithm