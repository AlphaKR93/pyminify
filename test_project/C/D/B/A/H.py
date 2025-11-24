E=ValueError
C=bytes
import typing as B
from C.D.D import hashes as D
from C.D.D.D.I import A
def S(backend:o,evp_pkey,peer_public_key):
	F=peer_public_key;A=backend;B=A._lib.EVP_PKEY_CTX_new(evp_pkey,A._ffi.NULL);A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.EVP_PKEY_CTX_free);C=A._lib.EVP_PKEY_derive_init(B);A.openssl_assert(C==1)
	if A._lib.Cryptography_HAS_EVP_PKEY_SET_PEER_EX:C=A._lib.EVP_PKEY_derive_set_peer_ex(B,F._evp_pkey,0)
	else:C=A._lib.EVP_PKEY_derive_set_peer(B,F._evp_pkey)
	A.openssl_assert(C==1);D=A._ffi.new('size_t *');C=A._lib.EVP_PKEY_derive(B,A._ffi.NULL,D);A.openssl_assert(C==1);A.openssl_assert(D[0]>0);G=A._ffi.new('unsigned char[]',D[0]);C=A._lib.EVP_PKEY_derive(B,G,D)
	if C!=1:H=A._consume_errors();raise E('Error computing shared key.',H)
	return A._ffi.buffer(G,D[0])[:]
def R(data:C,algorithm:B.Union[A,D.HashAlgorithm]):
	C=data;B=algorithm
	if not isinstance(B,A):F=D.Hash(B);F.update(C);C=F.finalize()
	else:B=B._algorithm
	if len(C)!=B.digest_size:raise E("The provided data must be the same length as the hash algorithm's digest size.")
	return C,B