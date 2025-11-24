L='x25519'
K=hasattr
J='X25519 is not supported by this version of OpenSSL.'
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
		if not Î.x25519_supported():raise A(J,B.UNSUPPORTED_EXCHANGE_ALGORITHM)
		return Î.x25519_load_public_bytes(data)
	@C.abstractmethod
	def public_bytes(self,encoding:E.Encoding,format:E.PublicFormat):0
	@C.abstractmethod
	def public_bytes_raw(self):0
	@C.abstractmethod
	def __eq__(self,other:object):0
if K(F,L):G.register(F.x25519.X25519PublicKey)
class H(metaclass=C.ABCMeta):
	@I
	def generate(cls):
		from C.D.B.A.B import Î
		if not Î.x25519_supported():raise A(J,B.UNSUPPORTED_EXCHANGE_ALGORITHM)
		return Î.x25519_generate_key()
	@I
	def from_private_bytes(cls,data:D):
		from C.D.B.A.B import Î
		if not Î.x25519_supported():raise A(J,B.UNSUPPORTED_EXCHANGE_ALGORITHM)
		return Î.x25519_load_private_bytes(data)
	@C.abstractmethod
	def public_key(self):0
	@C.abstractmethod
	def private_bytes(self,encoding:E.Encoding,format:E.PrivateFormat,encryption_algorithm:E.KeySerializationEncryption):0
	@C.abstractmethod
	def private_bytes_raw(self):0
	@C.abstractmethod
	def exchange(self,peer_public_key:G):0
if K(F,L):H.register(F.x25519.X25519PrivateKey)