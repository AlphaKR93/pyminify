F=None
C=bytes
from C.B import T,A,B
from C.D.D import constant_time as E
from C.D.D.E.D import H
class à:
	def __init__(C,backend:o,algorithm:G.BlockCipherAlgorithm,ctx=F):
		G=backend;E=algorithm;D=ctx
		if not G.cmac_algorithm_supported(E):raise A('This backend does not support CMAC.',B.UNSUPPORTED_CIPHER)
		C._backend=G;C._key=E.key;C._algorithm=E;C._output_length=E.block_size//8
		if D is F:I=C._backend._cipher_registry;J=I[type(E),H];K=J(C._backend,E,H);D=C._backend._lib.CMAC_CTX_new();C._backend.openssl_assert(D!=C._backend._ffi.NULL);D=C._backend._ffi.gc(D,C._backend._lib.CMAC_CTX_free);L=C._backend._ffi.from_buffer(C._key);M=C._backend._lib.CMAC_Init(D,L,len(C._key),K,C._backend._ffi.NULL);C._backend.openssl_assert(M==1)
		C._ctx=D
	def update(A,data:C):B=A._backend._lib.CMAC_Update(A._ctx,data,len(data));A._backend.openssl_assert(B==1)
	def finalize(A):B=A._backend._ffi.new('unsigned char[]',A._output_length);C=A._backend._ffi.new('size_t *',A._output_length);D=A._backend._lib.CMAC_Final(A._ctx,B,C);A._backend.openssl_assert(D==1);A._ctx=F;return A._backend._ffi.buffer(B)[:]
	def copy(A):B=A._backend._lib.CMAC_CTX_new();B=A._backend._ffi.gc(B,A._backend._lib.CMAC_CTX_free);C=A._backend._lib.CMAC_CTX_copy(B,A._ctx);A._backend.openssl_assert(C==1);return à(A._backend,A._algorithm,ctx=B)
	def verify(A,signature:C):
		B=A.finalize()
		if not E.bytes_eq(B,signature):raise T('Signature did not match digest.')