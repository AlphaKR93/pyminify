I='int *'
O=None
L=ValueError
H=len
G=isinstance
F=bytes
from C.B import E,A,B
from C.D.D import ciphers as U
from C.D.D.E import algorithms as V,modes as K
class ã:
	_ENCRYPT=1;_DECRYPT=0;_MAX_CHUNK_SIZE=2**30-1
	def __init__(C,backend:o,cipher,mode,operation:int):
		Q=operation;I=cipher;D=mode;C._backend=backend;C._cipher=I;C._mode=D;C._operation=Q;C._tag=O
		if G(C._cipher,U.BlockCipherAlgorithm):C._block_size_bytes=C._cipher.block_size//8
		else:C._block_size_bytes=1
		J=C._backend._lib.EVP_CIPHER_CTX_new();J=C._backend._ffi.gc(J,C._backend._lib.EVP_CIPHER_CTX_free);W=C._backend._cipher_registry
		try:X=W[type(I),type(D)]
		except KeyError:raise A('cipher {} in {} mode is not supported by this backend.'.format(I.name,D.name if D else D),B.UNSUPPORTED_CIPHER)
		T=X(C._backend,I,D)
		if T==C._backend._ffi.NULL:
			R=f"cipher {I.name} "
			if D is not O:R+=f"in {D.name} mode "
			R+='is not supported by this backend (Your version of OpenSSL may be too old. Current version: {}.)'.format(C._backend.openssl_version_text());raise A(R,B.UNSUPPORTED_CIPHER)
		if G(D,K.ModeWithInitializationVector):M=C._backend._ffi.from_buffer(D.initialization_vector)
		elif G(D,K.ModeWithTweak):M=C._backend._ffi.from_buffer(D.tweak)
		elif G(D,K.ModeWithNonce):M=C._backend._ffi.from_buffer(D.nonce)
		elif G(I,V.ChaCha20):M=C._backend._ffi.from_buffer(I.nonce)
		else:M=C._backend._ffi.NULL
		E=C._backend._lib.EVP_CipherInit_ex(J,T,C._backend._ffi.NULL,C._backend._ffi.NULL,C._backend._ffi.NULL,Q);C._backend.openssl_assert(E!=0);E=C._backend._lib.EVP_CIPHER_CTX_set_key_length(J,H(I.key));C._backend.openssl_assert(E!=0)
		if G(D,K.GCM):
			E=C._backend._lib.EVP_CIPHER_CTX_ctrl(J,C._backend._lib.EVP_CTRL_AEAD_SET_IVLEN,H(M),C._backend._ffi.NULL);C._backend.openssl_assert(E!=0)
			if D.tag is not O:E=C._backend._lib.EVP_CIPHER_CTX_ctrl(J,C._backend._lib.EVP_CTRL_AEAD_SET_TAG,H(D.tag),D.tag);C._backend.openssl_assert(E!=0);C._tag=D.tag
		E=C._backend._lib.EVP_CipherInit_ex(J,C._backend._ffi.NULL,C._backend._ffi.NULL,C._backend._ffi.from_buffer(I.key),M,Q);S=C._backend._consume_errors();N=C._backend._lib
		if E==0 and(not N.CRYPTOGRAPHY_IS_LIBRESSL and S[0]._lib_reason_match(N.ERR_LIB_EVP,N.EVP_R_XTS_DUPLICATED_KEYS)or N.Cryptography_HAS_PROVIDERS and S[0]._lib_reason_match(N.ERR_LIB_PROV,N.PROV_R_XTS_DUPLICATED_KEYS)):raise L('In XTS mode duplicated keys are not allowed')
		C._backend.openssl_assert(E!=0,errors=S);C._backend._lib.EVP_CIPHER_CTX_set_padding(J,0);C._ctx=J
	def update(A,data:F):B=bytearray(H(data)+A._block_size_bytes-1);C=A.update_into(data,B);return F(B[:C])
	def update_into(A,data:F,buf:F):
		C=data;D=H(C)
		if H(buf)<D+A._block_size_bytes-1:raise L('buffer must be at least {} bytes for this payload'.format(H(C)+A._block_size_bytes-1))
		B=0;E=0;F=A._backend._ffi.new(I);N=A._backend._ffi.from_buffer(buf,require_writable=True);O=A._backend._ffi.from_buffer(C)
		while B!=D:
			P=N+E;Q=O+B;J=min(A._MAX_CHUNK_SIZE,D-B);M=A._backend._lib.EVP_CipherUpdate(A._ctx,P,F,Q,J)
			if M==0 and G(A._mode,K.XTS):A._backend._consume_errors();raise L('In XTS mode you must supply at least a full block in the first update call. For AES this is 16 bytes.')
			else:A._backend.openssl_assert(M!=0)
			B+=J;E+=F[0]
		return E
	def finalize(A):
		M='unsigned char[]'
		if A._operation==A._DECRYPT and G(A._mode,K.ModeWithAuthenticationTag)and A.tag is O:raise L('Authentication tag must be provided when decrypting.')
		F=A._backend._ffi.new(M,A._block_size_bytes);H=A._backend._ffi.new(I);C=A._backend._lib.EVP_CipherFinal_ex(A._ctx,F,H)
		if C==0:
			D=A._backend._consume_errors()
			if not D and G(A._mode,K.GCM):raise E
			B=A._backend._lib;A._backend.openssl_assert(D[0]._lib_reason_match(B.ERR_LIB_EVP,B.EVP_R_DATA_NOT_MULTIPLE_OF_BLOCK_LENGTH)or B.Cryptography_HAS_PROVIDERS and D[0]._lib_reason_match(B.ERR_LIB_PROV,B.PROV_R_WRONG_FINAL_BLOCK_LENGTH)or B.CRYPTOGRAPHY_IS_BORINGSSL and D[0].reason==B.CIPHER_R_DATA_NOT_MULTIPLE_OF_BLOCK_LENGTH,errors=D);raise L('The length of the provided data is not a multiple of the block length.')
		if G(A._mode,K.GCM)and A._operation==A._ENCRYPT:J=A._backend._ffi.new(M,A._block_size_bytes);C=A._backend._lib.EVP_CIPHER_CTX_ctrl(A._ctx,A._backend._lib.EVP_CTRL_AEAD_GET_TAG,A._block_size_bytes,J);A._backend.openssl_assert(C!=0);A._tag=A._backend._ffi.buffer(J)[:]
		C=A._backend._lib.EVP_CIPHER_CTX_reset(A._ctx);A._backend.openssl_assert(C==1);return A._backend._ffi.buffer(F)[:H[0]]
	def finalize_with_tag(A,tag:F):
		B=tag;C=H(B)
		if C<A._mode._min_tag_length:raise L('Authentication tag must be {} bytes or longer.'.format(A._mode._min_tag_length))
		elif C>A._block_size_bytes:raise L('Authentication tag cannot be more than {} bytes.'.format(A._block_size_bytes))
		D=A._backend._lib.EVP_CIPHER_CTX_ctrl(A._ctx,A._backend._lib.EVP_CTRL_AEAD_SET_TAG,H(B),B);A._backend.openssl_assert(D!=0);A._tag=B;return A.finalize()
	def authenticate_additional_data(A,data:F):B=A._backend._ffi.new(I);C=A._backend._lib.EVP_CipherUpdate(A._ctx,A._backend._ffi.NULL,B,A._backend._ffi.from_buffer(data),H(data));A._backend.openssl_assert(C!=0)
	@property
	def tag(self):return self._tag