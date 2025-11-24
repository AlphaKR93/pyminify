d='uint8_t[]'
c='size_t *'
T=b'-siv'
N='unsigned char[]'
I='int *'
H=isinstance
F=None
D=int
B=len
A=bytes
import typing as C
from C.B import E
def O(backend:o,cipher:G):from C.D.D.E.A import L;return backend._lib.Cryptography_HAS_EVP_AEAD and H(cipher,L)
def k(backend:o,cipher:G):
	C=cipher;A=backend
	if O(A,C):return True
	else:
		B=P(C)
		if A._fips_enabled and B not in A._fips_aead:return False
		if B.endswith(T):return A._lib.CRYPTOGRAPHY_OPENSSL_300_OR_GREATER==1
		else:return A._lib.EVP_get_cipherbyname(B)!=A._ffi.NULL
def l(backend:o,cipher:G,key:A):
	B=cipher;A=backend
	if O(A,B):return e(A,B,key)
	else:return h(A,B,key)
def m(backend:o,cipher:G,nonce:A,data:A,associated_data:C.List[A],tag_length:D,ctx:C.Any=F):
	E=tag_length;D=associated_data;C=nonce;B=cipher;A=backend
	if O(A,B):return f(A,B,C,data,D,E,ctx)
	else:return i(A,B,C,data,D,E,ctx)
def n(backend:o,cipher:G,nonce:A,data:A,associated_data:C.List[A],tag_length:D,ctx:C.Any=F):
	E=tag_length;D=associated_data;C=nonce;B=cipher;A=backend
	if O(A,B):return g(A,B,C,data,D,E,ctx)
	else:return j(A,B,C,data,D,E,ctx)
def e(backend:o,cipher:G,key:A,tag_len:C.Optional[D]=F):C=tag_len;A=backend;E=R(A,cipher);assert E is not F;G=A._ffi.from_buffer(key);C=A._lib.EVP_AEAD_DEFAULT_TAG_LENGTH if C is F else C;D=A._lib.Cryptography_EVP_AEAD_CTX_new(E,G,B(key),C);A.openssl_assert(D!=A._ffi.NULL);D=A._ffi.gc(D,A._lib.EVP_AEAD_CTX_free);return D
def R(backend:o,cipher:G):from C.D.D.E.A import L;assert H(cipher,L);return backend._lib.EVP_aead_chacha20_poly1305()
def f(backend:o,cipher:G,nonce:A,data:A,associated_data:C.List[A],tag_length:D,ctx:C.Any):D=nonce;C=data;A=backend;assert ctx is not F;E=R(A,cipher);assert E is not F;G=A._ffi.new(c);H=B(C)+A._lib.EVP_AEAD_max_overhead(E);I=A._ffi.new(d,H);K=A._ffi.from_buffer(C);L=A._ffi.from_buffer(D);J=b''.join(associated_data);M=A._ffi.from_buffer(J);N=A._lib.EVP_AEAD_CTX_seal(ctx,I,G,H,L,B(D),K,B(C),M,B(J));A.openssl_assert(N==1);O=A._ffi.buffer(I,G[0])[:];return O
def g(backend:o,cipher:G,nonce:A,data:A,associated_data:C.List[A],tag_length:D,ctx:C.Any):
	D=nonce;C=data;A=backend
	if B(C)<tag_length:raise E
	assert ctx is not F;G=A._ffi.new(c);H=B(C);I=A._ffi.new(d,H);K=A._ffi.from_buffer(C);L=A._ffi.from_buffer(D);J=b''.join(associated_data);M=A._ffi.from_buffer(J);N=A._lib.EVP_AEAD_CTX_open(ctx,I,G,H,L,B(D),K,B(C),M,B(J))
	if N==0:A._consume_errors();raise E
	O=A._ffi.buffer(I,G[0])[:];return O
K=1
Q=0
def P(cipher:G):
	C='ascii';A=cipher;from C.D.D.E.A import J,V,W,M,L
	if H(A,L):return b'chacha20-poly1305'
	elif H(A,J):return f"aes-{B(A._key)*8}-ccm".encode(C)
	elif H(A,W):return f"aes-{B(A._key)*8}-ocb".encode(C)
	elif H(A,M):return f"aes-{B(A._key)*8//2}-siv".encode(C)
	else:assert H(A,V);return f"aes-{B(A._key)*8}-gcm".encode(C)
def S(cipher_name:A,backend:o):
	C=cipher_name;A=backend
	if C.endswith(T):B=A._lib.EVP_CIPHER_fetch(A._ffi.NULL,C,A._ffi.NULL);A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.EVP_CIPHER_free)
	else:B=A._lib.EVP_get_cipherbyname(C);A.openssl_assert(B!=A._ffi.NULL)
	return B
def h(backend:o,cipher:G,key:A):A=backend;B=A._lib.EVP_CIPHER_CTX_new();A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.EVP_CIPHER_CTX_free);C=P(cipher);D=S(C,A);E=A._ffi.from_buffer(key);F=A._lib.EVP_CipherInit_ex(B,D,A._ffi.NULL,E,A._ffi.NULL,0);A.openssl_assert(F!=0);return B
def U(backend:o,cipher_name:A,key:A,nonce:A,tag:C.Optional[A],tag_len:D,operation:D):
	I=nonce;H=cipher_name;G=operation;A=backend;J=S(H,A);C=A._lib.EVP_CIPHER_CTX_new();C=A._ffi.gc(C,A._lib.EVP_CIPHER_CTX_free);E=A._lib.EVP_CipherInit_ex(C,J,A._ffi.NULL,A._ffi.NULL,A._ffi.NULL,D(G==K));A.openssl_assert(E!=0);E=A._lib.EVP_CIPHER_CTX_ctrl(C,A._lib.EVP_CTRL_AEAD_SET_IVLEN,B(I),A._ffi.NULL);A.openssl_assert(E!=0)
	if G==Q:assert tag is not F;X(A,C,tag)
	elif H.endswith(b'-ccm'):E=A._lib.EVP_CIPHER_CTX_ctrl(C,A._lib.EVP_CTRL_AEAD_SET_TAG,tag_len,A._ffi.NULL);A.openssl_assert(E!=0)
	L=A._ffi.from_buffer(I);M=A._ffi.from_buffer(key);E=A._lib.EVP_CipherInit_ex(C,A._ffi.NULL,A._ffi.NULL,M,L,D(G==K));A.openssl_assert(E!=0);return C
def X(backend,ctx,tag:A):A=backend;C=A._ffi.from_buffer(tag);D=A._lib.EVP_CIPHER_CTX_ctrl(ctx,A._lib.EVP_CTRL_AEAD_SET_TAG,B(tag),C);A.openssl_assert(D!=0)
def Y(backend,ctx,nonce:A,operation:D):A=backend;B=A._ffi.from_buffer(nonce);C=A._lib.EVP_CipherInit_ex(ctx,A._ffi.NULL,A._ffi.NULL,A._ffi.NULL,B,D(operation==K));A.openssl_assert(C!=0)
def Z(backend:o,ctx,data_len:D):A=backend;B=A._ffi.new(I);C=A._lib.EVP_CipherUpdate(ctx,A._ffi.NULL,B,A._ffi.NULL,data_len);A.openssl_assert(C!=0)
def a(backend:o,ctx,associated_data:A):C=associated_data;A=backend;D=A._ffi.new(I);E=A._ffi.from_buffer(C);F=A._lib.EVP_CipherUpdate(ctx,A._ffi.NULL,D,E,B(C));A.openssl_assert(F!=0)
def b(backend:o,ctx,data:A):
	C=data;A=backend;D=A._ffi.new(I);F=A._ffi.new(N,B(C));G=A._ffi.from_buffer(C);H=A._lib.EVP_CipherUpdate(ctx,F,D,G,B(C))
	if H==0:A._consume_errors();raise E
	return A._ffi.buffer(F,D[0])[:]
def i(backend:o,cipher:G,nonce:A,data:A,associated_data:C.List[A],tag_length:D,ctx:C.Any=F):
	Q=nonce;E=tag_length;D=cipher;C=ctx;A=backend;from C.D.D.E.A import J,M
	if C is F:V=P(D);C=U(A,V,D._key,Q,F,E,K)
	else:Y(A,C,Q,K)
	if H(D,J):Z(A,C,B(data))
	for W in associated_data:a(A,C,W)
	G=b(A,C,data);R=A._ffi.new(I);S=A._ffi.new(N,16);L=A._lib.EVP_CipherFinal_ex(C,S,R);A.openssl_assert(L!=0);G+=A._ffi.buffer(S,R[0])[:];T=A._ffi.new(N,E);L=A._lib.EVP_CIPHER_CTX_ctrl(C,A._lib.EVP_CTRL_AEAD_GET_TAG,E,T);A.openssl_assert(L!=0);O=A._ffi.buffer(T)[:]
	if H(D,M):A.openssl_assert(B(O)==16);return O+G
	else:return G+O
def j(backend:o,cipher:G,nonce:A,data:A,associated_data:C.List[A],tag_length:D,ctx:C.Any=F):
	V=nonce;K=cipher;G=tag_length;D=ctx;C=data;A=backend;from C.D.D.E.A import J,M
	if B(C)<G:raise E
	if H(K,M):R=C[:G];C=C[G:]
	else:R=C[-G:];C=C[:-G]
	if D is F:W=P(K);D=U(A,W,K._key,V,R,G,Q)
	else:Y(A,D,V,Q);X(A,D,R)
	if H(K,J):Z(A,D,B(C))
	for c in associated_data:a(A,D,c)
	if H(K,J):
		L=A._ffi.new(I);O=A._ffi.new(N,B(C));d=A._ffi.from_buffer(C);S=A._lib.EVP_CipherUpdate(D,O,L,d,B(C))
		if S!=1:A._consume_errors();raise E
		T=A._ffi.buffer(O,L[0])[:]
	else:
		T=b(A,D,C);L=A._ffi.new(I);O=A._ffi.new(N,16);S=A._lib.EVP_CipherFinal_ex(D,O,L);T+=A._ffi.buffer(O,L[0])[:]
		if S==0:A._consume_errors();raise E
	return T