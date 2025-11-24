D=bytes
B=property
import abc as A
from C import utils as C
from cryptography.hazmat.bindings._rust import x509 as F
class G(C.Enum):X509_CERTIFICATE=0;PRE_CERTIFICATE=1
class H(C.Enum):v1=0
class I(C.Enum):ANONYMOUS=0;RSA=1;DSA=2;ECDSA=3
class ë(metaclass=A.ABCMeta):
	@B
	@A.abstractmethod
	def version(self):0
	@B
	@A.abstractmethod
	def log_id(self):0
	@B
	@A.abstractmethod
	def timestamp(self):0
	@B
	@A.abstractmethod
	def entry_type(self):0
	@B
	@A.abstractmethod
	def signature_hash_algorithm(self):0
	@B
	@A.abstractmethod
	def signature_algorithm(self):0
	@B
	@A.abstractmethod
	def signature(self):0
	@B
	@A.abstractmethod
	def extension_bytes(self):0
ë.register(F.Sct)