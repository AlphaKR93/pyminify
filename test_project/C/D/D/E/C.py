X=False
W=property
S=True
R=len
Q=ValueError
P=isinstance
O=int
J='Context was already finalized.'
B=None
A=bytes
import abc as F,typing as E
from C.B import C,H,I
from C.D.D.B import D
from C.D.D.E import modes as G
class K(metaclass=F.ABCMeta):
	@F.abstractmethod
	def update(self,data:A):0
	@F.abstractmethod
	def update_into(self,data:A,buf:A):0
	@F.abstractmethod
	def finalize(self):0
class L(K,metaclass=F.ABCMeta):
	@F.abstractmethod
	def authenticate_additional_data(self,data:A):0
class M(L,metaclass=F.ABCMeta):
	@F.abstractmethod
	def finalize_with_tag(self,tag:A):0
class N(L,metaclass=F.ABCMeta):
	@W
	@F.abstractmethod
	def tag(self):0
T=E.TypeVar('Mode',bound=E.Optional[G.Mode],covariant=S)
class Y(E.Generic[T]):
	def __init__(E,algorithm:D,mode:T,backend:E.Any=B):
		C=algorithm;A=mode
		if not P(C,D):raise TypeError('Expected interface of CipherAlgorithm.')
		if A is not B:assert P(A,G.Mode);A.validate_for_algorithm(C)
		E.algorithm=C;E.mode=A
	@E.overload
	def encryptor(self:Y[G.ModeWithAuthenticationTag]):0
	@E.overload
	def encryptor(self:U):0
	def encryptor(A):
		if P(A.mode,G.ModeWithAuthenticationTag):
			if A.mode.tag is not B:raise Q('Authentication tag must be None when encrypting.')
		from C.D.B.A.B import Î;C=Î.create_symmetric_encryption_ctx(A.algorithm,A.mode);return A._wrap_ctx(C,encrypt=S)
	@E.overload
	def decryptor(self:Y[G.ModeWithAuthenticationTag]):0
	@E.overload
	def decryptor(self:U):0
	def decryptor(A):from C.D.B.A.B import Î;B=Î.create_symmetric_decryption_ctx(A.algorithm,A.mode);return A._wrap_ctx(B,encrypt=X)
	def _wrap_ctx(B,ctx:ã,encrypt:bool):
		A=ctx
		if P(B.mode,G.ModeWithAuthenticationTag):
			if encrypt:return b(A)
			else:return a(A)
		else:return Z(A)
U=Y[E.Union[G.ModeWithNonce,G.ModeWithTweak,B,G.ECB,G.ModeWithInitializationVector]]
class Z(K):
	_ctx:E.Optional[ã]
	def __init__(A,ctx:ã):A._ctx=ctx
	def update(A,data:A):
		if A._ctx is B:raise C(J)
		return A._ctx.update(data)
	def update_into(A,data:A,buf:A):
		if A._ctx is B:raise C(J)
		return A._ctx.update_into(data,buf)
	def finalize(A):
		if A._ctx is B:raise C(J)
		D=A._ctx.finalize();A._ctx=B;return D
class V(L):
	_ctx:E.Optional[ã];_tag:E.Optional[A]
	def __init__(A,ctx:ã):A._ctx=ctx;A._bytes_processed=0;A._aad_bytes_processed=0;A._tag=B;A._updated=X
	def _check_limit(A,data_size:O):
		if A._ctx is B:raise C(J)
		A._updated=S;A._bytes_processed+=data_size
		if A._bytes_processed>A._ctx._mode._MAX_ENCRYPTED_BYTES:raise Q('{} has a maximum encrypted byte limit of {}'.format(A._ctx._mode.name,A._ctx._mode._MAX_ENCRYPTED_BYTES))
	def update(A,data:A):A._check_limit(R(data));assert A._ctx is not B;return A._ctx.update(data)
	def update_into(A,data:A,buf:A):A._check_limit(R(data));assert A._ctx is not B;return A._ctx.update_into(data,buf)
	def finalize(A):
		if A._ctx is B:raise C(J)
		D=A._ctx.finalize();A._tag=A._ctx.tag;A._ctx=B;return D
	def authenticate_additional_data(A,data:A):
		if A._ctx is B:raise C(J)
		if A._updated:raise H('Update has been called on this context.')
		A._aad_bytes_processed+=R(data)
		if A._aad_bytes_processed>A._ctx._mode._MAX_AAD_BYTES:raise Q('{} has a maximum AAD byte limit of {}'.format(A._ctx._mode.name,A._ctx._mode._MAX_AAD_BYTES))
		A._ctx.authenticate_additional_data(data)
class a(V,M):
	def finalize_with_tag(A,tag:A):
		if A._ctx is B:raise C(J)
		D=A._ctx.finalize_with_tag(tag);A._tag=A._ctx.tag;A._ctx=B;return D
class b(V,N):
	@W
	def tag(self):
		A=self
		if A._ctx is not B:raise I('You must finalize encryption before getting the tag.')
		assert A._tag is not B;return A._tag