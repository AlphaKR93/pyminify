Ø='Unable to parse PKCS7 data'
Ö='format is invalid with this key'
Õ='encoding must be an item from the Encoding enum'
Ô='password'
Ó='Password was given but private key is not encrypted.'
Ò='CRYPTOGRAPHY_PASSWORD_DATA *'
Ñ='Unsupported key type.'
Ð='EVP_PKEY_ED448'
Ï='EVP_PKEY_X448'
Í='EVP_PKEY_ED25519'
Ê='Invalid EC key.'
É='Cryptography_pem_password_cb'
Ä=range
Ã=type
À=True
º='ascii'
µ=getattr
ª=TypeError
y=len
t=False
r=isinstance
n=bytes
m=bool
l=None
k=ValueError
j=int
import collections as Ù,contextlib as Ú,itertools as Û,typing as p
from contextlib import contextmanager as Ü
from C import utils as Á,x509 as x
from C.B import A,B
from C.D.B.A import aead
from C.D.B.A.C import ã
from C.D.B.A.D import à
from C.D.B.A.F import g,f
from C.D.B.A.G import â,á
from cryptography.hazmat.bindings._rust import openssl as h
from C.D.C.A import binding as Ë
from C.D.D import hashes as q,serialization as i
from C.D.D.A import C
from C.D.D.D import dh as u,dsa as v,ec as s,rsa as z
from C.D.D.D.F import e,d,K,E
from C.D.D.E import BlockCipherAlgorithm as Ý,CipherAlgorithm as Â
from C.D.D.E.B import X,L,M,S,SM4,N,Y,J,P,R,U,W
from C.D.D.E.D import H,Q,V,T,Z,GCM,O,XTS,G
from C.D.D.N import ssh
from C.D.D.N.B import PBES,D,I,a,b
Ì=Ù.namedtuple('_MemoryBIO',['bio','char_ptr'])
class Þ:0
class o:
	name='openssl';_fips_aead={b'aes-128-ccm',b'aes-192-ccm',b'aes-256-ccm',b'aes-128-gcm',b'aes-192-gcm',b'aes-256-gcm'};_fips_ciphers=X,;_fips_hashes=q.SHA224,q.SHA256,q.SHA384,q.SHA512,q.SHA512_224,q.SHA512_256,q.SHA3_224,q.SHA3_256,q.SHA3_384,q.SHA3_512,q.SHAKE128,q.SHAKE256;_fips_ecdh_curves=s.SECP224R1,s.SECP256R1,s.SECP384R1,s.SECP521R1;_fips_rsa_min_key_size=2048;_fips_rsa_min_public_exponent=65537;_fips_dsa_min_modulus=1<<2048;_fips_dh_min_key_size=2048;_fips_dh_min_modulus=1<<_fips_dh_min_key_size
	def __init__(A):
		A._binding=Ë.Binding();A._ffi=A._binding.ffi;A._lib=A._binding.lib;A._fips_enabled=h.is_fips_enabled();A._cipher_registry={};A._register_default_ciphers();A._dh_types=[A._lib.EVP_PKEY_DH]
		if A._lib.Cryptography_HAS_EVP_PKEY_DHX:A._dh_types.append(A._lib.EVP_PKEY_DHX)
	def __repr__(A):return'<OpenSSLBackend(version: {}, FIPS: {}, Legacy: {})>'.format(A.openssl_version_text(),A._fips_enabled,A._binding._legacy_provider_loaded)
	def openssl_assert(A,ok:m,errors:p.Optional[p.List[h.OpenSSLError]]=l):return Ë._openssl_assert(A._lib,ok,errors=errors)
	def _enable_fips(A):A._binding._enable_fips();assert h.is_fips_enabled();A._fips_enabled=h.is_fips_enabled()
	def openssl_version_text(A):return A._ffi.string(A._lib.OpenSSL_version(A._lib.OPENSSL_VERSION)).decode(º)
	def openssl_version_number(A):return A._lib.OpenSSL_version_num()
	def _evp_md_from_algorithm(C,algorithm:q.HashAlgorithm):
		A=algorithm
		if A.name=='blake2b'or A.name=='blake2s':B='{}{}'.format(A.name,A.digest_size*8).encode(º)
		else:B=A.name.encode(º)
		D=C._lib.EVP_get_digestbyname(B);return D
	def _evp_md_non_null_from_algorithm(A,algorithm:q.HashAlgorithm):B=A._evp_md_from_algorithm(algorithm);A.openssl_assert(B!=A._ffi.NULL);return B
	def hash_supported(A,algorithm:q.HashAlgorithm):
		B=algorithm
		if A._fips_enabled and not r(B,A._fips_hashes):return t
		C=A._evp_md_from_algorithm(B);return C!=A._ffi.NULL
	def signature_hash_supported(A,algorithm:q.HashAlgorithm):
		B=algorithm
		if A._fips_enabled and r(B,q.SHA1):return t
		return A.hash_supported(B)
	def scrypt_supported(A):
		if A._fips_enabled:return t
		else:return A._lib.Cryptography_HAS_SCRYPT==1
	def hmac_supported(A,algorithm:q.HashAlgorithm):
		B=algorithm
		if A._fips_enabled and r(B,q.SHA1):return À
		return A.hash_supported(B)
	def cipher_supported(A,cipher:Â,mode:G):
		B=cipher
		if A._fips_enabled:
			if not r(B,A._fips_ciphers):return t
		try:C=A._cipher_registry[Ã(B),Ã(mode)]
		except KeyError:return t
		D=C(A,B,mode);return A._ffi.NULL!=D
	def register_cipher_adapter(C,cipher_cls,mode_cls,adapter):
		B=mode_cls;A=cipher_cls
		if(A,B)in C._cipher_registry:raise k('Duplicate registration for: {} {}.'.format(A,B))
		C._cipher_registry[A,B]=adapter
	def _register_default_ciphers(A):
		D='{cipher.name}-{cipher.key_size}-{mode.name}'
		for C in[X,L,M]:
			for B in[H,T,Z,O,Q,V,GCM]:A.register_cipher_adapter(C,B,w(D))
		for B in[H,T,Z,O,Q]:A.register_cipher_adapter(N,B,w(D))
		for B in[H,Q,V,O]:A.register_cipher_adapter(J,B,w('des-ede3-{mode.name}'))
		A.register_cipher_adapter(J,Z,w('des-ede3'));A.register_cipher_adapter(Y,Ã(l),w('chacha20'));A.register_cipher_adapter(X,XTS,ß)
		for B in[Z,H,O,Q,T]:A.register_cipher_adapter(SM4,B,w('sm4-{mode.name}'))
		if A._binding._legacy_provider_loaded or not A._lib.CRYPTOGRAPHY_OPENSSL_300_OR_GREATER:
			for B in[H,Q,O,Z]:A.register_cipher_adapter(P,B,w('bf-{mode.name}'))
			for B in[H,Q,O,Z]:A.register_cipher_adapter(W,B,w('seed-{mode.name}'))
			for(C,B)in Û.product([R,U],[H,O,Q,Z]):A.register_cipher_adapter(C,B,w('{cipher.name}-{mode.name}'))
			A.register_cipher_adapter(S,Ã(l),w('rc4'));A.register_cipher_adapter(Þ,Ã(l),w('rc2'))
	def create_symmetric_encryption_ctx(A,cipher:Â,mode:G):return ã(A,cipher,mode,ã._ENCRYPT)
	def create_symmetric_decryption_ctx(A,cipher:Â,mode:G):return ã(A,cipher,mode,ã._DECRYPT)
	def pbkdf2_hmac_supported(A,algorithm:q.HashAlgorithm):return A.hmac_supported(algorithm)
	def _consume_errors(A):return h.capture_error_stack()
	def _bn_to_int(A,bn):assert bn!=A._ffi.NULL;A.openssl_assert(not A._lib.BN_is_negative(bn));D=A._lib.BN_num_bytes(bn);B=A._ffi.new('unsigned char[]',D);C=A._lib.BN_bn2bin(bn,B);A.openssl_assert(C>=0);E=j.from_bytes(A._ffi.buffer(B)[:C],'big');return E
	def _int_to_bn(A,num:j):B=num.to_bytes(j(num.bit_length()/8.+1),'big');C=A._lib.BN_bin2bn(B,y(B),A._ffi.NULL);A.openssl_assert(C!=A._ffi.NULL);return C
	def generate_rsa_private_key(A,public_exponent:j,key_size:j):E=key_size;D=public_exponent;z._verify_rsa_parameters(D,E);B=A._lib.RSA_new();A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.RSA_free);C=A._int_to_bn(D);C=A._ffi.gc(C,A._lib.BN_free);F=A._lib.RSA_generate_key_ex(B,E,C,A._ffi.NULL);A.openssl_assert(F==1);G=A._rsa_cdata_to_evp_pkey(B);return â(A,B,G,unsafe_skip_rsa_key_validation=À)
	def generate_rsa_parameters_supported(B,public_exponent:j,key_size:j):A=public_exponent;return A>=3 and A&1!=0 and key_size>=512
	def load_rsa_private_numbers(A,numbers:z.RSAPrivateNumbers,unsafe_skip_rsa_key_validation:m):B=numbers;z._check_private_key_components(B.p,B.q,B.d,B.dmp1,B.dmq1,B.iqmp,B.public_numbers.e,B.public_numbers.n);C=A._lib.RSA_new();A.openssl_assert(C!=A._ffi.NULL);C=A._ffi.gc(C,A._lib.RSA_free);E=A._int_to_bn(B.p);F=A._int_to_bn(B.q);G=A._int_to_bn(B.d);H=A._int_to_bn(B.dmp1);I=A._int_to_bn(B.dmq1);J=A._int_to_bn(B.iqmp);K=A._int_to_bn(B.public_numbers.e);L=A._int_to_bn(B.public_numbers.n);D=A._lib.RSA_set0_factors(C,E,F);A.openssl_assert(D==1);D=A._lib.RSA_set0_key(C,L,K,G);A.openssl_assert(D==1);D=A._lib.RSA_set0_crt_params(C,H,I,J);A.openssl_assert(D==1);M=A._rsa_cdata_to_evp_pkey(C);return â(A,C,M,unsafe_skip_rsa_key_validation=unsafe_skip_rsa_key_validation)
	def load_rsa_public_numbers(A,numbers:z.RSAPublicNumbers):C=numbers;z._check_public_key_components(C.e,C.n);B=A._lib.RSA_new();A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.RSA_free);D=A._int_to_bn(C.e);E=A._int_to_bn(C.n);F=A._lib.RSA_set0_key(B,E,D,A._ffi.NULL);A.openssl_assert(F==1);G=A._rsa_cdata_to_evp_pkey(B);return á(A,B,G)
	def _create_evp_pkey_gc(A):B=A._lib.EVP_PKEY_new();A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.EVP_PKEY_free);return B
	def _rsa_cdata_to_evp_pkey(A,rsa_cdata):B=A._create_evp_pkey_gc();C=A._lib.EVP_PKEY_set1_RSA(B,rsa_cdata);A.openssl_assert(C==1);return B
	def _bytes_to_bio(A,data:n):B=A._ffi.from_buffer(data);C=A._lib.BIO_new_mem_buf(B,y(data));A.openssl_assert(C!=A._ffi.NULL);return Ì(A._ffi.gc(C,A._lib.BIO_free),B)
	def _create_mem_bio_gc(A):C=A._lib.BIO_s_mem();A.openssl_assert(C!=A._ffi.NULL);B=A._lib.BIO_new(C);A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.BIO_free);return B
	def _read_mem_bio(A,bio):B=A._ffi.new('char **');C=A._lib.BIO_get_mem_data(bio,B);A.openssl_assert(C>0);A.openssl_assert(B[0]!=A._ffi.NULL);D=A._ffi.buffer(B[0],C)[:];return D
	def _evp_pkey_to_private_key(B,evp_pkey,unsafe_skip_rsa_key_validation:m):
		G=unsafe_skip_rsa_key_validation;C=evp_pkey;D=B._lib.EVP_PKEY_id(C)
		if D==B._lib.EVP_PKEY_RSA:E=B._lib.EVP_PKEY_get1_RSA(C);B.openssl_assert(E!=B._ffi.NULL);E=B._ffi.gc(E,B._lib.RSA_free);return â(B,E,C,unsafe_skip_rsa_key_validation=G)
		elif D==B._lib.EVP_PKEY_RSA_PSS and not B._lib.CRYPTOGRAPHY_IS_LIBRESSL and not B._lib.CRYPTOGRAPHY_IS_BORINGSSL and not B._lib.CRYPTOGRAPHY_OPENSSL_LESS_THAN_111E:E=B._lib.EVP_PKEY_get1_RSA(C);B.openssl_assert(E!=B._ffi.NULL);E=B._ffi.gc(E,B._lib.RSA_free);H=B._create_mem_bio_gc();I=B._lib.i2d_RSAPrivateKey_bio(H,E);B.openssl_assert(I==1);return B.load_der_private_key(B._read_mem_bio(H),password=l,unsafe_skip_rsa_key_validation=G)
		elif D==B._lib.EVP_PKEY_DSA:return h.dsa.private_key_from_ptr(j(C))
		elif D==B._lib.EVP_PKEY_EC:F=B._lib.EVP_PKEY_get1_EC_KEY(C);B.openssl_assert(F!=B._ffi.NULL);F=B._ffi.gc(F,B._lib.EC_KEY_free);return g(B,F,C)
		elif D in B._dh_types:return h.dh.private_key_from_ptr(j(C))
		elif D==µ(B._lib,Í,l):return h.ed25519.private_key_from_ptr(j(C))
		elif D==µ(B._lib,Ï,l):return h.x448.private_key_from_ptr(j(C))
		elif D==B._lib.EVP_PKEY_X25519:return h.x25519.private_key_from_ptr(j(C))
		elif D==µ(B._lib,Ð,l):return h.ed448.private_key_from_ptr(j(C))
		else:raise A(Ñ)
	def _evp_pkey_to_public_key(B,evp_pkey):
		C=evp_pkey;D=B._lib.EVP_PKEY_id(C)
		if D==B._lib.EVP_PKEY_RSA:E=B._lib.EVP_PKEY_get1_RSA(C);B.openssl_assert(E!=B._ffi.NULL);E=B._ffi.gc(E,B._lib.RSA_free);return á(B,E,C)
		elif D==B._lib.EVP_PKEY_RSA_PSS and not B._lib.CRYPTOGRAPHY_IS_LIBRESSL and not B._lib.CRYPTOGRAPHY_IS_BORINGSSL and not B._lib.CRYPTOGRAPHY_OPENSSL_LESS_THAN_111E:E=B._lib.EVP_PKEY_get1_RSA(C);B.openssl_assert(E!=B._ffi.NULL);E=B._ffi.gc(E,B._lib.RSA_free);G=B._create_mem_bio_gc();H=B._lib.i2d_RSAPublicKey_bio(G,E);B.openssl_assert(H==1);return B.load_der_public_key(B._read_mem_bio(G))
		elif D==B._lib.EVP_PKEY_DSA:return h.dsa.public_key_from_ptr(j(C))
		elif D==B._lib.EVP_PKEY_EC:
			F=B._lib.EVP_PKEY_get1_EC_KEY(C)
			if F==B._ffi.NULL:I=B._consume_errors();raise k('Unable to load EC key',I)
			F=B._ffi.gc(F,B._lib.EC_KEY_free);return f(B,F,C)
		elif D in B._dh_types:return h.dh.public_key_from_ptr(j(C))
		elif D==µ(B._lib,Í,l):return h.ed25519.public_key_from_ptr(j(C))
		elif D==µ(B._lib,Ï,l):return h.x448.public_key_from_ptr(j(C))
		elif D==B._lib.EVP_PKEY_X25519:return h.x25519.public_key_from_ptr(j(C))
		elif D==µ(B._lib,Ð,l):return h.ed448.public_key_from_ptr(j(C))
		else:raise A(Ñ)
	def _oaep_hash_supported(B,algorithm:q.HashAlgorithm):
		A=algorithm
		if B._fips_enabled and r(A,q.SHA1):return t
		return r(A,(q.SHA1,q.SHA224,q.SHA256,q.SHA384,q.SHA512))
	def rsa_padding_supported(B,padding:C):
		A=padding
		if r(A,E):return À
		elif r(A,K)and r(A._mgf,e):
			if B._fips_enabled and r(A._mgf._algorithm,q.SHA1):return À
			else:return B.hash_supported(A._mgf._algorithm)
		elif r(A,d)and r(A._mgf,e):return B._oaep_hash_supported(A._mgf._algorithm)and B._oaep_hash_supported(A._algorithm)
		else:return t
	def rsa_encryption_supported(A,padding:C):
		B=padding
		if A._fips_enabled and r(B,E):return t
		else:return A.rsa_padding_supported(B)
	def generate_dsa_parameters(B,key_size:j):
		A=key_size
		if A not in(1024,2048,3072,4096):raise k('Key size must be 1024, 2048, 3072, or 4096 bits.')
		return h.dsa.generate_parameters(A)
	def generate_dsa_private_key(A,parameters:v.DSAParameters):return parameters.generate_private_key()
	def generate_dsa_private_key_and_parameters(A,key_size:j):B=A.generate_dsa_parameters(key_size);return A.generate_dsa_private_key(B)
	def load_dsa_private_numbers(B,numbers:v.DSAPrivateNumbers):A=numbers;v._check_dsa_private_numbers(A);return h.dsa.from_private_numbers(A)
	def load_dsa_public_numbers(B,numbers:v.DSAPublicNumbers):A=numbers;v._check_dsa_parameters(A.parameter_numbers);return h.dsa.from_public_numbers(A)
	def load_dsa_parameter_numbers(B,numbers:v.DSAParameterNumbers):A=numbers;v._check_dsa_parameters(A);return h.dsa.from_parameter_numbers(A)
	def dsa_supported(A):return not A._lib.CRYPTOGRAPHY_IS_BORINGSSL and not A._fips_enabled
	def dsa_hash_supported(A,algorithm:q.HashAlgorithm):
		if not A.dsa_supported():return t
		return A.signature_hash_supported(algorithm)
	def cmac_algorithm_supported(B,algorithm):A=algorithm;return B.cipher_supported(A,H(b'\x00'*A.block_size))
	def create_cmac_ctx(A,algorithm:Ý):return à(A,algorithm)
	def load_pem_private_key(A,data:n,password:p.Optional[n],unsafe_skip_rsa_key_validation:m):return A._load_key(A._lib.PEM_read_bio_PrivateKey,data,password,unsafe_skip_rsa_key_validation)
	def load_pem_public_key(A,data:n):
		D=A._bytes_to_bio(data);E=A._ffi.new(Ò);B=A._lib.PEM_read_bio_PUBKEY(D.bio,A._ffi.NULL,A._ffi.addressof(A._lib._original_lib,É),E)
		if B!=A._ffi.NULL:B=A._ffi.gc(B,A._lib.EVP_PKEY_free);return A._evp_pkey_to_public_key(B)
		else:
			A._consume_errors();F=A._lib.BIO_reset(D.bio);A.openssl_assert(F==1);C=A._lib.PEM_read_bio_RSAPublicKey(D.bio,A._ffi.NULL,A._ffi.addressof(A._lib._original_lib,É),E)
			if C!=A._ffi.NULL:C=A._ffi.gc(C,A._lib.RSA_free);B=A._rsa_cdata_to_evp_pkey(C);return á(A,C,B)
			else:A._handle_key_loading_error()
	def load_pem_parameters(A,data:n):return h.dh.from_pem_parameters(data)
	def load_der_private_key(A,data:n,password:p.Optional[n],unsafe_skip_rsa_key_validation:m):
		C=unsafe_skip_rsa_key_validation;B=password;E=A._bytes_to_bio(data);D=A._evp_pkey_from_der_traditional_key(E,B)
		if D:return A._evp_pkey_to_private_key(D,C)
		else:return A._load_key(A._lib.d2i_PKCS8PrivateKey_bio,data,B,C)
	def _evp_pkey_from_der_traditional_key(A,bio_data,password):
		B=A._lib.d2i_PrivateKey_bio(bio_data.bio,A._ffi.NULL)
		if B!=A._ffi.NULL:
			B=A._ffi.gc(B,A._lib.EVP_PKEY_free)
			if password is not l:raise ª(Ó)
			return B
		else:A._consume_errors();return
	def load_der_public_key(A,data:n):
		D=A._bytes_to_bio(data);B=A._lib.d2i_PUBKEY_bio(D.bio,A._ffi.NULL)
		if B!=A._ffi.NULL:B=A._ffi.gc(B,A._lib.EVP_PKEY_free);return A._evp_pkey_to_public_key(B)
		else:
			A._consume_errors();E=A._lib.BIO_reset(D.bio);A.openssl_assert(E==1);C=A._lib.d2i_RSAPublicKey_bio(D.bio,A._ffi.NULL)
			if C!=A._ffi.NULL:C=A._ffi.gc(C,A._lib.RSA_free);B=A._rsa_cdata_to_evp_pkey(C);return á(A,C,B)
			else:A._handle_key_loading_error()
	def load_der_parameters(A,data:n):return h.dh.from_der_parameters(data)
	def _cert2ossl(A,cert:x.Certificate):C=cert.public_bytes(i.Encoding.DER);D=A._bytes_to_bio(C);B=A._lib.d2i_X509_bio(D.bio,A._ffi.NULL);A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.X509_free);return B
	def _ossl2cert(A,x509_ptr:p.Any):B=A._create_mem_bio_gc();C=A._lib.i2d_X509_bio(B,x509_ptr);A.openssl_assert(C==1);return x.load_der_x509_certificate(A._read_mem_bio(B))
	def _key2ossl(A,key:a):C=key.private_bytes(i.Encoding.DER,i.PrivateFormat.PKCS8,i.NoEncryption());D=A._bytes_to_bio(C);B=A._lib.d2i_PrivateKey_bio(D.bio,A._ffi.NULL);A.openssl_assert(B!=A._ffi.NULL);return A._ffi.gc(B,A._lib.EVP_PKEY_free)
	def _load_key(A,openssl_read_func,data,password,unsafe_skip_rsa_key_validation):
		C=password;E=A._bytes_to_bio(data);B=A._ffi.new(Ò)
		if C is not l:Á._check_byteslike(Ô,C);F=A._ffi.from_buffer(C);B.password=F;B.length=y(C)
		D=openssl_read_func(E.bio,A._ffi.NULL,A._ffi.addressof(A._lib._original_lib,É),B)
		if D==A._ffi.NULL:
			if B.error!=0:
				A._consume_errors()
				if B.error==-1:raise ª('Password was not given but private key is encrypted')
				else:assert B.error==-2;raise k('Passwords longer than {} bytes are not supported by this backend.'.format(B.maxsize-1))
			else:A._handle_key_loading_error()
		D=A._ffi.gc(D,A._lib.EVP_PKEY_free)
		if C is not l and B.called==0:raise ª(Ó)
		assert C is not l and B.called==1 or C is l;return A._evp_pkey_to_private_key(D,unsafe_skip_rsa_key_validation)
	def _handle_key_loading_error(A):
		B=A._consume_errors()
		if not B:raise k('Could not deserialize key data. The data may be in an incorrect format or it may be encrypted with an unsupported algorithm.')
		elif B[0]._lib_reason_match(A._lib.ERR_LIB_EVP,A._lib.EVP_R_BAD_DECRYPT)or B[0]._lib_reason_match(A._lib.ERR_LIB_PKCS12,A._lib.PKCS12_R_PKCS12_CIPHERFINAL_ERROR)or A._lib.Cryptography_HAS_PROVIDERS and B[0]._lib_reason_match(A._lib.ERR_LIB_PROV,A._lib.PROV_R_BAD_DECRYPT):raise k('Bad decrypt. Incorrect password?')
		elif any(B._lib_reason_match(A._lib.ERR_LIB_EVP,A._lib.EVP_R_UNSUPPORTED_PRIVATE_KEY_ALGORITHM)for B in B):raise k('Unsupported public key algorithm.')
		else:raise k('Could not deserialize key data. The data may be in an incorrect format, it may be encrypted with an unsupported algorithm, or it may be an unsupported key type (e.g. EC curves with explicit parameters).',B)
	def elliptic_curve_supported(B,curve:s.EllipticCurve):
		try:C=B._elliptic_curve_to_nid(curve)
		except A:C=B._lib.NID_undef
		D=B._lib.EC_GROUP_new_by_curve_name(C)
		if D==B._ffi.NULL:B._consume_errors();return t
		else:B.openssl_assert(C!=B._lib.NID_undef);B._lib.EC_GROUP_free(D);return À
	def elliptic_curve_signature_algorithm_supported(A,signature_algorithm:s.EllipticCurveSignatureAlgorithm,curve:s.EllipticCurve):
		if not r(signature_algorithm,s.ECDSA):return t
		return A.elliptic_curve_supported(curve)
	def generate_elliptic_curve_private_key(C,curve:s.EllipticCurve):
		D=curve
		if C.elliptic_curve_supported(D):E=C._ec_key_new_by_curve(D);F=C._lib.EC_KEY_generate_key(E);C.openssl_assert(F==1);G=C._ec_cdata_to_evp_pkey(E);return g(C,E,G)
		else:raise A(f"Backend object does not support {D.name}.",B.UNSUPPORTED_ELLIPTIC_CURVE)
	def load_elliptic_curve_private_numbers(A,numbers:s.EllipticCurvePrivateNumbers):
		H=numbers;E=H.public_numbers;B=A._ec_key_new_by_curve(E.curve);I=A._ffi.gc(A._int_to_bn(H.private_value),A._lib.BN_clear_free);F=A._lib.EC_KEY_set_private_key(B,I)
		if F!=1:A._consume_errors();raise k(Ê)
		with A._tmp_bn_ctx()as G:
			A._ec_key_set_public_key_affine_coordinates(B,E.x,E.y,G);D=A._lib.EC_KEY_get0_group(B);A.openssl_assert(D!=A._ffi.NULL);J=Î._lib.EC_KEY_get0_public_key(B);A.openssl_assert(J!=A._ffi.NULL);C=A._lib.EC_POINT_new(D);A.openssl_assert(C!=A._ffi.NULL);C=A._ffi.gc(C,A._lib.EC_POINT_free);F=A._lib.EC_POINT_mul(D,C,I,A._ffi.NULL,A._ffi.NULL,G);A.openssl_assert(F==1)
			if A._lib.EC_POINT_cmp(D,J,C,G)!=0:raise k(Ê)
		K=A._ec_cdata_to_evp_pkey(B);return g(A,B,K)
	def load_elliptic_curve_public_numbers(A,numbers:s.EllipticCurvePublicNumbers):
		B=numbers;C=A._ec_key_new_by_curve(B.curve)
		with A._tmp_bn_ctx()as D:A._ec_key_set_public_key_affine_coordinates(C,B.x,B.y,D)
		E=A._ec_cdata_to_evp_pkey(C);return f(A,C,E)
	def load_elliptic_curve_public_bytes(A,curve:s.EllipticCurve,point_bytes:n):
		F=point_bytes;C=A._ec_key_new_by_curve(curve);D=A._lib.EC_KEY_get0_group(C);A.openssl_assert(D!=A._ffi.NULL);B=A._lib.EC_POINT_new(D);A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.EC_POINT_free)
		with A._tmp_bn_ctx()as G:
			E=A._lib.EC_POINT_oct2point(D,B,F,y(F),G)
			if E!=1:A._consume_errors();raise k('Invalid public bytes for the given curve')
		E=A._lib.EC_KEY_set_public_key(C,B);A.openssl_assert(E==1);H=A._ec_cdata_to_evp_pkey(C);return f(A,C,H)
	def derive_elliptic_curve_private_key(A,private_value:j,curve:s.EllipticCurve):
		I=private_value;D=A._ec_key_new_by_curve(curve);E=A._lib.EC_KEY_get0_group(D);A.openssl_assert(E!=A._ffi.NULL);C=A._lib.EC_POINT_new(E);A.openssl_assert(C!=A._ffi.NULL);C=A._ffi.gc(C,A._lib.EC_POINT_free);G=A._int_to_bn(I);G=A._ffi.gc(G,A._lib.BN_clear_free)
		with A._tmp_bn_ctx()as F:
			B=A._lib.EC_POINT_mul(E,C,G,A._ffi.NULL,A._ffi.NULL,F);A.openssl_assert(B==1);J=A._lib.BN_CTX_get(F);K=A._lib.BN_CTX_get(F);B=A._lib.EC_POINT_get_affine_coordinates(E,C,J,K,F)
			if B!=1:A._consume_errors();raise k('Unable to derive key from private_value')
		B=A._lib.EC_KEY_set_public_key(D,C);A.openssl_assert(B==1);H=A._int_to_bn(I);H=A._ffi.gc(H,A._lib.BN_clear_free);B=A._lib.EC_KEY_set_private_key(D,H);A.openssl_assert(B==1);L=A._ec_cdata_to_evp_pkey(D);return g(A,D,L)
	def _ec_key_new_by_curve(A,curve:s.EllipticCurve):B=A._elliptic_curve_to_nid(curve);return A._ec_key_new_by_curve_nid(B)
	def _ec_key_new_by_curve_nid(A,curve_nid:j):B=A._lib.EC_KEY_new_by_curve_name(curve_nid);A.openssl_assert(B!=A._ffi.NULL);return A._ffi.gc(B,A._lib.EC_KEY_free)
	def elliptic_curve_exchange_algorithm_supported(A,algorithm:s.ECDH,curve:s.EllipticCurve):
		B=curve
		if A._fips_enabled and not r(B,A._fips_ecdh_curves):return t
		return A.elliptic_curve_supported(B)and r(algorithm,s.ECDH)
	def _ec_cdata_to_evp_pkey(A,ec_cdata):B=A._create_evp_pkey_gc();C=A._lib.EVP_PKEY_set1_EC_KEY(B,ec_cdata);A.openssl_assert(C==1);return B
	def _elliptic_curve_to_nid(D,curve:s.EllipticCurve):
		C=curve;F={'secp192r1':'prime192v1','secp256r1':'prime256v1'};G=F.get(C.name,C.name);E=D._lib.OBJ_sn2nid(G.encode())
		if E==D._lib.NID_undef:raise A(f"{C.name} is not a supported elliptic curve",B.UNSUPPORTED_ELLIPTIC_CURVE)
		return E
	@Ü
	def _tmp_bn_ctx(self):
		A=self;B=A._lib.BN_CTX_new();A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.BN_CTX_free);A._lib.BN_CTX_start(B)
		try:yield B
		finally:A._lib.BN_CTX_end(B)
	def _ec_key_set_public_key_affine_coordinates(A,ec_cdata,x:j,y:j,bn_ctx):
		E=ec_cdata
		if x<0 or y<0:raise k('Invalid EC key. Both x and y must be non-negative.')
		x=A._ffi.gc(A._int_to_bn(x),A._lib.BN_free);y=A._ffi.gc(A._int_to_bn(y),A._lib.BN_free);C=A._lib.EC_KEY_get0_group(E);A.openssl_assert(C!=A._ffi.NULL);B=A._lib.EC_POINT_new(C);A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.EC_POINT_free);D=A._lib.EC_POINT_set_affine_coordinates(C,B,x,y,bn_ctx)
		if D!=1:A._consume_errors();raise k(Ê)
		D=A._lib.EC_KEY_set_public_key(E,B);A.openssl_assert(D==1)
	def _private_key_bytes(A,encoding:i.Encoding,format:i.PrivateFormat,encryption_algorithm:i.KeySerializationEncryption,key,evp_pkey,cdata):
		H=cdata;G=evp_pkey;E=encoding;B=encryption_algorithm
		if not r(E,i.Encoding):raise ª(Õ)
		if not r(format,i.PrivateFormat):raise ª('format must be an item from the PrivateFormat enum')
		if not r(B,i.KeySerializationEncryption):raise ª('Encryption algorithm must be a KeySerializationEncryption instance')
		if r(B,i.NoEncryption):D=b''
		elif r(B,i.BestAvailableEncryption):
			D=B.password
			if y(D)>1023:raise k('Passwords longer than 1023 bytes are not supported by this backend')
		elif r(B,i._KeySerializationEncryption)and B._format is format is i.PrivateFormat.OpenSSH:D=B.password
		else:raise k('Unsupported encryption type')
		if format is i.PrivateFormat.PKCS8:
			if E is i.Encoding.PEM:C=A._lib.PEM_write_bio_PKCS8PrivateKey
			elif E is i.Encoding.DER:C=A._lib.i2d_PKCS8PrivateKey_bio
			else:raise k('Unsupported encoding for PKCS8')
			return A._private_key_bytes_via_bio(C,G,D)
		if format is i.PrivateFormat.TraditionalOpenSSL:
			if A._fips_enabled and not r(B,i.NoEncryption):raise k('Encrypted traditional OpenSSL format is not supported in FIPS mode.')
			F=A._lib.EVP_PKEY_id(G)
			if E is i.Encoding.PEM:
				if F==A._lib.EVP_PKEY_RSA:C=A._lib.PEM_write_bio_RSAPrivateKey
				else:assert F==A._lib.EVP_PKEY_EC;C=A._lib.PEM_write_bio_ECPrivateKey
				return A._private_key_bytes_via_bio(C,H,D)
			if E is i.Encoding.DER:
				if D:raise k('Encryption is not supported for DER encoded traditional OpenSSL keys')
				if F==A._lib.EVP_PKEY_RSA:C=A._lib.i2d_RSAPrivateKey_bio
				else:assert F==A._lib.EVP_PKEY_EC;C=A._lib.i2d_ECPrivateKey_bio
				return A._bio_func_output(C,H)
			raise k('Unsupported encoding for TraditionalOpenSSL')
		if format is i.PrivateFormat.OpenSSH:
			if E is i.Encoding.PEM:return ssh._serialize_ssh_private_key(key,D,B)
			raise k('OpenSSH private key format can only be used with PEM encoding')
		raise k(Ö)
	def _private_key_bytes_via_bio(A,write_bio,evp_pkey,password):
		B=password
		if not B:C=A._ffi.NULL
		else:C=A._lib.EVP_get_cipherbyname(b'aes-256-cbc')
		return A._bio_func_output(write_bio,evp_pkey,C,B,y(B),A._ffi.NULL,A._ffi.NULL)
	def _bio_func_output(A,write_bio,*C):B=A._create_mem_bio_gc();D=write_bio(B,*C);A.openssl_assert(D==1);return A._read_mem_bio(B)
	def _public_key_bytes(A,encoding:i.Encoding,format:i.PublicFormat,key,evp_pkey,cdata):
		D=evp_pkey;B=encoding
		if not r(B,i.Encoding):raise ª(Õ)
		if not r(format,i.PublicFormat):raise ª('format must be an item from the PublicFormat enum')
		if format is i.PublicFormat.SubjectPublicKeyInfo:
			if B is i.Encoding.PEM:C=A._lib.PEM_write_bio_PUBKEY
			elif B is i.Encoding.DER:C=A._lib.i2d_PUBKEY_bio
			else:raise k('SubjectPublicKeyInfo works only with PEM or DER encoding')
			return A._bio_func_output(C,D)
		if format is i.PublicFormat.PKCS1:
			E=A._lib.EVP_PKEY_id(D)
			if E!=A._lib.EVP_PKEY_RSA:raise k('PKCS1 format is supported only for RSA keys')
			if B is i.Encoding.PEM:C=A._lib.PEM_write_bio_RSAPublicKey
			elif B is i.Encoding.DER:C=A._lib.i2d_RSAPublicKey_bio
			else:raise k('PKCS1 works only with PEM or DER encoding')
			return A._bio_func_output(C,cdata)
		if format is i.PublicFormat.OpenSSH:
			if B is i.Encoding.OpenSSH:return ssh.serialize_ssh_public_key(key)
			raise k('OpenSSH format must be used with OpenSSH encoding')
		raise k(Ö)
	def dh_supported(A):return not A._lib.CRYPTOGRAPHY_IS_BORINGSSL
	def generate_dh_parameters(A,generator:j,key_size:j):return h.dh.generate_parameters(generator,key_size)
	def generate_dh_private_key(A,parameters:u.DHParameters):return parameters.generate_private_key()
	def generate_dh_private_key_and_parameters(A,generator:j,key_size:j):return A.generate_dh_private_key(A.generate_dh_parameters(generator,key_size))
	def load_dh_private_numbers(A,numbers:u.DHPrivateNumbers):return h.dh.from_private_numbers(numbers)
	def load_dh_public_numbers(A,numbers:u.DHPublicNumbers):return h.dh.from_public_numbers(numbers)
	def load_dh_parameter_numbers(A,numbers:u.DHParameterNumbers):return h.dh.from_parameter_numbers(numbers)
	def dh_parameters_supported(A,p:j,g:j,q:p.Optional[j]=l):
		try:h.dh.from_parameter_numbers(u.DHParameterNumbers(p=p,g=g,q=q))
		except k:return t
		else:return À
	def dh_x942_serialization_supported(A):return A._lib.Cryptography_HAS_EVP_PKEY_DHX==1
	def x25519_load_public_bytes(A,data:n):return h.x25519.from_public_bytes(data)
	def x25519_load_private_bytes(A,data:n):return h.x25519.from_private_bytes(data)
	def x25519_generate_key(A):return h.x25519.generate_key()
	def x25519_supported(A):
		if A._fips_enabled:return t
		return not A._lib.CRYPTOGRAPHY_LIBRESSL_LESS_THAN_370
	def x448_load_public_bytes(A,data:n):return h.x448.from_public_bytes(data)
	def x448_load_private_bytes(A,data:n):return h.x448.from_private_bytes(data)
	def x448_generate_key(A):return h.x448.generate_key()
	def x448_supported(A):
		if A._fips_enabled:return t
		return not A._lib.CRYPTOGRAPHY_IS_LIBRESSL and not A._lib.CRYPTOGRAPHY_IS_BORINGSSL
	def ed25519_supported(A):
		if A._fips_enabled:return t
		return A._lib.CRYPTOGRAPHY_HAS_WORKING_ED25519
	def ed25519_load_public_bytes(A,data:n):return h.ed25519.from_public_bytes(data)
	def ed25519_load_private_bytes(A,data:n):return h.ed25519.from_private_bytes(data)
	def ed25519_generate_key(A):return h.ed25519.generate_key()
	def ed448_supported(A):
		if A._fips_enabled:return t
		return not A._lib.CRYPTOGRAPHY_IS_LIBRESSL and not A._lib.CRYPTOGRAPHY_IS_BORINGSSL
	def ed448_load_public_bytes(A,data:n):return h.ed448.from_public_bytes(data)
	def ed448_load_private_bytes(A,data:n):return h.ed448.from_private_bytes(data)
	def ed448_generate_key(A):return h.ed448.generate_key()
	def aead_cipher_supported(A,cipher):return aead._aead_cipher_supported(A,cipher)
	def _zero_data(B,data,length:j):
		for A in Ä(length):data[A]=0
	@Ú.contextmanager
	def _zeroed_null_terminated_buf(self,data):
		B=data;A=self
		if B is l:yield A._ffi.NULL
		else:
			C=y(B);D=A._ffi.new('char[]',C+1);A._ffi.memmove(D,B,C)
			try:yield D
			finally:A._zero_data(D,C)
	def load_key_and_certificates_from_pkcs12(B,data:n,password:p.Optional[n]):A=B.load_pkcs12(data,password);return A.key,A.cert.certificate if A.cert else l,[A.certificate for A in A.additional_certs]
	def load_pkcs12(A,data:n,password:p.Optional[n]):
		G=password
		if G is not l:Á._check_byteslike(Ô,G)
		R=A._bytes_to_bio(data);E=A._lib.d2i_PKCS12_bio(R.bio,A._ffi.NULL)
		if E==A._ffi.NULL:A._consume_errors();raise k('Could not deserialize PKCS12 data')
		E=A._ffi.gc(E,A._lib.PKCS12_free);H=A._ffi.new('EVP_PKEY **');J=A._ffi.new('X509 **');F=A._ffi.new('Cryptography_STACK_OF_X509 **')
		with A._zeroed_null_terminated_buf(G)as S:T=A._lib.PKCS12_parse(E,S,H,J,F)
		if T==0:A._consume_errors();raise k('Invalid password or PKCS12 data')
		L=l;M=l;N=[]
		if H[0]!=A._ffi.NULL:U=A._ffi.gc(H[0],A._lib.EVP_PKEY_free);M=A._evp_pkey_to_private_key(U,unsafe_skip_rsa_key_validation=t)
		if J[0]!=A._ffi.NULL:
			B=A._ffi.gc(J[0],A._lib.X509_free);V=A._ossl2cert(B);O=l;C=A._lib.X509_alias_get0(B,A._ffi.NULL)
			if C!=A._ffi.NULL:O=A._ffi.string(C)
			L=D(V,O)
		if F[0]!=A._ffi.NULL:
			W=A._ffi.gc(F[0],A._lib.sk_X509_free);P=A._lib.sk_X509_num(F[0])
			if A._lib.CRYPTOGRAPHY_OPENSSL_300_OR_GREATER or A._lib.CRYPTOGRAPHY_IS_BORINGSSL:K=Ä(P)
			else:K=reversed(Ä(P))
			for X in K:
				B=A._lib.sk_X509_value(W,X);A.openssl_assert(B!=A._ffi.NULL);B=A._ffi.gc(B,A._lib.X509_free);Y=A._ossl2cert(B);Q=l;C=A._lib.X509_alias_get0(B,A._ffi.NULL)
				if C!=A._ffi.NULL:Q=A._ffi.string(C)
				N.append(D(Y,Q))
		return I(M,L,N)
	def serialize_key_and_certificates_to_pkcs12(B,name:p.Optional[n],key:p.Optional[a],cert:p.Optional[x.Certificate],cas:p.Optional[p.List[b]],encryption_algorithm:i.KeySerializationEncryption):
		P=cas;O=name;C=encryption_algorithm;Q=l
		if O is not l:Á._check_bytes('name',O)
		if r(C,i.NoEncryption):E=-1;F=-1;L=0;M=0;G=B._ffi.NULL
		elif r(C,i.BestAvailableEncryption):
			if B._lib.CRYPTOGRAPHY_OPENSSL_300_OR_GREATER:E=B._lib.NID_aes_256_cbc;F=B._lib.NID_aes_256_cbc
			else:E=B._lib.NID_pbe_WithSHA1And3_Key_TripleDES_CBC;F=B._lib.NID_pbe_WithSHA1And3_Key_TripleDES_CBC
			L=20000;M=1;G=B._ffi.NULL;Q=C.password
		elif r(C,i._KeySerializationEncryption)and C._format is i.PrivateFormat.PKCS12:
			E=0;F=0;L=20000;M=1;Q=C.password;R=C._key_cert_algorithm
			if R is PBES.PBESv1SHA1And3KeyTripleDESCBC:E=B._lib.NID_pbe_WithSHA1And3_Key_TripleDES_CBC;F=B._lib.NID_pbe_WithSHA1And3_Key_TripleDES_CBC
			elif R is PBES.PBESv2SHA256AndAES256CBC:
				if not B._lib.CRYPTOGRAPHY_OPENSSL_300_OR_GREATER:raise A('PBESv2 is not supported by this version of OpenSSL')
				E=B._lib.NID_aes_256_cbc;F=B._lib.NID_aes_256_cbc
			else:assert R is l
			if C._hmac_hash is not l:
				if not B._lib.Cryptography_HAS_PKCS12_SET_MAC:raise A('Setting MAC algorithm is not supported by this version of OpenSSL.')
				G=B._evp_md_non_null_from_algorithm(C._hmac_hash);B.openssl_assert(G!=B._ffi.NULL)
			else:G=B._ffi.NULL
			if C._kdf_rounds is not l:L=C._kdf_rounds
		else:raise k('Unsupported key encryption type')
		if P is l or y(P)==0:J=B._ffi.NULL
		else:
			J=B._lib.sk_X509_new_null();J=B._ffi.gc(J,B._lib.sk_X509_free);V=[]
			for N in P:
				if r(N,D):
					S=N.friendly_name;K=B._cert2ossl(N.certificate)
					if S is l:H=B._lib.X509_alias_set1(K,B._ffi.NULL,-1)
					else:H=B._lib.X509_alias_set1(K,S,y(S))
					B.openssl_assert(H==1)
				else:K=B._cert2ossl(N)
				V.append(K);H=B._lib.sk_X509_push(J,K);Î.openssl_assert(H>=1)
		with B._zeroed_null_terminated_buf(Q)as T:
			with B._zeroed_null_terminated_buf(O)as W:
				X=B._cert2ossl(cert)if cert else B._ffi.NULL;Y=B._key2ossl(key)if key is not l else B._ffi.NULL;I=B._lib.PKCS12_create(T,W,Y,X,J,F,E,L,M,0)
				if I==B._ffi.NULL:Z=B._consume_errors();raise k('Failed to create PKCS12 (does the key match the certificate?)',Z)
			if B._lib.Cryptography_HAS_PKCS12_SET_MAC and G!=B._ffi.NULL:B._lib.PKCS12_set_mac(I,T,-1,B._ffi.NULL,0,M,G)
		B.openssl_assert(I!=B._ffi.NULL);I=B._ffi.gc(I,B._lib.PKCS12_free);U=B._create_mem_bio_gc();H=B._lib.i2d_PKCS12_bio(U,I);B.openssl_assert(H>0);return B._read_mem_bio(U)
	def poly1305_supported(A):
		if A._fips_enabled:return t
		return A._lib.Cryptography_HAS_POLY1305==1
	def pkcs7_supported(A):return not A._lib.CRYPTOGRAPHY_IS_BORINGSSL
	def load_pem_pkcs7_certificates(A,data:n):
		Á._check_bytes('data',data);C=A._bytes_to_bio(data);B=A._lib.PEM_read_bio_PKCS7(C.bio,A._ffi.NULL,A._ffi.NULL,A._ffi.NULL)
		if B==A._ffi.NULL:A._consume_errors();raise k(Ø)
		B=A._ffi.gc(B,A._lib.PKCS7_free);return A._load_pkcs7_certificates(B)
	def load_der_pkcs7_certificates(A,data:n):
		Á._check_bytes('data',data);C=A._bytes_to_bio(data);B=A._lib.d2i_PKCS7_bio(C.bio,A._ffi.NULL)
		if B==A._ffi.NULL:A._consume_errors();raise k(Ø)
		B=A._ffi.gc(B,A._lib.PKCS7_free);return A._load_pkcs7_certificates(B)
	def _load_pkcs7_certificates(C,p7):
		D=C._lib.OBJ_obj2nid(p7.type);C.openssl_assert(D!=C._lib.NID_undef)
		if D!=C._lib.NID_pkcs7_signed:raise A('Only basic signed structures are currently supported. NID for this data was {}'.format(D),B.UNSUPPORTED_SERIALIZATION)
		E=[]
		if p7.d.sign==C._ffi.NULL:return E
		G=p7.d.sign.cert;H=C._lib.sk_X509_num(G)
		for I in Ä(H):F=C._lib.sk_X509_value(G,I);C.openssl_assert(F!=C._ffi.NULL);J=C._ossl2cert(F);E.append(J)
		return E
class w:
	def __init__(A,fmt:str):A._fmt=fmt
	def __call__(D,backend:o,cipher:Â,mode:G):
		A=backend;C=D._fmt.format(cipher=cipher,mode=mode).lower();B=A._lib.EVP_get_cipherbyname(C.encode(º))
		if B==A._ffi.NULL and A._lib.Cryptography_HAS_300_EVP_CIPHER:B=A._lib.EVP_CIPHER_fetch(A._ffi.NULL,C.encode(º),A._ffi.NULL)
		A._consume_errors();return B
def ß(backend:o,cipher:X,mode):A=f"aes-{cipher.key_size//2}-xts";return backend._lib.EVP_get_cipherbyname(A.encode(º))
Î=o()