F=bytes
D='Context was already finalized.'
A=None
import typing as B
from C import utils as G
from C.B import C
from C.D.D import ciphers as E
class H:
	_ctx:B.Optional[à];_algorithm:E.BlockCipherAlgorithm
	def __init__(B,algorithm:E.BlockCipherAlgorithm,backend:B.Any=A,ctx:B.Optional[à]=A):
		C=algorithm
		if not isinstance(C,E.BlockCipherAlgorithm):raise TypeError('Expected instance of BlockCipherAlgorithm.')
		B._algorithm=C
		if ctx is A:from C.D.B.A.B import Î;B._ctx=Î.create_cmac_ctx(B._algorithm)
		else:B._ctx=ctx
	def update(B,data:F):
		if B._ctx is A:raise C(D)
		G._check_bytes('data',data);B._ctx.update(data)
	def finalize(B):
		if B._ctx is A:raise C(D)
		E=B._ctx.finalize();B._ctx=A;return E
	def verify(B,signature:F):
		E=signature;G._check_bytes('signature',E)
		if B._ctx is A:raise C(D)
		F,B._ctx=B._ctx,A;F.verify(E)
	def copy(B):
		if B._ctx is A:raise C(D)
		return H(B._algorithm,ctx=B._ctx.copy())