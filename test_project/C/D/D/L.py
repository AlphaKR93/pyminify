R='data'
J=b''
I='Context was already finalized.'
H=len
G=ValueError
F=None
B=int
A=bytes
import abc as K,typing as D
from C import utils as L
from C.B import C
from cryptography.hazmat.bindings._rust import check_ansix923_padding as S,check_pkcs7_padding as T
class E(metaclass=K.ABCMeta):
	@K.abstractmethod
	def update(self,data:A):0
	@K.abstractmethod
	def finalize(self):0
def M(block_size:B):
	A=block_size
	if not 0<=A<=2040:raise G('block_size must be in range(0, 2041).')
	if A%8!=0:raise G('block_size must be a multiple of 8.')
def N(buffer_:D.Optional[A],data:A,block_size:B):
	D=block_size;B=buffer_
	if B is F:raise C(I)
	L._check_byteslike(R,data);B+=A(data);E=H(B)//(D//8);G=B[:E*(D//8)];B=B[E*(D//8):];return B,G
def O(buffer_:D.Optional[A],block_size:B,paddingfn:D.Callable[[B],A]):
	A=buffer_
	if A is F:raise C(I)
	B=block_size//8-H(A);return A+paddingfn(B)
def P(buffer_:D.Optional[A],data:A,block_size:B):
	D=block_size;B=buffer_
	if B is F:raise C(I)
	L._check_byteslike(R,data);B+=A(data);E=max(H(B)//(D//8)-1,0);G=B[:E*(D//8)];B=B[E*(D//8):];return B,G
def Q(buffer_:D.Optional[A],block_size:B,checkfn:D.Callable[[A],B]):
	B='Invalid padding bytes.';A=buffer_
	if A is F:raise C(I)
	if H(A)!=block_size//8:raise G(B)
	D=checkfn(A)
	if not D:raise G(B)
	E=A[-1];return A[:-E]
class Y:
	def __init__(B,block_size:B):A=block_size;M(A);B.block_size=A
	def padder(A):return U(A.block_size)
	def unpadder(A):return V(A.block_size)
class U(E):
	_buffer:D.Optional[A]
	def __init__(A,block_size:B):A.block_size=block_size;A._buffer=J
	def update(A,data:A):A._buffer,B=N(A._buffer,data,A.block_size);return B
	def _padding(B,size:B):return A([size])*size
	def finalize(A):B=O(A._buffer,A.block_size,A._padding);A._buffer=F;return B
class V(E):
	_buffer:D.Optional[A]
	def __init__(A,block_size:B):A.block_size=block_size;A._buffer=J
	def update(A,data:A):A._buffer,B=P(A._buffer,data,A.block_size);return B
	def finalize(A):B=Q(A._buffer,A.block_size,T);A._buffer=F;return B
class Z:
	def __init__(B,block_size:B):A=block_size;M(A);B.block_size=A
	def padder(A):return W(A.block_size)
	def unpadder(A):return X(A.block_size)
class W(E):
	_buffer:D.Optional[A]
	def __init__(A,block_size:B):A.block_size=block_size;A._buffer=J
	def update(A,data:A):A._buffer,B=N(A._buffer,data,A.block_size);return B
	def _padding(B,size:B):return A([0])*(size-1)+A([size])
	def finalize(A):B=O(A._buffer,A.block_size,A._padding);A._buffer=F;return B
class X(E):
	_buffer:D.Optional[A]
	def __init__(A,block_size:B):A.block_size=block_size;A._buffer=J
	def update(A,data:A):A._buffer,B=P(A._buffer,data,A.block_size);return B
	def finalize(A):B=Q(A._buffer,A.block_size,S);A._buffer=F;return B