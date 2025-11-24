K=hasattr
J='ed25519 is not supported by this version of OpenSSL.'
I=classmethod
D=bytes
import abc as C
from C.B import A,B
from cryptography.hazmat.bindings._rust import openssl as F
from C.D.D import _serialization as E
class G(metaclass=C.ABCMeta):
	@I
	def from_public_bytes(cls,data:D):
		from C.D.B.A.B import Î
		if not Î.ed25519_supported():raise A(J,B.UNSUPPORTED_PUBLIC_KEY_ALGORITHM)
		return Î.ed25519_load_public_bytes(data)
	@C.abstractmethod
	def public_bytes(self,encoding:E.Encoding,format:E.PublicFormat):0
	@C.abstractmethod
	def public_bytes_raw(self):0
	@C.abstractmethod
	def verify(self,signature:D,data:D):0
	@C.abstractmethod
	def __eq__(self,other:object):0
if K(F,'ed25519'):G.register(F.ed25519.Ed25519PublicKey)
class H(metaclass=C.ABCMeta):
	@I
	def generate(cls):
		from C.D.B.A.B import Î
		if not Î.ed25519_supported():raise A(J,B.UNSUPPORTED_PUBLIC_KEY_ALGORITHM)
		return Î.ed25519_generate_key()
	@I
	def from_private_bytes(cls,data:D):
		from C.D.B.A.B import Î
		if not Î.ed25519_supported():raise A(J,B.UNSUPPORTED_PUBLIC_KEY_ALGORITHM)
		return Î.ed25519_load_private_bytes(data)
	@C.abstractmethod
	def public_key(self):0
	@C.abstractmethod
	def private_bytes(self,encoding:E.Encoding,format:E.PrivateFormat,encryption_algorithm:E.KeySerializationEncryption):0
	@C.abstractmethod
	def private_bytes_raw(self):0
	@C.abstractmethod
	def sign(self,data:D):0
if K(F,'x25519'):H.register(F.ed25519.Ed25519PrivateKey)