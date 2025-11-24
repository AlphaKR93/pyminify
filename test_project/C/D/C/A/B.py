I=False
H=classmethod
G=getattr
F=str
D=None
import os,sys,threading as K,types,typing as A,warnings as L,C as M
from C.B import J
from cryptography.hazmat.bindings._rust import _openssl as B,openssl as E
from C.D.C.A.A import R
def C(lib,ok:bool,errors:A.Optional[A.List[E.OpenSSLError]]=D):
	A=errors
	if not ok:
		if A is D:A=E.capture_error_stack()
		raise J('Unknown OpenSSL error. This error is commonly encountered when another library is not cleaning up the OpenSSL error stack. If you are using cryptography with another library that uses OpenSSL try disabling it before reporting a bug. Otherwise please file an issue at https://github.com/pyca/cryptography/issues with information on how to reproduce this. ({!r})'.format(A),A)
def N(loaded:bool):
	if not loaded:raise RuntimeError("OpenSSL 3.0's legacy provider failed to load. This is a fatal error by default, but cryptography supports running without legacy algorithms by setting the environment variable CRYPTOGRAPHY_OPENSSL_NO_LEGACY. If you did not expect this error, you have likely made a mistake with your OpenSSL configuration.")
def O(lib:A.Any,conditional_names:A.Dict[F,A.Callable[[],A.List[F]]]):
	A=lib;B=types.ModuleType('lib');B._original_lib=A;D=set()
	for(E,F)in conditional_names.items():
		if not G(A,E):D.update(F())
	for C in dir(A):
		if C not in D:setattr(B,C,G(A,C))
	return B
class P:
	lib:A.ClassVar=D;ffi=B.ffi;_lib_loaded=I;_init_lock=K.Lock();_legacy_provider:A.Any=ffi.NULL;_legacy_provider_loaded=I;_default_provider:A.Any=ffi.NULL
	def __init__(A):A._ensure_ffi_initialized()
	def _enable_fips(A):C(A.lib,A.lib.CRYPTOGRAPHY_OPENSSL_300_OR_GREATER);A._base_provider=A.lib.OSSL_PROVIDER_load(A.ffi.NULL,b'base');C(A.lib,A._base_provider!=A.ffi.NULL);A.lib._fips_provider=A.lib.OSSL_PROVIDER_load(A.ffi.NULL,b'fips');C(A.lib,A.lib._fips_provider!=A.ffi.NULL);B=A.lib.EVP_default_properties_enable_fips(A.ffi.NULL,1);C(A.lib,B==1)
	@H
	def _ensure_ffi_initialized(A):
		with A._init_lock:
			if not A._lib_loaded:
				A.lib=O(B.lib,R);A._lib_loaded=True
				if A.lib.CRYPTOGRAPHY_OPENSSL_300_OR_GREATER:
					if not os.environ.get('CRYPTOGRAPHY_OPENSSL_NO_LEGACY'):A._legacy_provider=A.lib.OSSL_PROVIDER_load(A.ffi.NULL,b'legacy');A._legacy_provider_loaded=A._legacy_provider!=A.ffi.NULL;N(A._legacy_provider_loaded)
					A._default_provider=A.lib.OSSL_PROVIDER_load(A.ffi.NULL,b'default');C(A.lib,A._default_provider!=A.ffi.NULL)
	@H
	def init_static_locks(cls):cls._ensure_ffi_initialized()
def Q(version:F):
	A=version;D=B.ffi.string(B.lib.CRYPTOGRAPHY_PACKAGE_VERSION)
	if A.encode('ascii')!=D:raise ImportError('The version of cryptography does not match the loaded shared object. This can happen if you have multiple copies of cryptography installed in your Python path. Please try creating a new virtual environment to resolve this issue. Loaded python version: {}, shared object version: {}'.format(A,D))
	C(B.lib,B.lib.OpenSSL_version_num()==E.openssl_version())
Q(M.__version__)
P.init_static_locks()
if sys.platform=='win32'and os.environ.get('PROCESSOR_ARCHITEW6432')is not D:L.warn('You are using cryptography on a 32-bit Python on a 64-bit Windows Operating System. Cryptography will be significantly faster if you switch to using a 64-bit Python.',UserWarning,stacklevel=2)