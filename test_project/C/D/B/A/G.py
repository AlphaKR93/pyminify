g='Only MGF1 is supported by this backend.'
f=property
b='unsigned char[]'
a='size_t *'
X=TypeError
V=ValueError
U=len
Q=int
P='BIGNUM **'
I=isinstance
C=bytes
import threading as h,typing as M
from C.B import T,A,B
from C.D.B.A.H import R
from C.D.D import hashes as S,serialization as W
from C.D.D.D import utils as Y
from C.D.D.D.F import e,d,K,AsymmetricPadding as O,E,F,G,D,N
from C.D.D.D.G import J,L,ó,H
def i(backend:o,pss:K,key:M.Union[J,ó],hash_algorithm:S.HashAlgorithm):
	B=hash_algorithm;A=pss._salt_length
	if I(A,D):return N(key,B)
	elif I(A,G):return B.digest_size
	elif I(A,F):
		if I(key,J):raise V('PSS salt length can only be set to AUTO when verifying')
		return backend._lib.RSA_PSS_SALTLEN_AUTO
	else:return A
def c(backend:o,key:M.Union[â,á],data:C,padding:O):
	D=backend;C=padding
	if not I(C,O):raise X('Padding must be an instance of AsymmetricPadding.')
	if I(C,E):F=D._lib.RSA_PKCS1_PADDING
	elif I(C,d):
		F=D._lib.RSA_PKCS1_OAEP_PADDING
		if not I(C._mgf,e):raise A(g,B.UNSUPPORTED_MGF)
		if not D.rsa_padding_supported(C):raise A('This combination of padding and hash algorithm is not supported by this backend.',B.UNSUPPORTED_PADDING)
	else:raise A(f"{C.name} is not supported by this backend.",B.UNSUPPORTED_PADDING)
	return j(D,key,data,F,C)
def j(backend:o,key:M.Union[â,á],data:C,padding_enum:Q,padding:O):
	F=key;D=padding;A=backend
	if I(F,á):G=A._lib.EVP_PKEY_encrypt_init;H=A._lib.EVP_PKEY_encrypt
	else:G=A._lib.EVP_PKEY_decrypt_init;H=A._lib.EVP_PKEY_decrypt
	E=A._lib.EVP_PKEY_CTX_new(F._evp_pkey,A._ffi.NULL);A.openssl_assert(E!=A._ffi.NULL);E=A._ffi.gc(E,A._lib.EVP_PKEY_CTX_free);B=G(E);A.openssl_assert(B==1);B=A._lib.EVP_PKEY_CTX_set_rsa_padding(E,padding_enum);A.openssl_assert(B>0);J=A._lib.EVP_PKEY_size(F._evp_pkey);A.openssl_assert(J>0)
	if I(D,d):O=A._evp_md_non_null_from_algorithm(D._mgf._algorithm);B=A._lib.EVP_PKEY_CTX_set_rsa_mgf1_md(E,O);A.openssl_assert(B>0);P=A._evp_md_non_null_from_algorithm(D._algorithm);B=A._lib.EVP_PKEY_CTX_set_rsa_oaep_md(E,P);A.openssl_assert(B>0)
	if I(D,d)and D._label is not None and U(D._label)>0:K=A._lib.OPENSSL_malloc(U(D._label));A.openssl_assert(K!=A._ffi.NULL);A._ffi.memmove(K,D._label,U(D._label));B=A._lib.EVP_PKEY_CTX_set0_rsa_oaep_label(E,K,U(D._label));A.openssl_assert(B==1)
	L=A._ffi.new(a,J);N=A._ffi.new(b,J);B=H(E,N,L,data,U(data));R=A._ffi.buffer(N)[:L[0]];A._lib.ERR_clear_error()
	if B<=0:raise V('Encryption/decryption failed.')
	return R
def k(backend:o,key:M.Union[â,á],padding:O,algorithm:M.Optional[S.HashAlgorithm]):
	F=algorithm;D=backend;C=padding
	if not I(C,O):raise X('Expected provider of AsymmetricPadding.')
	G=D._lib.EVP_PKEY_size(key._evp_pkey);D.openssl_assert(G>0)
	if I(C,E):H=D._lib.RSA_PKCS1_PADDING
	elif I(C,K):
		if not I(C._mgf,e):raise A(g,B.UNSUPPORTED_MGF)
		if not I(F,S.HashAlgorithm):raise X('Expected instance of hashes.HashAlgorithm.')
		if G-F.digest_size-2<0:raise V('Digest too large for key size. Use a larger key or different digest.')
		H=D._lib.RSA_PKCS1_PSS_PADDING
	else:raise A(f"{C.name} is not supported by this backend.",B.UNSUPPORTED_PADDING)
	return H
def Z(backend:o,padding:O,algorithm:M.Optional[S.HashAlgorithm],key:M.Union[á,â],init_func:M.Callable[[M.Any],Q]):
	H=key;G=padding;F=algorithm;C=backend;J=k(C,H,G,F);D=C._lib.EVP_PKEY_CTX_new(H._evp_pkey,C._ffi.NULL);C.openssl_assert(D!=C._ffi.NULL);D=C._ffi.gc(D,C._lib.EVP_PKEY_CTX_free);E=init_func(D)
	if E!=1:L=C._consume_errors();raise V('Unable to sign/verify with this key',L)
	if F is not None:
		M=C._evp_md_non_null_from_algorithm(F);E=C._lib.EVP_PKEY_CTX_set_signature_md(D,M)
		if E<=0:C._consume_errors();raise A('{} is not supported by this backend for RSA signing.'.format(F.name),B.UNSUPPORTED_HASH)
	E=C._lib.EVP_PKEY_CTX_set_rsa_padding(D,J)
	if E<=0:C._consume_errors();raise A('{} is not supported for the RSA signature operation.'.format(G.name),B.UNSUPPORTED_PADDING)
	if I(G,K):assert I(F,S.HashAlgorithm);E=C._lib.EVP_PKEY_CTX_set_rsa_pss_saltlen(D,i(C,G,H,F));C.openssl_assert(E>0);N=C._evp_md_non_null_from_algorithm(G._mgf._algorithm);E=C._lib.EVP_PKEY_CTX_set_rsa_mgf1_md(D,N);C.openssl_assert(E>0)
	return D
def l(backend:o,padding:O,algorithm:S.HashAlgorithm,private_key:â,data:C):
	B=data;A=backend;E=Z(A,padding,algorithm,private_key,A._lib.EVP_PKEY_sign_init);C=A._ffi.new(a);D=A._lib.EVP_PKEY_sign(E,A._ffi.NULL,C,B,U(B));A.openssl_assert(D==1);F=A._ffi.new(b,C[0]);D=A._lib.EVP_PKEY_sign(E,F,C,B,U(B))
	if D!=1:G=A._consume_errors();raise V('Digest or salt length too long for key size. Use a larger key or shorter salt length if you are specifying a PSS salt',G)
	return A._ffi.buffer(F)[:]
def m(backend:o,padding:O,algorithm:S.HashAlgorithm,public_key:á,signature:C,data:C):
	B=signature;A=backend;D=Z(A,padding,algorithm,public_key,A._lib.EVP_PKEY_verify_init);C=A._lib.EVP_PKEY_verify(D,B,U(B),data,U(data));A.openssl_assert(C>=0)
	if C==0:A._consume_errors();raise T
def n(backend:o,padding:O,algorithm:M.Optional[S.HashAlgorithm],public_key:á,signature:C):
	D=signature;C=public_key;A=backend;G=Z(A,padding,algorithm,C,A._lib.EVP_PKEY_verify_recover_init);B=A._lib.EVP_PKEY_size(C._evp_pkey);A.openssl_assert(B>0);E=A._ffi.new(b,B);F=A._ffi.new(a,B);H=A._lib.EVP_PKEY_verify_recover(G,E,F,D,U(D));I=A._ffi.buffer(E)[:F[0]];A._lib.ERR_clear_error()
	if H!=1:raise T
	return I
class â(J):
	_evp_pkey:object;_rsa_cdata:object;_key_size:Q
	def __init__(A,backend:o,rsa_cdata,evp_pkey,*,unsafe_skip_rsa_key_validation:bool):
		I='Invalid private key';C=rsa_cdata;B=backend
		if not unsafe_skip_rsa_key_validation:
			H=B._lib.RSA_check_key(C)
			if H!=1:D=B._consume_errors();raise V(I,D)
			E=B._ffi.new(P);F=B._ffi.new(P);B._lib.RSA_get0_factors(C,E,F);B.openssl_assert(E[0]!=B._ffi.NULL);B.openssl_assert(F[0]!=B._ffi.NULL);J=B._lib.BN_is_odd(E[0]);K=B._lib.BN_is_odd(F[0])
			if J!=1 or K!=1:D=B._consume_errors();raise V(I,D)
		A._backend=B;A._rsa_cdata=C;A._evp_pkey=evp_pkey;A._blinded=False;A._blinding_lock=h.Lock();G=A._backend._ffi.new(P);A._backend._lib.RSA_get0_key(A._rsa_cdata,G,A._backend._ffi.NULL,A._backend._ffi.NULL);A._backend.openssl_assert(G[0]!=A._backend._ffi.NULL);A._key_size=A._backend._lib.BN_num_bits(G[0])
	def _enable_blinding(A):
		if not A._blinded:
			with A._blinding_lock:A._non_threadsafe_enable_blinding()
	def _non_threadsafe_enable_blinding(A):
		if not A._blinded:B=A._backend._lib.RSA_blinding_on(A._rsa_cdata,A._backend._ffi.NULL);A._backend.openssl_assert(B==1);A._blinded=True
	@f
	def key_size(self):return self._key_size
	def decrypt(A,ciphertext:C,padding:O):
		B=ciphertext;A._enable_blinding();C=(A.key_size+7)//8
		if C!=U(B):raise V('Ciphertext length must be equal to key size.')
		return c(A._backend,A,B,padding)
	def public_key(A):B=A._backend._lib.RSAPublicKey_dup(A._rsa_cdata);A._backend.openssl_assert(B!=A._backend._ffi.NULL);B=A._backend._ffi.gc(B,A._backend._lib.RSA_free);C=A._backend._rsa_cdata_to_evp_pkey(B);return á(A._backend,B,C)
	def private_numbers(A):B=A._backend._ffi.new(P);C=A._backend._ffi.new(P);D=A._backend._ffi.new(P);E=A._backend._ffi.new(P);F=A._backend._ffi.new(P);G=A._backend._ffi.new(P);I=A._backend._ffi.new(P);J=A._backend._ffi.new(P);A._backend._lib.RSA_get0_key(A._rsa_cdata,B,C,D);A._backend.openssl_assert(B[0]!=A._backend._ffi.NULL);A._backend.openssl_assert(C[0]!=A._backend._ffi.NULL);A._backend.openssl_assert(D[0]!=A._backend._ffi.NULL);A._backend._lib.RSA_get0_factors(A._rsa_cdata,E,F);A._backend.openssl_assert(E[0]!=A._backend._ffi.NULL);A._backend.openssl_assert(F[0]!=A._backend._ffi.NULL);A._backend._lib.RSA_get0_crt_params(A._rsa_cdata,G,I,J);A._backend.openssl_assert(G[0]!=A._backend._ffi.NULL);A._backend.openssl_assert(I[0]!=A._backend._ffi.NULL);A._backend.openssl_assert(J[0]!=A._backend._ffi.NULL);return L(p=A._backend._bn_to_int(E[0]),q=A._backend._bn_to_int(F[0]),d=A._backend._bn_to_int(D[0]),dmp1=A._backend._bn_to_int(G[0]),dmq1=A._backend._bn_to_int(I[0]),iqmp=A._backend._bn_to_int(J[0]),public_numbers=H(e=A._backend._bn_to_int(C[0]),n=A._backend._bn_to_int(B[0])))
	def private_bytes(A,encoding:W.Encoding,format:W.PrivateFormat,encryption_algorithm:W.KeySerializationEncryption):return A._backend._private_key_bytes(encoding,format,encryption_algorithm,A,A._evp_pkey,A._rsa_cdata)
	def sign(A,data:C,padding:O,algorithm:M.Union[Y.Prehashed,S.HashAlgorithm]):C=algorithm;B=data;A._enable_blinding();B,C=R(B,C);return l(A._backend,padding,C,A,B)
class á(ó):
	_evp_pkey:object;_rsa_cdata:object;_key_size:Q
	def __init__(A,backend:o,rsa_cdata,evp_pkey):A._backend=backend;A._rsa_cdata=rsa_cdata;A._evp_pkey=evp_pkey;B=A._backend._ffi.new(P);A._backend._lib.RSA_get0_key(A._rsa_cdata,B,A._backend._ffi.NULL,A._backend._ffi.NULL);A._backend.openssl_assert(B[0]!=A._backend._ffi.NULL);A._key_size=A._backend._lib.BN_num_bits(B[0])
	@f
	def key_size(self):return self._key_size
	def __eq__(A,other:object):
		B=other
		if not I(B,á):return NotImplemented
		return A._backend._lib.EVP_PKEY_cmp(A._evp_pkey,B._evp_pkey)==1
	def encrypt(A,plaintext:C,padding:O):return c(A._backend,A,plaintext,padding)
	def public_numbers(A):B=A._backend._ffi.new(P);C=A._backend._ffi.new(P);A._backend._lib.RSA_get0_key(A._rsa_cdata,B,C,A._backend._ffi.NULL);A._backend.openssl_assert(B[0]!=A._backend._ffi.NULL);A._backend.openssl_assert(C[0]!=A._backend._ffi.NULL);return H(e=A._backend._bn_to_int(C[0]),n=A._backend._bn_to_int(B[0]))
	def public_bytes(A,encoding:W.Encoding,format:W.PublicFormat):return A._backend._public_key_bytes(encoding,format,A,A._evp_pkey,A._rsa_cdata)
	def verify(C,signature:C,data:C,padding:O,algorithm:M.Union[Y.Prehashed,S.HashAlgorithm]):B=algorithm;A=data;A,B=R(A,B);m(C._backend,padding,B,C,signature,A)
	def recover_data_from_signature(A,signature:C,padding:O,algorithm:M.Optional[S.HashAlgorithm]):
		B=algorithm
		if I(B,Y.Prehashed):raise X('Prehashed is only supported in the sign and verify methods. It cannot be used with recover_data_from_signature.')
		return n(A._backend,padding,B,A,signature)