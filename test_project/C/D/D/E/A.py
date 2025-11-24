a='bit_length must be 128, 192, or 256'
Z='bit_length must be an integer'
Y='associated_data'
X='nonce'
U='data'
T='Data or associated data too long. Max 2**31 - 1 bytes'
S='key'
R=OverflowError
Q=classmethod
O=TypeError
N=isinstance
I=b''
H=None
G=int
D=ValueError
B=len
A=bytes
import os as P,typing as E
from C import exceptions as K,utils as C
from C.D.B.A import aead as F
from C.D.B.A.B import Î
from cryptography.hazmat.bindings._rust import FixedPool as b
class L:
	_MAX_SIZE=2**31-1
	def __init__(A,key:A):
		E=key
		if not Î.aead_cipher_supported(A):raise K.UnsupportedAlgorithm('ChaCha20Poly1305 is not supported by this version of OpenSSL',K._Reasons.UNSUPPORTED_CIPHER)
		C._check_byteslike(S,E)
		if B(E)!=32:raise D('ChaCha20Poly1305 key must be 32 bytes.')
		A._key=E;A._pool=b(A._create_fn)
	@Q
	def generate_key(cls):return P.urandom(32)
	def _create_fn(A):return F._aead_create_ctx(Î,A,A._key)
	def encrypt(A,nonce:A,data:A,associated_data:E.Optional[A]):
		E=nonce;D=data;C=associated_data
		if C is H:C=I
		if B(D)>A._MAX_SIZE or B(C)>A._MAX_SIZE:raise R(T)
		A._check_params(E,D,C)
		with A._pool.acquire()as G:return F._encrypt(Î,A,E,D,[C],16,G)
	def decrypt(B,nonce:A,data:A,associated_data:E.Optional[A]):
		C=nonce;A=associated_data
		if A is H:A=I
		B._check_params(C,data,A)
		with B._pool.acquire()as D:return F._decrypt(Î,B,C,data,[A],16,D)
	def _check_params(E,nonce:A,data:A,associated_data:A):
		A=nonce;C._check_byteslike(X,A);C._check_byteslike(U,data);C._check_byteslike(Y,associated_data)
		if B(A)!=12:raise D('Nonce must be 12 bytes')
class J:
	_MAX_SIZE=2**31-1
	def __init__(A,key:A,tag_length:G=16):
		F=tag_length;E=key;C._check_byteslike(S,E)
		if B(E)not in(16,24,32):raise D('AESCCM key must be 128, 192, or 256 bits.')
		A._key=E
		if not N(F,G):raise O('tag_length must be an integer')
		if F not in(4,6,8,10,12,14,16):raise D('Invalid tag_length')
		A._tag_length=F
		if not Î.aead_cipher_supported(A):raise K.UnsupportedAlgorithm('AESCCM is not supported by this version of OpenSSL',K._Reasons.UNSUPPORTED_CIPHER)
	@Q
	def generate_key(cls,bit_length:G):
		A=bit_length
		if not N(A,G):raise O(Z)
		if A not in(128,192,256):raise D(a)
		return P.urandom(A//8)
	def encrypt(A,nonce:A,data:A,associated_data:E.Optional[A]):
		E=nonce;D=data;C=associated_data
		if C is H:C=I
		if B(D)>A._MAX_SIZE or B(C)>A._MAX_SIZE:raise R(T)
		A._check_params(E,D,C);A._validate_lengths(E,B(D));return F._encrypt(Î,A,E,D,[C],A._tag_length)
	def decrypt(B,nonce:A,data:A,associated_data:E.Optional[A]):
		C=nonce;A=associated_data
		if A is H:A=I
		B._check_params(C,data,A);return F._decrypt(Î,B,C,data,[A],B._tag_length)
	def _validate_lengths(C,nonce:A,data_len:G):
		A=15-B(nonce)
		if 2**(8*A)<data_len:raise D('Data too long for nonce')
	def _check_params(E,nonce:A,data:A,associated_data:A):
		A=nonce;C._check_byteslike(X,A);C._check_byteslike(U,data);C._check_byteslike(Y,associated_data)
		if not 7<=B(A)<=13:raise D('Nonce must be between 7 and 13 bytes')
class V:
	_MAX_SIZE=2**31-1
	def __init__(E,key:A):
		A=key;C._check_byteslike(S,A)
		if B(A)not in(16,24,32):raise D('AESGCM key must be 128, 192, or 256 bits.')
		E._key=A
	@Q
	def generate_key(cls,bit_length:G):
		A=bit_length
		if not N(A,G):raise O(Z)
		if A not in(128,192,256):raise D(a)
		return P.urandom(A//8)
	def encrypt(C,nonce:A,data:A,associated_data:E.Optional[A]):
		E=nonce;D=data;A=associated_data
		if A is H:A=I
		if B(D)>C._MAX_SIZE or B(A)>C._MAX_SIZE:raise R(T)
		C._check_params(E,D,A);return F._encrypt(Î,C,E,D,[A],16)
	def decrypt(B,nonce:A,data:A,associated_data:E.Optional[A]):
		C=nonce;A=associated_data
		if A is H:A=I
		B._check_params(C,data,A);return F._decrypt(Î,B,C,data,[A],16)
	def _check_params(E,nonce:A,data:A,associated_data:A):
		A=nonce;C._check_byteslike(X,A);C._check_byteslike(U,data);C._check_byteslike(Y,associated_data)
		if B(A)<8 or B(A)>128:raise D('Nonce must be between 8 and 128 bytes')
class W:
	_MAX_SIZE=2**31-1
	def __init__(E,key:A):
		A=key;C._check_byteslike(S,A)
		if B(A)not in(16,24,32):raise D('AESOCB3 key must be 128, 192, or 256 bits.')
		E._key=A
		if not Î.aead_cipher_supported(E):raise K.UnsupportedAlgorithm('OCB3 is not supported by this version of OpenSSL',K._Reasons.UNSUPPORTED_CIPHER)
	@Q
	def generate_key(cls,bit_length:G):
		A=bit_length
		if not N(A,G):raise O(Z)
		if A not in(128,192,256):raise D(a)
		return P.urandom(A//8)
	def encrypt(C,nonce:A,data:A,associated_data:E.Optional[A]):
		E=nonce;D=data;A=associated_data
		if A is H:A=I
		if B(D)>C._MAX_SIZE or B(A)>C._MAX_SIZE:raise R(T)
		C._check_params(E,D,A);return F._encrypt(Î,C,E,D,[A],16)
	def decrypt(B,nonce:A,data:A,associated_data:E.Optional[A]):
		C=nonce;A=associated_data
		if A is H:A=I
		B._check_params(C,data,A);return F._decrypt(Î,B,C,data,[A],16)
	def _check_params(E,nonce:A,data:A,associated_data:A):
		A=nonce;C._check_byteslike(X,A);C._check_byteslike(U,data);C._check_byteslike(Y,associated_data)
		if B(A)<12 or B(A)>15:raise D('Nonce must be between 12 and 15 bytes')
class M:
	_MAX_SIZE=2**31-1
	def __init__(E,key:A):
		A=key;C._check_byteslike(S,A)
		if B(A)not in(32,48,64):raise D('AESSIV key must be 256, 384, or 512 bits.')
		E._key=A
		if not Î.aead_cipher_supported(E):raise K.UnsupportedAlgorithm('AES-SIV is not supported by this version of OpenSSL',K._Reasons.UNSUPPORTED_CIPHER)
	@Q
	def generate_key(cls,bit_length:G):
		A=bit_length
		if not N(A,G):raise O(Z)
		if A not in(256,384,512):raise D('bit_length must be 256, 384, or 512')
		return P.urandom(A//8)
	def encrypt(C,data:A,associated_data:E.Optional[E.List[A]]):
		D=data;A=associated_data
		if A is H:A=[]
		C._check_params(D,A)
		if B(D)>C._MAX_SIZE or any(B(A)>C._MAX_SIZE for A in A):raise R(T)
		return F._encrypt(Î,C,I,D,A,16)
	def decrypt(B,data:A,associated_data:E.Optional[E.List[A]]):
		A=associated_data
		if A is H:A=[]
		B._check_params(data,A);return F._decrypt(Î,B,I,data,A,16)
	def _check_params(F,data:A,associated_data:E.List[A]):
		A=associated_data;C._check_byteslike(U,data)
		if B(data)==0:raise D('data must not be zero length')
		if not N(A,list):raise O('associated_data must be a list of bytes-like objects or None')
		for E in A:C._check_byteslike('associated_data elements',E)