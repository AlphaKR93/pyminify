from cryptography.hazmat.bindings._rust import asn1 as B
from C.D.D import hashes as C
D=B.decode_dss_signature
E=B.encode_dss_signature
class A:
	def __init__(B,algorithm:C.HashAlgorithm):
		A=algorithm
		if not isinstance(A,C.HashAlgorithm):raise TypeError('Expected instance of HashAlgorithm.')
		B._algorithm=A;B._digest_size=A.digest_size
	@property
	def digest_size(self):return self._digest_size